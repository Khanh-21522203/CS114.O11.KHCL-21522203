import os.path
import numpy as np
import pandas as pd
fname = ['data_dsmlvietnam.csv', 'data_mlcoban.csv'] # 647 -
list_hashtag = ["#sharing", "#machine_learning", "#deep_learning", "#python", "#data", "#cv", "#nlp", "#math", "#Q&A", "#webinar"]
Hung = []
Khanh = []
Cap = []
for fn in fname:
    df = pd.read_csv(os.path.join('labeled', fn))
    for idx, row in df.iterrows():
        if not pd.isna(row["Hùng"]) and not pd.isna(row["Khánh"]) and not pd.isna(row["Cáp"]):
            it_Hung = []
            it_Khanh = []
            it_Cap = []
            for i in row["Hùng"].split(','):
                if i == "#pythonlibraries":
                    i = "#python"
                if i in list_hashtag:
                    it_Hung.append(i)
            Hung.append(it_Hung)
            for i in row["Khánh"].split(','):
                if i == "#pythonlibraries":
                    i = "#python"
                if i in list_hashtag:
                    it_Khanh.append(i)
            Khanh.append(it_Khanh)
            for i in row["Cáp"].split(','):
                if i == "#pythonlibraries":
                    i = "#python"
                if i in list_hashtag:
                    it_Cap.append(i)
            Cap.append(it_Cap)
