import pytest
from dataset_manager import load_dataset, split_data


# Test 1: Load valid dataset
def test_valid_dataset():
    df = load_dataset("data.csv")
    assert not df.empty


# Test 2: Missing file exception
def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_dataset("missing.csv")


# Test 3: Valid train/test split
def test_valid_split():
    train, test = split_data("data.csv", ratio=0.8)
    assert len(train) > len(test)


# Test 4: Split ratio exactly 1.0 (Boundary Value Analysis)
def test_boundary_split_ratio():
    with pytest.raises(ValueError):
        split_data("data.csv", ratio=1.0)


# Test 5: Invalid file extension (Equivalence Partitioning)
def test_invalid_extension():
    with pytest.raises(ValueError):
        load_dataset("data.txt")
