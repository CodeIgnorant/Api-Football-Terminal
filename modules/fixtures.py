import pandas as pd

def process_fixture_data(fixtures, season_year):
    # Convert JSON data to a list of dictionaries with selected information
    fixtures_data = []
    for fixture in fixtures:
        fixtures_data.append({
            "Fixture ID": fixture.get("fixture", {}).get("id"),
            "Status Short": fixture.get("fixture", {}).get("status", {}).get("short"),
            "Round": fixture.get("league", {}).get("round"),
            "Home Team ID": fixture.get("teams", {}).get("home", {}).get("id"),
            "Home Team Name": fixture.get("teams", {}).get("home", {}).get("name"),
            "Away Team ID": fixture.get("teams", {}).get("away", {}).get("id"),
            "Away Team Name": fixture.get("teams", {}).get("away", {}).get("name"),
            "Halftime Home Score": fixture.get("score", {}).get("halftime", {}).get("home"),
            "Halftime Away Score": fixture.get("score", {}).get("halftime", {}).get("away"),
            "Fulltime Home Score": fixture.get("score", {}).get("fulltime", {}).get("home"),
            "Fulltime Away Score": fixture.get("score", {}).get("fulltime", {}).get("away")
        })
    
    # Once calculations are complete, create a DataFrame
    df = pd.DataFrame(fixtures_data)
    
    # Handle missing values by filling them with 0 (correct way)
    df['Halftime Home Score'] = df['Halftime Home Score'].fillna(0)
    df['Halftime Away Score'] = df['Halftime Away Score'].fillna(0)
    df['Fulltime Home Score'] = df['Fulltime Home Score'].fillna(0)
    df['Fulltime Away Score'] = df['Fulltime Away Score'].fillna(0)

    # Print a message indicating manipulation
    print("Data manipulation: Empty values were filled with '0'.")
    
    return df