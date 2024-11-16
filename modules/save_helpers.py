import os
from datetime import datetime

def save_to_excel(df, file_prefix, sheet_name="Sheet1"):
    """
    Save the given DataFrame to an Excel file in the 'data' folder.
    :param df: DataFrame to save.
    :param file_prefix: Prefix for the filename (e.g., league name or purpose).
    :param sheet_name: Name of the Excel sheet (default is 'Sheet1').
    """
    # Create 'data' folder if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Generate a unique timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/{file_prefix}_{timestamp}.xlsx"
    
    # Save the DataFrame to Excel
    df.to_excel(filename, index=False, engine="openpyxl", sheet_name=sheet_name)
    print(f"Data has been saved to {filename}")