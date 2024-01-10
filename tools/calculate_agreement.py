import os.path
import numpy as np
import pandas as pd
from sklearn.metrics import cohen_kappa_score
from nltk.metrics.agreement import AnnotationTask
from nltk.metrics import masi_distance
fname = ['data_dsmlvietnam.csv', 'data_mlcoban.csv']
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
                i = i.strip()
                if i == "Q&A":
                    i = "#Q&A"
                elif i == "#machine_learing":
                    i = "#machine_learning"
                elif i == "#deep_leaning":
                    i = "#deep_learning"
                elif i == "#deep_learing":
                    i = "#deep_learning"
                elif i == "#webniar":
                    i = "#webinar"
                elif i == "#pythonlibararies":
                    i = "#pythonlibraries"
                if i == "#pythonlibraries":
                    i = "#python"
                if i in list_hashtag:
                    it_Hung.append(i)
            for i in row["Khánh"].split(','):
                i = i.strip()
                if i == "Q&A":
                    i = "#Q&A"
                elif i == "#machine_learing":
                    i = "#machine_learning"
                elif i == "#deep_leaning":
                    i = "#deep_learning"
                elif i == "#deep_learing":
                    i = "#deep_learning"
                elif i == "#webniar":
                    i = "#webinar"
                elif i == "#pythonlibararies":
                    i = "#pythonlibraries"
                if i == "#pythonlibraries":
                    i = "#python"
                if i in list_hashtag:
                    it_Khanh.append(i)
            for i in row["Cáp"].split(','):
                i = i.strip()
                if i == "Q&A":
                    i = "#Q&A"
                elif i == "#machine_learing":
                    i = "#machine_learning"
                elif i == "#deep_leaning":
                    i = "#deep_learning"
                elif i == "#deep_learing":
                    i = "#deep_learning"
                elif i == "#webniar":
                    i = "#webinar"
                elif i == "#pythonlibararies":
                    i = "#pythonlibraries"
                if i == "#pythonlibraries":
                    i = "#python"
                if i in list_hashtag:
                    it_Cap.append(i)
            if len(it_Cap) and len(it_Hung) and len(it_Khanh):
                Cap.append(it_Cap)
                Hung.append(it_Hung)
                Khanh.append(it_Khanh)
task_data = []
print("length of data: ",len(Hung))
for i in range(len(Hung)):
    item_H = ('Hung', str(i), frozenset(Hung[i]))
    item_K = ('Khanh', str(i), frozenset(Khanh[i]))
    item_C = ('Cap', str(i), frozenset(Cap[i]))
    task_data.append(item_H)
    task_data.append(item_K)
    task_data.append(item_C)

task = AnnotationTask(distance = masi_distance)

task.load_array(task_data)

print(task.alpha())