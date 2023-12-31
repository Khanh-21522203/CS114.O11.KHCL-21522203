import os.path

import pandas as pd
fname = ['p_dsmlvietnam.csv', 'p_mlcoban.csv', 'p_mlopvn.csv']
list_hashtag = []
for fn in fname:
    df = pd.read_csv(os.path.join('process_data',fn))
    for ls_ht in df["old_hastag"].apply(str):
        ls_ht = ls_ht.split('\t')
        list_hashtag = ls_ht + list_hashtag

print(list(set(list_hashtag)))