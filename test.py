# import statements
import pandas as pd

# file paths
file_path = "data/salaries.csv"

df = pd.read_csv(file_path)

print(df[df['Age'] > 30])
