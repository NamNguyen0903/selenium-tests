# Selenium Test Project

Dự án này chứa các kịch bản kiểm thử tự động sử dụng Selenium để kiểm tra các chức năng khác nhau của ứng dụng web. Mục tiêu của dự án là đảm bảo rằng các chức năng quan trọng của trang web hoạt động đúng và có thể phát hiện các lỗi phát sinh trong quá trình sử dụng.

## Thiết Lập Môi Trường

1. **Clone Kho Mã**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Cài Đặt Các Thư Viện Yêu Cầu**:
   Cài đặt các thư viện Python cần thiết từ file `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Thiết Lập WebDriver**:
   - Tải WebDriver tương thích với phiên bản trình duyệt của bạn.
   - Thêm WebDriver vào PATH của hệ thống hoặc đặt vào thư mục dự án.

4. **Cấu Hình pytest.ini**:
   File `pytest.ini` cung cấp cấu hình cho pytest, bao gồm các tùy chọn như mức độ log, hiển thị chi tiết kiểm thử, và các báo cáo bổ sung. Đảm bảo tệp này nằm trong thư mục dự án.

## Chạy Các Kịch Bản Kiểm Thử

Các kịch bản kiểm thử đã được thiết kế để xác minh các chức năng riêng biệt của ứng dụng web. Để chạy tất cả các kiểm thử, sử dụng lệnh:

```bash
pytest --html=report.html --self-contained-html
```

Điều này sẽ tạo báo cáo `report.html` có thể xem được trong trình duyệt sau khi kiểm thử hoàn thành.

### Chạy Các Kịch Bản Cụ Thể

1. **Kiểm Thử Xác Minh Dữ Liệu**:
   ```bash
   python test_data_validation.py
   ```

2. **Kiểm Thử Xử Lý Lỗi**:
   ```bash
   python test_error_handling.py
   ```

3. **Kiểm Thử Gửi Biểu Mẫu**:
   ```bash
   python test_form_submission.py
   ```

4. **Kiểm Thử Đăng Nhập/Đăng Xuất**:
   ```bash
   python test_login_logout.py
   ```

5. **Kiểm Thử Điều Hướng**:
   ```bash
   python test_navigation.py
   ```

6. **Kiểm Thử Thiết Kế Đáp Ứng**:
   ```bash
   python test_responsive_design.py
   ```

7. **Kiểm Thử Chức Năng Tìm Kiếm**:
   ```bash
   python test_search_functionality.py
   ```

### Xem Báo Cáo Kết Quả

- Báo cáo được tạo tại `report.html`, bao gồm kết quả của tất cả các kịch bản kiểm thử (13 bài kiểm thử thành công, 1 bài thất bại).
- Báo cáo sẽ hiển thị số bài kiểm thử thành công, thất bại, và thời gian hoàn thành của mỗi bài.

### Lưu Ý

- Đảm bảo rằng ứng dụng web đang chạy và có thể truy cập trước khi thực hiện các kịch bản kiểm thử.
- Một số kịch bản có thể yêu cầu biến môi trường (ví dụ: API key, URL). Tham khảo trong mã của từng kịch bản để biết chi tiết cấu hình.

## Giải Quyết Sự Cố

- **Lỗi WebDriver**: Đảm bảo phiên bản WebDriver tương thích với trình duyệt của bạn.
- **Lỗi Thư Viện Thiếu**: Chạy lại `pip install -r requirements.txt` để đảm bảo tất cả các thư viện cần thiết đã được cài đặt.
- **Lỗi Cấu Hình pytest**: Kiểm tra file `pytest.ini` để đảm bảo các tùy chọn được cấu hình đúng cách.

## Giấy Phép

Dự án này được cấp phép theo giấy phép MIT. Xem chi tiết trong tệp LICENSE.

---

Chúc bạn kiểm thử thành công!
```

Tệp `README.md` này bao gồm hướng dẫn thiết lập chi tiết, cách chạy từng kịch bản kiểm thử, tạo báo cáo, và các lưu ý xử lý lỗi.
