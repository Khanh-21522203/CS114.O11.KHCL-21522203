import g4f
import csv
# g4f.debug.logging = False  # Enable debug logging
# g4f.debug.check_version = False  # Disable automatic version checking

content = "Chaò mọi người !! \n\
# Chắc nhiều bạn có biết tới các nơi 😅  thân quen sau: LibG*n, SciH*b, ZL*b. \n \
# Với các bạn làm nghiên cứu, chắc hẳn SciH*b không còn quá xa lạ. Trang này cung cấp một lượng lớn báo khoa học mà bạn có thể tải về m.i.ễ.n p.h.í. Tuy nhiên, từ năm 2020 trở lại đây, do dính dáng tới 1 vụ kiện cáo ở Ấn Độ, trang SH tạm ngưng việc cập nhật/bổ sung các bài báo mới (báo từ 2020 trở lại đây). Vậy làm sao để tìm báo khoa học mới đây? \n \
# Cách 1: Trả tền để đoc bóa trên trang xuat ban. "
content1 = "[HCM] Mình đng tim co-founder co startup AI dài hạn, bạn nào quan tâm và thấy phù hợp thì inbox mình nhé, nếu bạn là chuyên về nghiên cứu AI càng phù hợp."
content2 = "4 nhóm phương pháp chính để phát hiện Outliers 🔥🔥🔥\
# Hi các bạn, \
# 2 hôm trước mình vừa đọc được 1 post rất hay trên linkedin về chủ đề outlier detection. Mình xin dịch + tóm gọn lại để các bạn cùng nắm được ☺️\
# Có rất nhiều phương pháp để có thể phát hiện được outliers, nhưng nhìn chung các phương pháp này sẽ được chia vào 4 nhóm lớn:\
# Nhóm dựa vào thống kê: Nhóm này dựa vào box plot hoặc các graph tương tự. Thường thì các điểm nằm ngoài vùng 1.5 lần interquartile có khả năng cao là outliers. Các điểm nằm ngoài vùng 3 lần interquartile được coi là các extreme outliers.\
# Nhóm dựa vào độ lân cận: Nhóm này dựa vào khoảng cách để xác định outliers. Thông thường thì KNN sẽ được sử dụng để chỉ ra các outliers dựa vào khoảng cách giữa chúng tới các điểm lân cận.\
# Nhóm dựa vào Time Series: Time Series làm tăng độ phức tạp do có xu hướng tổng quan của dữ liệu (trend effect) và xu hướng theo mùa hoặc tháng (seasonal effect). STL (Seasonal Trend Loses) Decomposition có thể được sử dụng để loại bỏ ảnh hưởng của các xu hướng này trước. Sau đó các kĩ thuật thống kê như là interquartile range (IQR) có thể được sử dụng để phát hiện outliers.\
# Nhóm dựa vào Machine Learning: 1 vài thuật toán Machine Learning như Isolation Forest có thể được dùng để phát hiện outliers. \
# Link đến bài viết gốc: https://www.linkedin.com/posts/mattdancho_outliers-have-led-me-to-100s-of-business-activity-7142179371833782272-TeVN?utm_source=share&utm_medium=member_desktop"
## Normal response
#gpt_4
# response = g4f.ChatCompletion.create(
#     model= g4f.models.gpt_4 ,
#     messages=[
#         # {"role": "user", "content": f'{content} \nyêu cầu: chỉ xóa emoji, và chỉnh sửa lỗi chính tả, không thay thế câu,chỉ trả về kết quả là đoạn văn đã chính sửa theo theo yêu cầu không viết gì thêm'},
#         # {"role": "user", "content": f'{content} \nhãy xóa emoji, chỉnh sửa lỗi chính tả, không xóa nội dung , không thay thế câu,trả về kết quả theo format: \nKẾT QUẢ CHỈNH SỬA: "nội dung đã chỉnh sửa"'},
#         {"role": "user", "content": f'{content2} \nhãy xóa emoji, chỉnh sửa lỗi chính tả, không xóa nội dung , không thay thế câu,trả về kết quả theo format: \nKẾT QUẢ CHỈNH SỬA: "nội dung đã chỉnh sửa"'}
#     ],
#     stream=False,
# )
file_path = "../data/dsmlvietnam.csv"
import pandas as pd

df = pd.read_csv("../data/dsmlvietnam.csv", sep='\t', index_col=0)
sub_df = df
sub_df = sub_df.drop(axis=1, columns=['Links'])
model = ['gpt-4', 'gpt-4-turbo']
i = 0
# sub_df["Processed_data"] = None
# for idx, content in enumerate(sub_df["Contents"]):
#     # mod = model[1]
#     # if i%2 == 0:
#     #     mod = model[0]
#     # print(content)
#     # response = g4f.ChatCompletion.create(
#     #     model= mod ,
#     #     messages=[
#     #         {
#     #             "role": "system",
#     #             "content": "Tôi gửi bạn một nội dung bài viết, Nhiệm vụ của bạn là: Chỉ xóa emoji, chỉnh sửa lỗi chính tả tiếng việt, giữ nguyên nội dung, và trả về kết quả theo format: \nKẾT QUẢ CHỈNH SỬA: <sos>nội dung đã chỉnh sửa</eos>"
#     #         },
#     #         {
#     #             "role": "user",
#     #             "content": f'{content}'}
#     #     ],
#     #     stream=False,
#     # )
#     # print(response)
#     sub_df["Processed_data"][idx] = response
#     i +=1
#     if i%20==0:
#         print("save at index: ",i)
#         # sub_df.to_csv("", encoding='utf-8-sig', index=False)
#         df.to_csv("processml.csv", mode="a", index=False, header=not pd.Series(["processml.csv"]).exists())
sub_df.to_csv("processml.csv", encoding='utf-8-sig', index=False)
