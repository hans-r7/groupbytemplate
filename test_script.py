import pandas as pd
import os

def test_groupby_operation():
    # Check if results.csv exists
    assert os.path.exists("results.csv"), "results.csv does not exist"
    
    # Read results
    result = pd.read_csv("results.csv")
    
    # Read expected output
    expected = pd.read_csv("expected_output.csv")
    
    # Check if the dataframes match
    pd.testing.assert_frame_equal(result, expected, check_dtype=False)
    
    # Check if the column names match
    assert list(result.columns) == ["category", "total"], "Column names do not match"

if __name__ == "__main__":
    test_groupby_operation()
    print("All tests passed!")