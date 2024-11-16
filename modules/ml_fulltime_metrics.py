def calculate_fulltime_metrics(ml_df, df):
    """
    Calculate fulltime metrics for both home and away teams, including:
    - Fulltime Average Goals - Home
    - Fulltime Scoring Rate - Home
    - Fulltime Cumulative Goals - Home
    - Fulltime Average Goals - Away
    - Fulltime Scoring Rate - Away
    - Fulltime Cumulative Goals - Away

    :param ml_df: The ML-ready DataFrame containing basic columns.
    :param df: The processed DataFrame with all original match data.
    :return: Updated ml_df with fulltime metrics for home and away teams.
    """
    # Önce round sırasına göre veriyi sıralayın
    df = df.sort_values(by="Round")
    
    # Fulltime Cumulative Goals - Home
    ml_df["Fulltime Cumulative Goals - Home"] = ml_df.apply(
        lambda row: df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Fulltime Home Score"].sum(), axis=1
    )
    
    # Fulltime Average Goals - Home
    ml_df["Fulltime Average Goals - Home"] = ml_df.apply(
        lambda row: df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Fulltime Home Score"].mean() if not df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Fulltime Home Score"].empty else 0, axis=1
    )
    
    # Fulltime Scoring Rate - Home
    ml_df["Fulltime Scoring Rate - Home"] = ml_df.apply(
        lambda row: df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Fulltime Home Score"].apply(lambda x: 1 if x > 0 else 0).mean() if not df[
            (df["Home Team ID"] == row["Home Team ID"]) & (df["Round"] < row["Round"])
        ]["Fulltime Home Score"].empty else 0, axis=1
    )
    
    # Fulltime Cumulative Goals - Away
    ml_df["Fulltime Cumulative Goals - Away"] = ml_df.apply(
        lambda row: df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Fulltime Away Score"].sum(), axis=1
    )
    
    # Fulltime Average Goals - Away
    ml_df["Fulltime Average Goals - Away"] = ml_df.apply(
        lambda row: df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Fulltime Away Score"].mean() if not df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Fulltime Away Score"].empty else 0, axis=1
    )
    
    # Fulltime Scoring Rate - Away
    ml_df["Fulltime Scoring Rate - Away"] = ml_df.apply(
        lambda row: df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Fulltime Away Score"].apply(lambda x: 1 if x > 0 else 0).mean() if not df[
            (df["Away Team ID"] == row["Away Team ID"]) & (df["Round"] < row["Round"])
        ]["Fulltime Away Score"].empty else 0, axis=1
    )
    
    return ml_df