import requests
from underthesea import word_tokenize

API_URL = "https://api-inference.huggingface.co/models/bmd1905/vietnamese-correction"
headers = {"Authorization": "Bearer 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"}

def spell_correction(text):
	payload = {"inputs": text}
	response = requests.post(API_URL, headers=headers, json=payload)
	response = response.json()
	output = response[0]['generated_text']
	return output

def word_segmentation(text):
    return word_tokenize(text)
    
if __name__=="__main__":
    print(spell_correction("Lần này anh Phươngqyết xếp hàng mua bằng được 1 chiếc"))
    print(word_segmentation("Bác sĩ bây giờ có thể thản nhiên báo tin bệnh nhân bị ung thư"))