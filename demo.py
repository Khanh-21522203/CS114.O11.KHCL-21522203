
import numpy as np
from joblib import load
model_load= load('trained_.joblib')
scaler_load = load('scaler.joblib')
import streamlit as st
from tools.preprocessing import preprocessing
st.title(":blue[HASHTAG RECOMMENDATION]")    
st.subheader(":green[Python, Data Science, Machine Learning, Deep Learning]")
post = st.text_input('Nội dung bài đăng 👉')
def predict_label(array):
    Classes = ['#Q&A', '#cv' ,'#data', '#deep_learning' ,'#machine_learning' ,'#math', '#nlp',
 '#python' ,'#sharing']
    selected_classes_indices = np.where(array == 1)[1]
    selected_classes = [Classes[index] for index in selected_classes_indices]
    return selected_classes
    
if post:
    post = preprocessing(post)
    post_scaled = scaler_load.transform([post])
    predict = model_load.predict(post_scaled)
    st.write('Hashtag recommendation : ')
    for item in range(len(predict_label(predict))):
        st.write(item+1  , predict_label(predict)[item])