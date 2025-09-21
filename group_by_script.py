import pandas as pd
import sys

# Define input and output file names
input_file = sys.argv[1]
output_file = sys.argv[2]

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