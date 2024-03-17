import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(df):
    # Print column names to verify the presence of expected columns
    print("Column names:", df.columns)
    
    # Get the numerical columns
    numerical_columns = df.select_dtypes(include=['number']).columns
    
    # Visualize numerical data
    for col in numerical_columns:
        plt.hist(df[col])
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {col}')
        plt.show()

# Assuming 'df' is your DataFrame
df = pd.read_csv("E:\Data Analyst intern\Auto Sales data.csv")  # Replace with your actual file path
visualize_data(df)
