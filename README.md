# VN_traffic_signs
Phát hiện và phân loại biển báo giao thông ở Việt Nam

# Phiên bản thư viện
streamlit==1.39.0
numpy==1.23.5
opencv-python==4.8.1.78
pandas==1.5.0
ultralytics==8.3.52
Pillow==9.2.0

# Hướng dẫn build và chạy demo

Bước 1: Kiểm tra và cài đặt môi trường ảo

Tạo môi trường ảo:
bash
python -m venv venv

Kích hoạt môi trường ảo:
Windows:
bash
venv\Scripts\activate
Linux/Mac:
source venv/bin/activate

Bước 2: Cài đặt các thư viện cần thiết

Dự án sử dụng pip để quản lý các thư viện. Bạn chỉ cần cài đặt các thư viện được liệt kê trong file requirements.txt.
Chạy lệnh sau để cài đặt tất cả các thư viện yêu cầu:
bash
pip install -r requirements.txt

Bước 3: Chạy ứng dụng

Dự án này sử dụng Streamlit, vì vậy để chạy ứng dụng, bạn chỉ cần sử dụng lệnh sau trong terminal:
bash
streamlit run app.py
Lệnh này sẽ mở ứng dụng trên trình duyệt của bạn. Bạn có thể làm việc với ứng dụng trực tuyến qua giao diện của Streamlit.


