import os.path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
fname = ['test_data.csv', 'train_data.csv']
list_hashtag = ["#sharing", "#machine_learning", "#deep_learning", "#python", "#data", "#cv", "#nlp", "#math", "#Q&A"]
hashtag_dict = {hashtag: 0 for hashtag in list_hashtag}
hashtag_dict_all = {hashtag: 0 for hashtag in list_hashtag}
hashtag_dict = {hashtag: 0 for hashtag in list_hashtag}
hashtag_dict_all = {hashtag: 0 for hashtag in list_hashtag}
sentence_lengths = []
for fn in fname:
    hashtag_dict = {hashtag: 0 for hashtag in list_hashtag}
    df = pd.read_csv(os.path.join('data', fn))
    print(f'{fn} have {len(df["text"])} samples')
    for row in df["label"]:
        for i in row[1:-1].strip().split(","):
            i = i.strip()[1:-1]
            hashtag_dict[i] += 1
            hashtag_dict_all[i] += 1

    hashtags = list(hashtag_dict.keys())
    values = list(hashtag_dict.values())

    #Plotting the histogram
    plt.bar(hashtags, values, color='blue')
    plt.xlabel('Hashtags')
    plt.ylabel('Values')
    plt.title(f'Hashtag distribution in {fn.split("_")[0]} file')
    plt.xticks(rotation=45, ha='right')  # Rotating x-axis labels for better readability
    plt.tight_layout()
    # for sentence in df['text']:
#         sentence_lengths.append(len(sentence.split()))
#
# plt.hist(sentence_lengths, bins=50, color='blue', edgecolor='black')
# plt.title('Distribution of Sentence Lengths')
# plt.xlabel('Length of Sentences')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.savefig(f"statistic_results/distribution_length_data.png")
    plt.savefig(f"statistic_results/hashtag_counts_{fn.split('_')[0]}.png")
#
hashtags_all = list(hashtag_dict_all.keys())
values_all = list(hashtag_dict_all.values())
plt.bar(hashtags_all, values_all, color='blue')
plt.xlabel('Hashtags')
plt.ylabel('Values')
plt.title(f'Hashtag distribution in data file')
plt.xticks(rotation=45, ha='right')  # Rotating x-axis labels for better readability
plt.tight_layout()
plt.savefig(f"statistic_results/hashtag_counts_all.png")

