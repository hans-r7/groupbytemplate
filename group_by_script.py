import pandas as pd

# Define input and output file names
input_file = "sample_data.csv"
output_file = "results.csv"

# Read the CSV file
print(f"Reading data from {input_file}...")
df = pd.read_csv(input_file)

# Perform group by operation
print("Performing group by operation...")
result = df.groupby("category")["value"].sum().reset_index()
result.columns = ["category", "total"]

# Save results
result.to_csv(output_file, index=False)
print(f"Results saved to {output_file}")
print("\nSummary:")
print(result)