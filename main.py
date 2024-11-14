# main.py

import os
from datetime import datetime
from modules.api_client import APIClient
from modules.country_league_selector import select_country_and_league
from modules.fixtures import process_fixture_data
from modules.secondhalf_score import calculate_secondhalf_scores
from modules.result import calculate_match_result
from modules.total_goals import calculate_total_goals
from modules.over_under import calculate_over_under
from modules.goal_range import calculate_goal_range
from modules.both_team_score import calculate_both_team_score

# Main function
def main():
    # Create an instance of APIClient and test the connection
    api_client = APIClient()
    
    # Test API connection
    if api_client.test_connection():
        print("API connection successful!")
        
        # Use the function to select a country and then a league
        league_id, season_year = select_country_and_league(api_client)
        
        if league_id and season_year:
            # Send request to 'fixtures' endpoint to get finished matches for the selected league and season
            fixtures_response = api_client.send_request("fixtures", league=league_id, season=season_year, status="FT")
            if "error" in fixtures_response:
                print("Failed to retrieve fixtures data for the selected league.")
            else:
                fixtures = fixtures_response.get("response", [])
                if not fixtures:
                    print("No finished matches found for the selected league.")
                else:
                    # Process fixtures data in a separate function and get the DataFrame
                    df = process_fixture_data(fixtures, season_year)
                    
                    # Calculate second half scores using another function
                    df = calculate_secondhalf_scores(df)
                    
                    # Calculate match result using another function
                    df = calculate_match_result(df)
                    
                    # Calculate total goals using another function
                    df = calculate_total_goals(df)
                    
                    # Calculate over/under metrics using another function
                    df = calculate_over_under(df)
                    
                    # Calculate goal range using another function
                    df = calculate_goal_range(df)
                    
                    # Calculate both team score using another function
                    df = calculate_both_team_score(df)
                    
                    # Save DataFrame to Excel file in the 'data' folder with league name in the filename
                    os.makedirs("data", exist_ok=True)
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    league_name = fixtures[0].get("league", {}).get("name", "unknown_league").replace(" ", "_")
                    filename = f"data/{league_name}_{timestamp}.xlsx"
                    df.to_excel(filename, index=False, engine="openpyxl", sheet_name=league_name)
                    print(f"Data has been saved to {filename}")
    else:
        print("API connection failed.")

# Entry point check
if __name__ == "__main__":
    main()