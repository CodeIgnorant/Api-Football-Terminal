# modules/country_league_selector.py

def select_country_and_league(api_client):
    # Send request to 'countries' endpoint
    response = api_client.send_request("countries")
    if "error" in response:
        print("Failed to retrieve countries data.")
        return None, None
    else:
        # Print the names of the countries with numbers
        countries = response.get("response", [])
        for index, country in enumerate(countries, start=1):
            name = country.get("name")
            print(f"{index}. {name}")
        
        # Get user's choice
        try:
            choice = int(input("Please enter the number of the country you want to select: "))
            if 1 <= choice <= len(countries):
                selected_country = countries[choice - 1]
                country_name = selected_country['name']
                print(f"You selected: {country_name}")
                
                # Send request to 'leagues' endpoint to get current season leagues
                leagues_response = api_client.send_request("leagues", country=country_name, current="true")
                if "error" in leagues_response:
                    print("Failed to retrieve leagues data for the selected country.")
                    return None, None
                else:
                    leagues = leagues_response.get("response", [])
                    if not leagues:
                        print("No active leagues found for the selected country.")
                        return None, None
                    else:
                        # Sort leagues by ID and print them
                        leagues_sorted = sorted(leagues, key=lambda x: x.get("league", {}).get("id"))
                        print("Current active leagues:")
                        for index, league in enumerate(leagues_sorted, start=1):
                            league_name = league.get("league", {}).get("name")
                            if league_name:
                                print(f"{index}. {league_name}")
                        
                        # Get user's choice for a league
                        try:
                            league_choice = int(input("Please enter the number of the league you want to select: "))
                            if 1 <= league_choice <= len(leagues_sorted):
                                selected_league = leagues_sorted[league_choice - 1]
                                league_id = selected_league.get("league", {}).get("id")
                                # Get the current season year
                                seasons = selected_league.get("seasons", [])
                                current_season = next((season for season in seasons if season.get("current")), None)
                                season_year = current_season.get("year") if current_season else None
                                print(f"You selected: {selected_league.get('league', {}).get('name')} with ID: {league_id} for Season: {season_year}")
                                return league_id, season_year  # Return the selected league's ID and season year
                            else:
                                print("Invalid choice. Please run the program again and select a valid league number.")
                                return None, None
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                            return None, None
            else:
                print("Invalid choice. Please run the program again and select a valid number.")
                return None, None
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None, None
