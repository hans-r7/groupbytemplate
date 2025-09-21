import subprocess

# Run the student's script, capture stdout
proc = subprocess.run(
    ["python", "group_by_script.py", "tests/input.csv"], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    encoding="utf-8",
    check=True
)

stdout = proc.stdout

# Expected summary as a string
expected_summary = """Summary:
 category  total
    Books     75
 Clothing    135
Electronics 505"""

# Normalize whitespace for robustness (optional)
stdout_clean = "\n".join(line.strip() for line in stdout.strip().split("\n"))
expected_clean = "\n".join(line.strip() for line in expected_summary.strip().split("\n"))

if expected_clean in stdout_clean:
    print("Test passed!")
    exit(0)
else:
    print("Test failed! Student's summary was:")
    print(stdout)
    exit(1)
