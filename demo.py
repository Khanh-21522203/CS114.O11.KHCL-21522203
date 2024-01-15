
import numpy as np
import torch
from torchtext.transforms import ToTensor
import torch.nn as nn
from joblib import load
import streamlit as st
from tools.preprocessing import preprocessing
from torch.utils.data import Dataset, DataLoader
import pandas as pd

model_load= load('trained_.joblib')
scaler_load = load('scaler.joblib')


class HashtagRecommendation(nn.Module):
  def __init__(self, embedding_dim, hidden_dim, vocab_size, num_labels):
    super(HashtagRecommendation, self).__init__()
    self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)
    self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
    self.fc1 = nn.Linear(hidden_dim, 128)
    self.fc2 = nn.Linear(128, 64)
    self.fc3 = nn.Linear(64, num_labels)
    self.relu = nn.ReLU()
    self.sigmoid = nn.Sigmoid()
    self.dropout = nn.Dropout(p=0.2)

  def forward(self, sentence):
    embeds = self.word_embeddings(sentence)
    lstm_out, _ = self.lstm(embeds)
    # Select the last output of LSTM layer
    lstm_out = lstm_out[:, -1, :]
    x = self.relu(self.fc1(lstm_out))
    x = self.dropout(x)
    x = self.relu(self.fc2(x))
    x = self.dropout(x)
    logits = self.fc3(x)
    probs = self.sigmoid(logits)
    return probs
  
class HashTag_Dataset(Dataset):
  def __init__(self, root, max_length=250):
    super(HashTag_Dataset, self).__init__()
    self.classes = ['#Q&A', '#cv', '#data', '#deep_learning', '#machine_learning', '#math', '#nlp', '#python', '#sharing']
    text, labels = [], []

    df = pd.read_csv(root, encoding='utf-8-sig')
    texts = df['text']
    labels = df["label"]
    self.texts = texts
    self.labels = labels
    self.vocab = self.make_vocab(texts)
    self.max_length = max_length
  def make_vocab(self, texts):
    vocab = dict()
    for text in texts:
      words = text.split()
      for word in words:
        if word not in vocab:
          vocab[word] = 1
        else:
          vocab[word] += 1
    vocab = list(dict(filter(lambda x: x[1]>3, vocab.items())).keys())
    vocab.append('<UNK>')
    vocab.append('<PAD>')
    return vocab
  def encode_text(self, text):
    words = text.split()
    if len(words) > self.max_length:
      words = words[:self.max_length]
    else:
      words += ['<PAD>']*(self.max_length-len(words))
    enc = [self.vocab.index(w) if w in self.vocab else self.vocab.index('<UNK>') for w in words]
    return enc
  def encode_label(self, label):
    enc = ast.literal_eval(label)
    enc = [1 if l in enc else 0 for l in self.classes]
    return enc
  def __len__(self):
    return len(self.labels)

  def len_vocab(self):
    return len(self.vocab)

  def num_classes(self):
    return len(self.classes)

  def __getitem__(self, idx):
    text = self.texts[idx]
    label = self.labels[idx]
    encode = self.encode_text(text)
    label = self.encode_label(label)
    encode = torch.tensor(encode, dtype=torch.long)
    label = torch.tensor(label, dtype=torch.float32)
    return encode, label
train_set = HashTag_Dataset(root = "data/train_data.csv")
model_lstm = torch.load('lstm copy.pth', map_location=torch.device('cpu'))

st.title(":blue[HASHTAG RECOMMENDATION]")    
st.subheader(":green[Python, Data Science, Machine Learning, Deep Learning]")
post = st.text_input('Nội dung bài đăng 👉')
option = st.selectbox(
   "Chọn Model",
   ("SVM", "LSTM", "Transformer"),
   index=None,
   placeholder="Chọn model . . .",
)


def predict_label(array):
    
    selected_classes_indices = np.where(array == 1)[1]
    selected_classes = [Classes[index] for index in selected_classes_indices]
    return selected_classes
    
if post:
    if option == 'SVM':
        post = preprocessing(post)
        post_scaled = scaler_load.transform([post])
        predict = model_load.predict(post_scaled)
        st.write('Hashtag recommendation : ')
        for item in range(len(predict_label(predict))):
            st.write(item+1  , predict_label(predict)[item])
    elif option == 'LSTM':
        test = train_set.encode_text(post)
        test = ToTensor()(test)[None, :]
        test = test.to('cpu')
        pred = model_lstm(test)[0].tolist()
        pred = [train_set.classes[i] for i in range(len(pred)) if pred[i]>0.5]
        st.write('Hashtag recommendation : ')
        for item in range(len(pred)):
            st.write(item+1  , pred[item])
        
    elif option == 'Transformer':
        st.write('Hashtag recommendation : ')
    else:
       st.write('Vui lòng chọn model ')