import pandas as pd
from visualization import visualize_data  # Import the visualization function

# Load the dataset into a DataFrame
df = pd.read_csv("E:\Data Analyst intern\Auto Sales data.csv")  # Replace 'your_dataset.csv' with your actual file path

# Call the visualize_data function with the loaded DataFrame
visualize_data(df)
