import os
from datetime import datetime
from modules.api_client import APIClient
from modules.country_league_selector import select_country_and_league
from modules.data_processing import process_all_data
from modules.ml_processing import process_ml_data
from modules.ml_next_match import prepare_next_round_data  # Yeni eklendi
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
            # Send request to 'fixtures' endpoint to get matches for the selected league and season
            fixtures_response = api_client.send_request("fixtures", league=league_id, season=season_year)
            
            if "error" in fixtures_response:
                print("Failed to retrieve fixtures data for the selected league.")
            else:
                fixtures = fixtures_response.get("response", [])
                if not fixtures:
                    print("No finished matches found for the selected league.")
                else:
                    # Process all data
                    df = process_all_data(fixtures, season_year)

                    # Generate league name for file naming
                    league_name = fixtures[0].get("league", {}).get("name", "unknown_league").replace(" ", "_")

                    # Save the processed data to an Excel file
                    save_to_excel(df, file_prefix=f"{league_name}_processed", sheet_name="Processed Data")

                    # Process ML-ready DataFrame
                    ml_df = process_ml_data(df)

                    # Save the ML-ready data to a separate Excel file
                    save_to_excel(ml_df, file_prefix=f"{league_name}_ml_ready", sheet_name="ML Data")

                    # Prepare next round data for predictions
                    next_match_df = prepare_next_round_data(df)

                    # Save the next round data to a separate Excel file
                    save_to_excel(next_match_df, file_prefix=f"{league_name}_next_match", sheet_name="Next Match Data")

    else:
        print("API connection failed.")

# Entry point check
if __name__ == "__main__":
    main()
