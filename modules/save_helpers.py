# save_helpers.py

import os
from datetime import datetime

def save_to_excel(df, league_name):
    """
    Save the given DataFrame to an Excel file in the 'data' folder.
    :param df: DataFrame to save.
    :param league_name: Name of the league to include in the filename.
    """
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/{league_name}_{timestamp}.xlsx"
    df.to_excel(filename, index=False, engine="openpyxl", sheet_name=league_name)
    print(f"Data has been saved to {filename}")