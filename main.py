# main.py

import os
from datetime import datetime
from modules.api_client import APIClient
from modules.country_league_selector import select_country_and_league
from modules.data_processing import process_all_data
from modules.save_helpers import save_to_excel

# Main function
def main():
    # Create an instance of APIClient and test the connection
    api_client = APIClient()
    
    # Test API connection and get fixtures
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
                    # Process all data
                    df = process_all_data(fixtures, season_year)

                    # Save DataFrame to Excel
                    league_name = fixtures[0].get("league", {}).get("name", "unknown_league").replace(" ", "_")
                    save_to_excel(df, league_name)

    else:
        print("API connection failed.")

# Entry point check
if __name__ == "__main__":
    main()