import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    elif file_path.endswith(".json"):
        return pd.read_json(file_path)
    else:
        raise ValueError(
            "Unsupported File Format!\n"
            "I can only organize CSV, Excel, or JSON files."
        )


def show_summary(df):
    print("\n--- Data Summary ---")
    print(df.describe(include="all"))


def check_missing(df):
    print("\n--- Missing Values ---")
    print(df.isnull().sum())


def correlation_heatmap(df):
    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.empty:
        print("\nNo numeric columns available for correlation heatmap.")
        return

    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def main():
    file_path = input("Enter the name (or path) of your file: ").strip()

    try:
        df = load_data(file_path)
        show_summary(df)
        check_missing(df)
        correlation_heatmap(df)
    except FileNotFoundError:
        print("File not found. Please check the file name/path.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
