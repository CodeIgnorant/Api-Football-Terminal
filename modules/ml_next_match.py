import pandas as pd
from modules.ml_processing import process_ml_data

def prepare_next_round_data(df):
    """
    Prepare data for the next round using completed matches for feature calculations.
    """
    # Tamamlanmış maçları filtrele
    df_completed = df[df["Status Short"] == "FT"]
    
    # Sıradaki round'u belirle
    max_completed_round = df_completed["Round"].max()
    next_round = max_completed_round + 1
    
    # Sıradaki round'a ait maçları seç
    df_next_round = df[df["Round"] == next_round].copy()
    
    # Eğer sıradaki round'da maç yoksa
    if df_next_round.empty:
        print(f"No matches found for next round: {next_round}")
        return None
    
    # Tamamlanmış maçlardan özellik hesaplamaları yap
    df_next_round = process_ml_data(df_next_round, df_completed)
    
    # Hedef sütunları boş bırak
    target_columns = ["Fulltime Result", "Halftime Result", "Secondhalf Result"]
    for col in target_columns:
        df_next_round[col] = None  # Tahmin için hedef değerler boş
    
    return df_next_round
