import pandas as pd

def process_fixture_data(fixtures, season_year):
    # Convert JSON data to a list of dictionaries with selected information
    fixtures_data = []
    for fixture in fixtures:
        # Extract relevant data and process "Round" to keep only numerical values
        round_raw = fixture.get("league", {}).get("round", "")
        round_numeric = int(round_raw.split("-")[-1].strip()) if "-" in round_raw else None
        
        fixtures_data.append({
            "Round": round_numeric,  # Only the numeric value of "Round"
            "Status Short": fixture.get("fixture", {}).get("status", {}).get("short"),
            "Home Team ID": fixture.get("teams", {}).get("home", {}).get("id"),
            "Home Team Name": fixture.get("teams", {}).get("home", {}).get("name"),
            "Away Team ID": fixture.get("teams", {}).get("away", {}).get("id"),
            "Away Team Name": fixture.get("teams", {}).get("away", {}).get("name"),
            "Halftime Home Score": fixture.get("score", {}).get("halftime", {}).get("home"),
            "Halftime Away Score": fixture.get("score", {}).get("halftime", {}).get("away"),
            "Fulltime Home Score": fixture.get("score", {}).get("fulltime", {}).get("home"),
            "Fulltime Away Score": fixture.get("score", {}).get("fulltime", {}).get("away")
        })
    
    # Create a DataFrame
    df = pd.DataFrame(fixtures_data)
    
    # Check if there are any missing values
    missing_values_exist = df[['Halftime Home Score', 'Halftime Away Score', 'Fulltime Home Score', 'Fulltime Away Score']].isnull().any().any()
    
    # Handle missing values by filling them with 0 (correct way)
    if missing_values_exist:
        df['Halftime Home Score'] = df['Halftime Home Score'].fillna(0)
        df['Halftime Away Score'] = df['Halftime Away Score'].fillna(0)
        df['Fulltime Home Score'] = df['Fulltime Home Score'].fillna(0)
        df['Fulltime Away Score'] = df['Fulltime Away Score'].fillna(0)
        # Print a message indicating manipulation
        print("Data manipulation: Empty values were filled with '0'.")
    
    return df