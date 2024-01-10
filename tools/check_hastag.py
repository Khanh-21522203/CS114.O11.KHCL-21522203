import os.path
import numpy as np
import pandas as pd
fname = ['data_dsmlvietnam.csv', 'data_mlcoban.csv'] # 647 -
list_hashtag = []
for fn in fname:
    if fn == "data_dsmlvietnam.csv":
        df = pd.read_csv(os.path.join('labeled', fn))
        Hung = []
        Khanh = []
        Cap = []
        col_dsml = df.columns
        for idx, row in df.iterrows():
            if not pd.isna(row["Hùng"]) and not pd.isna(row["Khánh"]) and not pd.isna(row["Cáp"]):
                Hung.append(row["Hùng"])
                Khanh.append(row["Khánh"])
                Cap.append(row["Cáp"])
        print(Hung)
        print("check len: ", len(Hung))
        print("check len: ", len(Khanh))
        print("check len: ", len(Cap))
        # for ls_ht in df["old_hastag"].apply(str):
        #     ls_ht = ls_ht.split('\t')
        #     list_hashtag = ls_ht + list_hashtag

# print(list(set(list_hashtag)))