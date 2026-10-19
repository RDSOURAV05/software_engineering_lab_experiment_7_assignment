import os
import pandas as pd


def load_dataset(filepath: str) -> pd.DataFrame:
    """
    Load a dataset from a CSV file after validating its extension and file existence.

    Parameters:
        filepath (str): Path to the dataset CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.

    Raises:
        ValueError: If the file extension is not strictly .csv (Equivalence Partitioning).
        FileNotFoundError: If the specified file does not exist.
    """
    if not filepath.lower().endswith(".csv"):
        raise ValueError(f"Invalid file extension: '{filepath}'. Only .csv files are supported.")

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset file not found: '{filepath}'")

    return pd.read_csv(filepath)


def split_data(filepath: str, ratio: float = 0.8):
    """
    Split a dataset into train and test sets based on the specified split ratio.

    Parameters:
        filepath (str): Path to the dataset CSV file.
        ratio (float): Fraction of data to assign to the training set (default: 0.8).

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: (train_dataframe, test_dataframe)

    Raises:
        ValueError: If split ratio is >= 1.0 or <= 0.0 (Boundary Value Analysis).
    """
    if ratio <= 0.0 or ratio >= 1.0:
        raise ValueError(f"Invalid split ratio: {ratio}. Ratio must be strictly between 0.0 and 1.0.")

    df = load_dataset(filepath)
    split_idx = int(len(df) * ratio)
    train_df = df.iloc[:split_idx]
    test_df = df.iloc[split_idx:]
    return train_df, test_df
