<h3 align="center" font-size= 14px;><b>Trường Đại Học Công Nghệ Thông Tin - ĐHQH TPHCM</b></h3>
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: 5;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>
<h1 align="center"><b>Đồ án cuối kỳ môn Máy học - CS114.O11.KHCL</b></h1>
<h2 align="center"><b>Recommend Topic Hashtags</b></h2>

* Bộ môn: Máy học - CS114.O11.KHCL
* Giảng viên:
  * Lê Đình Duy - *duydl@uit.edu.vn*
  * Phạm Nguyễn Trường An - *truonganpn@uit.edu.vn*
* Thành viên nhóm:
<p align="center">

| STT |   MSSV   |    Họ và Tên    |        Email        |
| --- |:--------:| --------------: | ---------------------: |
| 1   | 21522203 |  Đào Nhật Khánh | 21522203@gm.uit.edu.vn |
| 2   | 21522700 | Cáp Hữu Anh Trí | 21522700@gm.uit.edu.vn |
| 3   | 21522110 | Bùi Mạnh Hùng | 21522110@gm.uit.edu.vn |

</p>

# **BẢNG MỤC LỤC**

1. [Tổng Quan Về Đồ Án](#tongquan)
2. [Xây Dựng Bộ Dữ Liệu](#dulieu)
3. [Training Và Đánh Giá Model](#training)
4. [Hướng Phát Triển Ứng Dụng Và Cải Tiến](#ungdung)
5. [Nguồn Tham Khảo](#thamkhao)

<a name="tongquan"></a>
# **1. Tổng Quan Về Đồ Án**
# Mô tả bài toán

* **Ngữ cảnh ứng dụng**:
  * Trong các nhóm facebook, hashtag được sử dụng rộng rãi để gắn thẻ và tổ chức các bài viết. Tuy nhiên, việc tìm kiếm và sử dụng hashtag phù hợp lại khá thụ động và tốn nhiều thời gian cho người dùng. Và còn tồn tại rất nhiều bài viết trong group chưa được gán hashtag. Do đó, nhóm chúng em đặt mục tiêu xây dựng một hệ thống có thể tự động đề xuất các hashtag liên quan cho nội dung bài viết trong các nhóm Facebook.
      <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/b65d8d08-f570-494d-8583-260686b263b5"/> </div>  
  * Để phù hợp với quy mô ứng dụng, và phạm vi thực nghiệm, nhóm chỉ giới hạn nội dung là các bài post trong group facebook có liên quan đến lĩnh vực Computer Science
* **INPUT và OUTPUT Bài toán:**
  * INPUT: 
    * Nội dung một bài post : chỉ bao gồm dữ liệu dạng văn bản
    * Bộ dữ liệu đào tạo bao gồm text và các nhãn (hashtags) tương ứng
  * OUTPUT: 
    * Đưa ra gợi ý hashtags (có trong tập dữ liệu)
<a name="dulieu"></a>
# **3.Xây Dựng Bộ Dữ Liệu**
## Mô tả dữ liệu
Dữ liệu được nhóm tự thu thập
* **Tại sao cần tự thu thập dữ liệu thủ công:**
  * Không có bộ dữ liệu phù hợp với mục tiêu và bài toán nhóm đặt ra :
      * Ngôn ngữ Tiếng Việt
      * Liên quan đến lĩnh vực Computer Science
* **Các tiêu chí khi thu thập dữ liệu:**
  * Thu thập dự kiến trên 1000 mẫu
  * Liên quan đến lĩnh vực Computer Science
  * Ngôn ngữ chiếm đa số trong nội dung là Tiếng Việt 
* **Việc thu thập dữ liệu:**
  * Crawl dữ liệu trên 2 group: [Forum Machine Learning cơ bản](https://www.facebook.com/groups/machinelearningcoban) và [Group hỏi đáp Python, Data Science, Machine Learning, Deep Learning](https://www.facebook.com/groups/dsmlvietnam) 
* **Khó khăn của việc thu thập dữ liệu:**
  * Do thu thập dữ liệu tự động, nên sẽ có nhiều bài viết nội dung không liên quan, bài viết rác
* **Gán nhãn bộ dữ liệu**
  * Quy trình gán nhãn bộ dữ liệu
      <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/2ce8b609-2f3f-494d-ab9b-18701655cc08"/>
      <div style=width: 130px; align = center>Quy trình gán nhãn dữ liệu</div>
  * Hướng dẫn gán nhãn dữ liệu
      * Đĩnh nghĩa các nhãn dữ liệu
        * #sharing : có nội dung chia sẻ kinh nghiệm, job, tài liệu, cuộc thi, webinar,..
        * #machine_learning: có nội dung về các bài toán, thuật toán Machine Learning truyền thống như:  Linear Regression, Logistic Regression, scalar,... hoặc liên quan về road_map,..
        * #deep_learning: có nội dung về các bài toán, thuật toán Deep Learning hiện đại như: LSTM, Transformer,..  hoặc liên quan về road map,..
        * #python : có nội dung liên quan về code python, hoặc các thư viện hỗ trợ như  pytorch, tensorflow, pandas… 
        * #data: có nội dung liên quan đến dữ liệu , xử lý dữ liệu ,.., hoặc liên quan về road map, nghề nghiệp về data
        * #cv: có nội dung liên quan đến bài toán thuộc lĩnh vực Computer Vision, hoặc liên quan về road map, nghề nghiệp trong lĩnh vưc Computer Vision,.
        * #nlp: có nội dung liên quan đến bài toán thuộc lĩnh việc NLP, hoặc liên quan về road map, nghề nhiệp trong lĩnh vực NLP,..
        * #math: có nội dung liên quan đến kiến thức toán học như xác suất thống kê, đại số, giải tích,..
        * #Q&A: có nội dung liên quan đến hỏi đáp về một số vấn đề trong lĩnh vực Computer Science
      * Một số lưu ý khi gán nhãn:
        * Bỏ qua các bài nội dung hoàn toàn bằng Tiếng Anh
        * Bỏ qua các bài nội dung không liên quan đến nhãn
        * Mỗi bài nội dung có thể có nhiều hashtag
  * Tính độ đồng thuận
      * Sử dụng công thức **Krippendorff's alpha** để tính độ đồng thuận
        <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/273d5fa5-a433-4468-a8f0-80afef486987"/> </div>
      * Đánh giá trên thang đo độ đồng thuận Landis và Koch
        <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/c9687d25-0cb9-49d2-ad9e-09e289ba13c7" width="300"/> </div>
      * Kết quả đánh giá gán nhãn của nhóm:
          * Số người gán nhãn: 3
          * Số mẫu dữ liệu: 89 mẫu
          * Độ đồng thuận: 0.716
          > => Theo thang đo của Landis và Koch, độ đồng thuận ở mức **substantial** do đó nhóm tiến hành gán nhãn toàn bộ
* **Các bước tiền xử lý dữ liệu**
    * Normalize: xóa ký tự xuống dòng, lowercase toàn bộ văn bản.
    * Remove hastags, links, emojis: xóa những hashtags (chuỗi bắt đầu bằng '#'), những links (chuỗi bắt đầu bằng 'http') và các emoji.
    * Tokenizer: dùng pyvi.ViTokenizer.
        * Ví dụ:  công cụ ai giúp tăng tốc độ học của bạn link to pdf ->  công_cụ ai giúp tăng_tốc_độ học của bạn link to pdf
    * Encode number: chuyển các số trong văn bản thành '<number>'.
    * Delete one-length token: xóa những token có độ dài bằng 1.
  <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/3c299271-c480-4f48-a8be-1d9ab23ab5b8"/> </div>
  <div style=width: 130px; align = center>Các bước tiền xử lý dữ liệu</div>
* **Phân chia dữ liệu train-test**
    * Các bước chia dữ liệu
      * Với mỗi hashtag, lấy 10% data để tạo tập test.
      * Xóa những samples trùng nhau ở tập test.
      * Loại bỏ samples trong tập test ở data gốc để tạo tập train.
    <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/7c839333-fece-4466-9e4e-d3ca80ab970f"/> </div>
    <div style=width: 130px; align = center>Minh họa cách phân chia dữ liệu</div>
    * Kết quả sau khi phân chia dữ liệu
      <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/4585e789-184d-47bc-ac13-7ff18643a53c"/> </div>
* **Tổng quan về Bộ Dữ liệu:**
  *  Bộ dữ liệu: gồm 1282 mẫu dữ liệu  
  * Thống kê dữ liệu sau khi gán nhãn
    
      <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/4fc24414-80f3-44ff-ad32-d3f8bda3af85"/> </div>  
      <div style=width: 130px; align = center>Thống kê dữ liệu sau khi gán nhãn</div>
  * Thống kê về độ dài của các câu trong tập dữ liệu
      <div align="middle"> <img src= "https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/c9fe4358-acd0-4f3f-bb3a-d935aa070d8f"/> </div>  
      <div style=width: 130px; align = center>Thống kê về độ dài của các câu</div>
      
<h3> Nhận xét: </h3>
<ol> 
  <li> Ta thấy rằng bộ dữ liệu phân đang bị bất cân bằng giữa các nhãn. </li>
  <li> Trong quá trình tiền xử lý dữ liệu, nhóm vẫn chưa xử lý được các từ viết tắt hoặc sai lỗi chính tả</li>
</ol>

<a name="training"></a>
# **4. Training Và Đánh Giá Model**
  * Các phương pháp sử dụng
    * TF-IDF, BOW với mô hình Logistic Regression, SVM, Naive Bayes
    * LSTM
    * Transformer
      Chi tiết xem (tại đây)[https://www.canva.com/design/DAF5i5ginJk/0iG2RNULtHUpxP3lhUzf1Q/edit?utm_content=DAF5i5ginJk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton]
<a name="ungdung"></a>
# 5. Hướng Phát Triển Ứng Dụng Và Cải Tiến:
  * **Hướng phát triển trong tương lai:**
    * Tìm các phương pháp xử lý dữ liệu viết tắt, sai chính tả
    * Tăng cường dữ liệu, đồng thời xử lý bất cân bằng dữ liệu hiện tại
    * Tìm kiếm các mô hình tối ưu, đạt được độ chính xác cao hơn
    * Mở rộng bài toán bằng cách thêm nhiều nhãn và nhiều lĩnh vực khác nữa
<a name="thamkhao"></a>
# 6. Nguồn Tham Khảo:

[1] https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html

[2] https://www.nltk.org/_modules/nltk/metrics/agreement.html

[3] https://mmuratarat.github.io/2020-0125/multilabel_classification_metrics
