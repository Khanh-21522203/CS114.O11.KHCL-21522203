import os.path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
fname = ['data_dsmlvietnam.csv', 'data_mlcoban.csv'] # 50 - 48
list_hashtag = ["#sharing", "#machine_learning", "#deep_learning", "#python", "#data", "#cv", "#nlp", "#math", "#Q&A", "#webinar"]
hashtag_dict = {hashtag: 0 for hashtag in list_hashtag}
contents = []
hashtags = []
for fn in fname:
    df = pd.read_csv(os.path.join('labeled', fn))
    for idx, row in df.iterrows():
        if not pd.isna(row["Hùng"]) or not pd.isna(row["Khánh"]) or not pd.isna(row["Cáp"]):
            if (idx >= 50 and fn == "data_dsmlvietnam.csv") or (idx >= 48 and fn == "data_mlcoban.csv"):
                if not pd.isna(row["Hùng"]):
                    it_Hung = []
                    for i in row["Hùng"].strip().split(","):
                        i = i.strip()
                        if i == "#machine_learing":
                            i = "#machine_learning"
                        elif i == "deep_learning":
                            i = "#deep_learning"
                        elif i == "#Q7A":
                            i = "#Q&A"
                        elif i == "#shairng":
                            i = "#sharing"
                        elif i == "#deep_learining":
                            i = "#deep_learning"
                        if i in list_hashtag:
                            hashtag_dict[i] +=1
                            it_Hung.append(i)
                    if it_Hung:
                        contents.append(row["Contents"])
                        hashtags.append(it_Hung)

                elif not pd.isna(row["Khánh"]):
                    it_Khanh = []
                    for i in row["Khánh"].strip().split(","):
                        i = i.strip()
                        if i == "#machine_learing":
                            i = "#machine_learning"
                        elif i == "deep_learning":
                            i = "#deep_learning"
                        elif i == "#Q7A":
                            i = "#Q&A"
                        elif i == "#shairng":
                            i = "#sharing"
                        elif i == "#deep_learining":
                            i = "#deep_learning"
                        if i in list_hashtag:
                            hashtag_dict[i] += 1
                            it_Khanh.append(i)
                    if it_Khanh:
                        contents.append(row["Contents"])
                        hashtags.append(it_Khanh)

                elif not pd.isna(row["Cáp"]):
                    it_Cap = []
                    for i in row["Cáp"].strip().split(","):
                        i = i.strip()
                        if i == "#machine_learing":
                            i = "#machine_learning"
                        elif i == "deep_learning":
                            i = "#deep_learning"
                        elif i == "#Q7A":
                            i = "#Q&A"
                        elif i == "#shairng":
                            i = "#sharing"
                        elif i == "#deep_learining":
                            i = "#deep_learning"
                        if i in list_hashtag:
                            hashtag_dict[i] += 1
                            it_Cap.append(i)
                    if it_Cap:
                        contents.append(row["Contents"])
                        hashtags.append(it_Cap)
data = {
    'Contents': contents,
    "Hashtags": hashtags
}
data = pd.DataFrame(data)
data.to_csv("data.csv")

# Extracting hashtags and values from the dictionary
hashtags = list(hashtag_dict.keys())
values = list(hashtag_dict.values())

# Plotting the histogram
plt.bar(hashtags, values, color='blue')
plt.xlabel('Hashtags')
plt.ylabel('Values')
plt.title('Hashtag Counts')
plt.xticks(rotation=45, ha='right')  # Rotating x-axis labels for better readability
plt.tight_layout()
plt.savefig("statistic_results/hashtag_counts.png")