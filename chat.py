import g4f

g4f.debug.logging = True  # Enable debug logging
g4f.debug.check_version = False  # Disable automatic version checking

content = "Chaò mọi người !! \n\
Chắc nhiều bạn có biết tới các nơi 😅  thân quen sau: LibG*n, SciH*b, ZL*b. \n \
Với các bạn làm nghiên cứu, chắc hẳn SciH*b không còn quá xa lạ. Trang này cung cấp một lượng lớn báo khoa học mà bạn có thể tải về m.i.ễ.n p.h.í. Tuy nhiên, từ năm 2020 trở lại đây, do dính dáng tới 1 vụ kiện cáo ở Ấn Độ, trang SH tạm ngưng việc cập nhật/bổ sung các bài báo mới (báo từ 2020 trở lại đây). Vậy làm sao để tìm báo khoa học mới đây? \n \
Cách 1: Trả tiền để đọc báo trên trang xuất bản. "
## Normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4_turbo  ,
    messages=[{"role": "user", "content": f'{content} \nchỉ xóa emoji, và chỉ sửa lỗi chính tả, không thay thế câu, chỉ trả về kết quả là nội dung chỉnh sửa, không viết gì thêm'}],
)

print("sau khi xử lý:\n", response)