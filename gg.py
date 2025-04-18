import pandas as pd

def load_dataset(file_path):
    """
    Load a dataset from a CSV file.
    :param file_path: Path to the CSV file.
    :return: Pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def explore_dataset(data):
    """
    Perform basic exploration of the dataset.
    :param data: Pandas DataFrame.
    """
    print("\nDataset Info:")
    print(data.info())

    print("\nFirst 5 Rows:")
    print(data.head())

    print("\nStatistics:")
    print(data.describe())

    print("\nMissing Values:")
    print(data.isnull().sum())

def clean_dataset(data):
    """
    Clean the dataset by handling missing values.
    :param data: Pandas DataFrame.
    :return: Cleaned DataFrame.
    """
    print("\nCleaning dataset...")
    # Drop rows with missing values
    cleaned_data = data.dropna()
    print(f"Rows after dropping missing values: {len(cleaned_data)}")
    return cleaned_data

def analyze_dataset(data):
    """
    Perform analysis on the dataset.
    :param data: Pandas DataFrame.
    """
    print("\nAnalyzing dataset...")
    # Example 1: Count unique values in a column
    if 'Category' in data.columns:
        print("\nUnique values in 'Category' column:")
        print(data['Category'].value_counts())

    # Example 2: Calculate mean of a numerical column
    if 'Value' in data.columns:
        print(f"\nMean of 'Value' column: {data['Value'].mean()}")

    # Example 3: Correlation matrix
    print("\nCorrelation Matrix:")
    print(data.corr())

def main():
    # File path to the dataset
    file_path = "sample_dataset.csv"

    # Load the dataset
    data = load_dataset(file_path)
    if data is None:
        return

    # Explore the dataset
    explore_dataset(data)

    # Clean the dataset
    cleaned_data = clean_dataset(data)

    # Analyze the dataset
    analyze_dataset(cleaned_data)

if __name__ == "__main__":
    main()