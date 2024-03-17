import pandas as pd

def clean_data(df):
    # Print column names to verify the presence of 'date_column'
    print("Column names:", df.columns)
    
    # Check if 'ORDERDATE' exists in the DataFrame
    if 'ORDERDATE' not in df.columns:
        raise KeyError("'ORDERDATE' does not exist in the DataFrame.")

    print(df.isnull().sum())
    
    # Fix the warning by specifying numeric_only=True
    df.fillna(df.mean(numeric_only=True), inplace=True)
    
    # Convert 'ORDERDATE' to datetime format
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
    
    return df
