def calculate_secondhalf_metrics(ml_df, df):
    """
    Calculate second half metrics for both home and away teams, including:
    - Second Half Average Goals - Home
    - Second Half Scoring Rate - Home
    - Second Half Cumulative Goals - Home
    - Second Half Average Goals - Away
    - Second Half Scoring Rate - Away
    - Second Half Cumulative Goals - Away

    :param ml_df: The ML-ready DataFrame containing basic columns.
    :param df: The processed DataFrame with all original match data.
    :return: Updated ml_df with second half metrics for home and away teams.
    """
    # Önce round sırasına göre veriyi sıralayın
    df = df.sort_values(by="Round")
    
    # Second Half Cumulative Goals - Home
    ml_df["Second Half Cumulative Goals - Home"] = ml_df.apply(
        lambda row: df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Secondhalf Home Score"].sum(), axis=1
    )
    
    # Second Half Average Goals - Home
    ml_df["Second Half Average Goals - Home"] = ml_df.apply(
        lambda row: df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Secondhalf Home Score"].mean() if not df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Secondhalf Home Score"].empty else 0, axis=1
    )
    
    # Second Half Scoring Rate - Home
    ml_df["Second Half Scoring Rate - Home"] = ml_df.apply(
        lambda row: df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Secondhalf Home Score"].apply(lambda x: 1 if x > 0 else 0).mean() if not df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Secondhalf Home Score"].empty else 0, axis=1
    )
    
    # Second Half Cumulative Goals - Away
    ml_df["Second Half Cumulative Goals - Away"] = ml_df.apply(
        lambda row: df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Secondhalf Away Score"].sum(), axis=1
    )
    
    # Second Half Average Goals - Away
    ml_df["Second Half Average Goals - Away"] = ml_df.apply(
        lambda row: df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Secondhalf Away Score"].mean() if not df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Secondhalf Away Score"].empty else 0, axis=1
    )
    
    # Second Half Scoring Rate - Away
    ml_df["Second Half Scoring Rate - Away"] = ml_df.apply(
        lambda row: df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Secondhalf Away Score"].apply(lambda x: 1 if x > 0 else 0).mean() if not df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Secondhalf Away Score"].empty else 0, axis=1
    )
    
    return ml_df