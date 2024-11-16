from modules.ml_halftime_metrics import calculate_halftime_metrics
from modules.ml_secondhalf_metrics import calculate_secondhalf_metrics
from modules.ml_fulltime_metrics import calculate_fulltime_metrics
from modules.ml_result_win_rates import calculate_result_win_rates

def process_ml_data(df, completed_df=None):
    """
    Process the ML-ready DataFrame by applying feature engineering.
    :param df: DataFrame containing the matches to be processed.
    :param completed_df: DataFrame containing only completed matches (optional).
    :return: Processed ML-ready DataFrame.
    """
    # Eğer tamamlanmış maçlar sağlanmışsa
    if completed_df is not None:
        # Create an ML-ready DataFrame with basic columns
        ml_df = df[["Round", "Home Team ID", "Home Team Name", "Away Team ID", "Away Team Name"]].copy()

        # Halftime metrics hesaplama
        ml_df = calculate_halftime_metrics(ml_df, completed_df)

        # Second half metrics hesaplama
        ml_df = calculate_secondhalf_metrics(ml_df, completed_df)

        # Fulltime metrics hesaplama
        ml_df = calculate_fulltime_metrics(ml_df, completed_df)

        # Result-based win rates hesaplama
        ml_df = calculate_result_win_rates(ml_df, completed_df)

        # Tahmin için hedef sütunları boş bırak
        target_columns = ["Fulltime Result", "Halftime Result", "Secondhalf Result"]
        for col in target_columns:
            ml_df[col] = None
    else:
        # Tamamlanmış maçlar sağlanmadıysa, tüm verileri kullan
        df_filtered = df[df["Status Short"] == "FT"]
        max_round_played = df_filtered["Round"].max()
        df_filtered = df_filtered[df_filtered["Round"] <= max_round_played]

        # Create an ML-ready DataFrame with basic columns
        ml_df = df_filtered[["Round", "Home Team ID", "Home Team Name", "Away Team ID", "Away Team Name"]].copy()

        # Halftime metrics hesaplama
        ml_df = calculate_halftime_metrics(ml_df, df_filtered)

        # Second half metrics hesaplama
        ml_df = calculate_secondhalf_metrics(ml_df, df_filtered)

        # Fulltime metrics hesaplama
        ml_df = calculate_fulltime_metrics(ml_df, df_filtered)

        # Result-based win rates hesaplama
        ml_df = calculate_result_win_rates(ml_df, df_filtered)

        # Hedef sütunları ekleme
        target_columns = ["Fulltime Result", "Halftime Result", "Secondhalf Result"]
        for col in target_columns:
            ml_df[col] = df_filtered[col]

    # Round sütununa göre sıralama
    ml_df = ml_df.sort_values(by="Round").reset_index(drop=True)

    # Ondalık basamakları 2'ye yuvarlama
    ml_df = ml_df.round(2)

    return ml_df
