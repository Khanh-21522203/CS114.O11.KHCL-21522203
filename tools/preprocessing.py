import re
from pyvi import ViTokenizer

def normalize(text):
    t = text.replace('\n', ' ')
    t = t.lower()
    return t

def delete_hashtag(text):
    return re.sub(r'#\w+', '', text)

def delete_link(text):
    return re.sub(r'http\S+', '', text)

def remove_emojis(text):
    emoj = re.compile(r"""[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002702-\U000027B0\U000024C2-\U0001F251\U0001f926-\U0001f937\U00010000-\U0010ffff\u200d\u23cf\u23e9\u231a\ufe0f\u3030-]+(?<!\n)""", re.UNICODE)
    return re.sub(emoj, '', text)

def encode_number(text):
    t = text.split(' ')
    t = map(lambda x: '<number>' if bool(re.match(r'^[0-9]+(\.[0-9]+)?$', x)) else x, t)
    return ' '.join(t)

def delete_onelen_token(text):
    t = text.split(' ')
    t = filter(lambda x: len(x)>1, t)
    return ' '.join(t)

def preprocessing(text):
    t = normalize(text)
    t = delete_hashtag(t)
    t = delete_link(t)
    t = remove_emojis(t)
    t = ViTokenizer.tokenize(t)
    t = encode_number(t)
    t = delete_onelen_token(t)
    return t

if __name__=="__main__":
    text = """dạ chào anh Việt và mọi người, hiện tại em đang làm đồ án dự báo công suất phát nhà máy điện mặt trời bằng mô hình LSTM.
            Bộ dữ liệu em đang có là bức xạ, nhiệt độ môi trường, nhiệt độ tấm pin, và công suất phát của nhà máy.
            Em học điện, cũng mới tìm hiểu mảng này, nên mọi người ai có làm rồi có ý tưởng hay tài liệu gì chia sẻ giúp em với ạ.
            em cám ơn mọi người."""
    print(preprocessing(text))