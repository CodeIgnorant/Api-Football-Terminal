def calculate_halftime_metrics(ml_df, df):
    """
    Calculate halftime metrics for both home and away teams, including:
    - Halftime Average Goals - Home
    - Halftime Scoring Rate - Home
    - Halftime Cumulative Goals - Home
    - Halftime Average Goals - Away
    - Halftime Scoring Rate - Away
    - Halftime Cumulative Goals - Away

    :param ml_df: The ML-ready DataFrame containing basic columns.
    :param df: The processed DataFrame with all original match data.
    :return: Updated ml_df with halftime metrics for home and away teams.
    """
    # Önce round sırasına göre veriyi sıralayın
    df = df.sort_values(by="Round")
    
    # Halftime Cumulative Goals - Home
    ml_df["Halftime Cumulative Goals - Home"] = ml_df.apply(
        lambda row: df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Halftime Home Score"].sum(), axis=1
    )
    
    # Halftime Average Goals - Home
    ml_df["Halftime Average Goals - Home"] = ml_df.apply(
        lambda row: df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Halftime Home Score"].mean() if not df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Halftime Home Score"].empty else 0, axis=1
    )
    
    # Halftime Scoring Rate - Home
    ml_df["Halftime Scoring Rate - Home"] = ml_df.apply(
        lambda row: df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Halftime Home Score"].apply(lambda x: 1 if x > 0 else 0).mean() if not df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Halftime Home Score"].empty else 0, axis=1
    )
    
    # Halftime Cumulative Goals - Away
    ml_df["Halftime Cumulative Goals - Away"] = ml_df.apply(
        lambda row: df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Halftime Away Score"].sum(), axis=1
    )
    
    # Halftime Average Goals - Away
    ml_df["Halftime Average Goals - Away"] = ml_df.apply(
        lambda row: df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Halftime Away Score"].mean() if not df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Halftime Away Score"].empty else 0, axis=1
    )
    
    # Halftime Scoring Rate - Away
    ml_df["Halftime Scoring Rate - Away"] = ml_df.apply(
        lambda row: df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Halftime Away Score"].apply(lambda x: 1 if x > 0 else 0).mean() if not df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Halftime Away Score"].empty else 0, axis=1
    )
    
    return ml_df