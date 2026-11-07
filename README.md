# Quản Lý Kho Dược Phẩm (Pharmaceutical Inventory Management System)

## 1. Giới thiệu dự án

Ứng dụng dòng lệnh (Console CLI) quản lý kho dược phẩm được xây dựng theo phương pháp lập trình hướng đối tượng (OOP) và kiến trúc phân lớp (Layered Architecture). Hệ thống hỗ trợ theo dõi thuốc, nhà cung cấp, kiểm soát nhập/xuất kho an toàn, cảnh báo thuốc cận hạn/hết hạn và báo cáo thống kê trực quan.

## 2. Các chức năng chính

- **Quản lý danh mục thuốc:** Thêm, sửa, xóa, tra cứu thông tin chi tiết thuốc, hạn sử dụng, nhà sản xuất.
- **Quản lý nhà cung cấp:** Quản lý thông tin đối tác cung ứng dược phẩm.
- **Quản lý Nhập / Xuất kho:**
  - Nhập kho: Ghi nhận lô hàng mới, cập nhật số lượng tồn và lưu lịch sử giao dịch.
  - Xuất kho an toàn: Kiểm tra tồn kho, ngăn chặn xuất các lô thuốc đã hết hạn sử dụng.
- **Tìm kiếm & Sắp xếp:** Tra cứu thuốc theo tên/mã, lọc theo danh mục, sắp xếp theo giá hoặc hạn sử dụng.
- **Báo cáo & Thống kê:** Thống kê tổng giá trị tồn kho, danh sách thuốc sắp hết hàng, cảnh báo thuốc cận hạn (dưới 30 ngày).
- **Lưu trữ dữ liệu:** Lưu trữ và đồng bộ tự động dữ liệu ra định dạng JSON.

## 3. Cấu trúc thư mục

```text
2.Code/
├── data/              # Thư mục lưu trữ dữ liệu JSON
├── models/            # Lớp thực thể đối tượng (Medicine, Supplier, Transaction)
├── services/          # Xử lý logic nghiệp vụ (kho, xuất/nhập, tìm kiếm, thống kê)
├── ui/                # Giao diện người dùng trên dòng lệnh (Console CLI)
├── utils/             # Các hàm tiện ích, kiểm tra tính hợp lệ dữ liệu
├── main.py            # Điểm khởi chạy chương trình chính
├── .gitignore         # Cấu hình bỏ qua các tệp tạm của Git
└── README.md          # Tài liệu tổng quan dự án
```

## 4. Yêu cầu & Hướng dẫn sử dụng

- **Yêu cầu môi trường:** Python 3.10 trở lên.
- **Cài đặt thư viện:** Dự án sử dụng hoàn toàn thư viện chuẩn (`Standard Library`) của Python, không cần cài thêm thư viện ngoài.
