import requests
from underthesea import word_tokenize
import re
from urlextract import URLExtract
API_URL = "https://api-inference.huggingface.co/models/bmd1905/vietnamese-correction"
headers = {"Authorization": "Bearer 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"}

def spell_correction(text):
	payload = {"inputs": text}
	response = requests.post(API_URL, headers=headers, json=payload)
	response = response.json()

	output = response[0]['generated_text']
    
	return output

def lowercase(text):
    return text.lower()

def remove_url(text):
    extractor = URLExtract()
    url_to_remove = extractor.find_urls(text)
    for word in url_to_remove:
        text = re.sub(r'\b' + re.escape(word) + r'\b', " ", text, flags=re.IGNORECASE)
    return text

def remove_emojis(data):
  emoj = re.compile(r"""[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002702-\U000027B0\U000024C2-\U0001F251\U0001f926-\U0001f937\U00010000-\U0010ffff\u200d\u23cf\u23e9\u231a\ufe0f\u3030-]+(?<!\n)""", re.UNICODE)
  return re.sub(emoj, '', data)

def word_segmentation(text):
    return word_tokenize(text)
    
def denoise(text):
    text = re.sub(r"[?!.,;:<>{}=~|\[\]()/#@\"\'\-\n]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text
def preprocessing(text):
    
    text = remove_emojis(text)
    text = remove_url(text)
    text = denoise(text)
    text = spell_correction(text)
    text = lowercase(text)
    text = word_segmentation(text)
    return text
if __name__=="__main__":
    # print(spell_correction("Lần này anh Phươngqyết xếp hàng mua bằng được 1 chiếc"))
    # print(word_segmentation("Bác sĩ bây giờ có thể thản nhiên báo tin bệnh nhân bị ung thư"))
    print(preprocessing("Repo áp dụng hai models tốt nhất hiện nay trong việc phân loại điểm bất thường (hư hỏng hay trầy xước) của các vật thể công nghiệp \
                                là FastFlow và PatchCore nhằm so sánh và cải thiện khả năng phân loại của models. Đề tài được xây dựng và bám sát hai bài nghiên cứu \
                                là:Towards Total Recall in Industrial Anomaly Detection: [https://arxiv.org/abs/2106.08265]\
                                FastFlow: Unsupervised Anomaly Detection and Localization via 2D Normalizing Flows: [https://arxiv.org/abs/2111.07677]"))