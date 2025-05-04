import pandas as pd

def load_data(filepath):
    """
    Loads a CSV file and returns a pandas DataFrame.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        df = pd.read_csv(filepath)
        if 'sex' in df.columns:
            df = df[df['sex'] == 'male']
        else:
            print("Warning: 'sex' column not found. Returning full dataset.")
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File {filepath} is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def clean_data(df):
# Drop rows with missing values
    df_cleaned = df.dropna()

    # Convert all categorical columns (object dtype) to lowercase
    for col in df_cleaned.select_dtypes(include='object').columns:
        df_cleaned[col] = df_cleaned[col].str.lower()

    return df_cleaned
