import subprocess
import pandas as pd

# Run the student's script
subprocess.run(["python", "group_by_script.py", "tests/input.csv", "tests/output.csv"], check=True)

# Read the output and expected output
output = pd.read_csv("tests/results.csv")
expected = pd.read_csv("tests/expected_output.csv")

# Check if the outputs are the same
if output.equals(expected):
    print("Test passed!")
    exit(0)
else:
    print("Test failed!")
    exit(1)
