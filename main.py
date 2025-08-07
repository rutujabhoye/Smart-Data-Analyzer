import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file):
    return pd.read_csv(file)

def show_basic_info(df):
    print("\nBasic Information:")
    print(df.info())
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nMissing Values:\n", df.isnull().sum())

def analyze_data(df):
    with open("analysis_report.txt", "w") as f:
        f.write("Smart Data Analyzer Report\n")
        f.write("===========================\n\n")
        f.write("Dataset Shape: {}\n\n".format(df.shape))
        f.write("Columns: {}\n\n".format(list(df.columns)))
        f.write("Summary Statistics:\n")
        f.write(str(df.describe()))
        f.write("\n\nMissing Values:\n")
        f.write(str(df.isnull().sum()))

def visualize_data(df):
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in num_cols:
        plt.figure(figsize=(6,4))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.savefig(f'screenshots/{col}_distribution.png')
        plt.close()

def main():
    print("Welcome to Smart Data Analyzer ")
    file = input("Enter CSV filename (e.g., sample_dataset.csv): ")
    try:
        df = load_data(file)
        show_basic_info(df)
        analyze_data(df)
        visualize_data(df)
        print("\n Analysis complete. Check 'analysis_report.txt' and 'screenshots/' folder.")
    except Exception as e:
        print(" Error:", e)

if __name__ == "__main__":
    main()
