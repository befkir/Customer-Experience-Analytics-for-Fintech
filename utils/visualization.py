import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_rating_comparison(rating_df, output_filename='rating_comparison.png'):
    """
    Plots and saves a bar chart comparing ratings across multiple banks.

    Args:
        rating_df (pd.DataFrame): A DataFrame where index is rating (e.g., 1-5)
                                  and columns are bank names with count values.
        output_filename (str): The name of the output PNG file (saved in root/output/).
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output'))
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)

    # Plot setup
    plt.figure(figsize=(10, 6))
    bar_width = 0.25
    x = list(range(len(rating_df.index)))
    banks = rating_df.columns
    colors = ['red', 'yellow', 'blue']  # Adjust or expand if needed

    for i, bank in enumerate(banks):
        plt.bar([pos + bar_width * i for pos in x], rating_df[bank], width=bar_width,
                label=bank, color=colors[i % len(colors)])

    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.title('Rating Count per Bank')
    plt.xticks([pos + bar_width for pos in x], rating_df.index)
    plt.legend()
    plt.tight_layout()

    # Save and show
    plt.savefig(output_path, dpi=300)
    plt.show()

    print(f"Saved rating comparison chart to {output_path}")

def plot_all_rating(df: pd.DataFrame, output_path: str = "../output/rating_comparison.png") -> None:
    """
    Plots rating distribution comparison across apps using a hue column 'source'.

    Args:
        df (pd.DataFrame): Combined DataFrame with 'rating' and 'source' columns.
        output_path (str): Path to save the PNG plot. Defaults to '../output/rating_comparison.png'.
    """
    if 'rating' not in df.columns or 'source' not in df.columns:
        raise ValueError("DataFrame must contain 'rating' and 'source' columns.")

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='rating', hue='source')

    plt.title('Rating Distribution Comparison Across Apps')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.legend(title='App')
    plt.tight_layout()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.show()