def calculate_result_win_rates(ml_df, df):
    """
    Calculate win, draw, and lose rates for Fulltime, Halftime, and Secondhalf results.
    Adds the following columns to ml_df:
    - Fulltime Result Home Win - Home
    - Fulltime Result Away Win - Home
    - Fulltime Result Draw - Home
    - Fulltime Result Home Win - Away
    - Fulltime Result Away Win - Away
    - Fulltime Result Draw - Away
    - (Similarly for Halftime and Secondhalf results)

    :param ml_df: The ML-ready DataFrame containing basic columns.
    :param df: The processed DataFrame with all original match data.
    :return: Updated ml_df with result win, draw, and lose rates.
    """
    # Round sırasına göre sıralama
    df = df.sort_values(by="Round")
    
    def calculate_rate(row, team_id_column, is_home, result_value, result_column):
        """Helper function to calculate the rate of a specific result (1, 0, or 2)."""
        team_id = row[team_id_column]
        if is_home:
            matches = df[(df["Home Team ID"] == team_id) & (df["Round"] < row["Round"])]
        else:
            matches = df[(df["Away Team ID"] == team_id) & (df["Round"] < row["Round"])]
        
        total_matches = matches.shape[0]
        if total_matches == 0:
            return 0
        return matches[matches[result_column] == result_value].shape[0] / total_matches
    
    # Fulltime Result oranları
    ml_df["Fulltime Result Home Win - Home"] = ml_df.apply(
        lambda row: calculate_rate(row, "Home Team ID", True, 1, "Fulltime Result"), axis=1
    )
    ml_df["Fulltime Result Away Win - Home"] = ml_df.apply(
        lambda row: calculate_rate(row, "Home Team ID", True, 2, "Fulltime Result"), axis=1
    )
    ml_df["Fulltime Result Draw - Home"] = ml_df.apply(
        lambda row: calculate_rate(row, "Home Team ID", True, 0, "Fulltime Result"), axis=1
    )
    ml_df["Fulltime Result Home Win - Away"] = ml_df.apply(
        lambda row: calculate_rate(row, "Away Team ID", False, 1, "Fulltime Result"), axis=1
    )
    ml_df["Fulltime Result Away Win - Away"] = ml_df.apply(
        lambda row: calculate_rate(row, "Away Team ID", False, 2, "Fulltime Result"), axis=1
    )
    ml_df["Fulltime Result Draw - Away"] = ml_df.apply(
        lambda row: calculate_rate(row, "Away Team ID", False, 0, "Fulltime Result"), axis=1
    )
    
    # Halftime Result oranları
    ml_df["Halftime Result Home Win - Home"] = ml_df.apply(
        lambda row: calculate_rate(row, "Home Team ID", True, 1, "Halftime Result"), axis=1
    )
    ml_df["Halftime Result Away Win - Home"] = ml_df.apply(
        lambda row: calculate_rate(row, "Home Team ID", True, 2, "Halftime Result"), axis=1
    )
    ml_df["Halftime Result Draw - Home"] = ml_df.apply(
        lambda row: calculate_rate(row, "Home Team ID", True, 0, "Halftime Result"), axis=1
    )
    ml_df["Halftime Result Home Win - Away"] = ml_df.apply(
        lambda row: calculate_rate(row, "Away Team ID", False, 1, "Halftime Result"), axis=1
    )
    ml_df["Halftime Result Away Win - Away"] = ml_df.apply(
        lambda row: calculate_rate(row, "Away Team ID", False, 2, "Halftime Result"), axis=1
    )
    ml_df["Halftime Result Draw - Away"] = ml_df.apply(
        lambda row: calculate_rate(row, "Away Team ID", False, 0, "Halftime Result"), axis=1
    )
    
    # Secondhalf Result oranları
    ml_df["Secondhalf Result Home Win - Home"] = ml_df.apply(
        lambda row: calculate_rate(row, "Home Team ID", True, 1, "Secondhalf Result"), axis=1
    )
    ml_df["Secondhalf Result Away Win - Home"] = ml_df.apply(
        lambda row: calculate_rate(row, "Home Team ID", True, 2, "Secondhalf Result"), axis=1
    )
    ml_df["Secondhalf Result Draw - Home"] = ml_df.apply(
        lambda row: calculate_rate(row, "Home Team ID", True, 0, "Secondhalf Result"), axis=1
    )
    ml_df["Secondhalf Result Home Win - Away"] = ml_df.apply(
        lambda row: calculate_rate(row, "Away Team ID", False, 1, "Secondhalf Result"), axis=1
    )
    ml_df["Secondhalf Result Away Win - Away"] = ml_df.apply(
        lambda row: calculate_rate(row, "Away Team ID", False, 2, "Secondhalf Result"), axis=1
    )
    ml_df["Secondhalf Result Draw - Away"] = ml_df.apply(
        lambda row: calculate_rate(row, "Away Team ID", False, 0, "Secondhalf Result"), axis=1
    )
    
    return ml_df