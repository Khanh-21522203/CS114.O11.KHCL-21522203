import os.path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fname = ['p_mlcoban.csv', 'p_dsmlvietnam.csv']

bar_width = 0.35  # Width of the bars
index = np.arange(len(fname))  # X-axis positions for the bars

fig, ax = plt.subplots()

for i, fn in enumerate(fname):
    df = pd.read_csv(os.path.join('data/process_data', fn))

    # Count null and non-null values
    null_count = df["old_hastag"].isnull().sum()
    non_null_count = len(df["old_hastag"]) - null_count
    total_count = len(df["old_hastag"])

    # Calculate percentages
    null_percentage = (null_count / total_count) * 100
    non_null_percentage = (non_null_count / total_count) * 100

    # Plot grouped bars
    ax.bar(index[i] - bar_width / 2, null_percentage, bar_width, label=f'{fn} - Non-Hashtag', color='red')
    ax.bar(index[i] + bar_width / 2, non_null_percentage, bar_width, label=f'{fn} - Hashtag', color='green')

    # Annotate percentages on top of the bars
    ax.text(index[i] - bar_width / 2, null_percentage + 1, f'{null_percentage:.2f}%', ha='center', va='bottom', color='black')
    ax.text(index[i] + bar_width / 2, non_null_percentage + 1, f'{non_null_percentage:.2f}%', ha='center', va='bottom', color='black')

ax.set_title('Histogram for Hashtag and Non-Hashtag Values')
ax.set_xlabel('File')
ax.set_ylabel('Percentage (%)')
ax.set_xticks(index)
ax.set_xticklabels(fname)
ax.legend()

# Save the combined histogram as a PNG file
save_path = os.path.join('statistic_results', 'combined_histogram_percentage.png')
plt.savefig(save_path)

# Show the combined histogram
plt.show()
