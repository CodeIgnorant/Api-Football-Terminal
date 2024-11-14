# result.py

def calculate_match_result(df):
    """
    Calculate the match results based on the fulltime, halftime, and second half scores.
    Adds 'Fulltime Result', 'Halftime Result', and 'Secondhalf Result' columns to the DataFrame with values 'home', 'away', or 'draw'.
    
    :param df: DataFrame containing fixture data.
    :return: DataFrame with new 'Fulltime Result', 'Halftime Result', and 'Secondhalf Result' columns.
    """
    # Calculate Match Result
    df['Fulltime Result'] = df.apply(lambda row: 'home' if row['Fulltime Home Score'] > row['Fulltime Away Score'] 
                                             else 'away' if row['Fulltime Away Score'] > row['Fulltime Home Score']
                                             else 'draw', axis=1)
    
    # Calculate Halftime Result
    df['Halftime Result'] = df.apply(lambda row: 'home' if row['Halftime Home Score'] > row['Halftime Away Score'] 
                                               else 'away' if row['Halftime Away Score'] > row['Halftime Home Score']
                                               else 'draw', axis=1)
    
    # Calculate Secondhalf Result
    df['Secondhalf Result'] = df.apply(lambda row: 'home' if row['Secondhalf Home Score'] > row['Secondhalf Away Score'] 
                                                 else 'away' if row['Secondhalf Away Score'] > row['Secondhalf Home Score']
                                                 else 'draw', axis=1)
    
    return df