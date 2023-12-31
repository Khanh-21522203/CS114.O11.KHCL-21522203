import pandas as pd
import csv
import re
import regex

def remove_emojis(data):
  emoj = re.compile(r"""[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002702-\U000027B0\U000024C2-\U0001F251\U0001f926-\U0001f937\U00010000-\U0010ffff\u200d\u23cf\u23e9\u231a\ufe0f\u3030]+(?<!\n)""", re.UNICODE)
  return re.sub(emoj, '', data)


def extract_hashtags(text):
    hashtag_list = []

    words = text.split()

    for word in words:
        if re.match(r'#[\w_]+', word, flags=re.IGNORECASE):
            hashtag = word
            hashtag_list.append(hashtag)

    text = " ".join([w for w in words if not re.match(r'#[\w_]+', w, flags=re.IGNORECASE)])

    return hashtag_list, text

df = pd.read_csv("data/mlopvn.csv", sep='\t', index_col=0)
df = df.drop(axis=1, columns=["Links"])
df["p_content"] = None
df['old_hastag'] = None
df['Hashtag'] = None
for idx, content in enumerate(df["Contents"].apply(str)):
    content = remove_emojis(content)
    hashtags, content = extract_hashtags(content)
    df["p_content"][idx] = content
    df['old_hastag'][idx] = "\t".join(hashtags)

df.to_csv("process_data/p_mlopvn.csv", encoding='utf-8-sig', index=False)
