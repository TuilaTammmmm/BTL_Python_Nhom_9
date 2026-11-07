class ConsoleView:
    """Giao diện dòng lệnh hiển thị bảng và menu"""

    @staticmethod
    def show_menu():
        """Hiển thị menu chính của chương trình"""
        print("\n" + "=" * 50)
        print("    HỆ THỐNG QUẢN LÝ KHO DƯỢC PHẨM - NHÓM 09")
        print("=" * 50)
        print("1. Thêm mới dược phẩm")
        print("2. Cập nhật thông tin dược phẩm")
        print("3. Xóa dược phẩm (có xác nhận Y/N)")
        print("4. Hiển thị danh sách dược phẩm")
        print("5. Sắp xếp dược phẩm (Hạn dùng / Tồn kho)")
        print("6. Tìm kiếm dược phẩm (Mã / Tên / Số lô)")
        print("7. Nhập kho theo lô")
        print("8. Xuất kho an toàn (Chặn xuất thuốc hết hạn)")
        print("9. Thống kê, cảnh báo hạn dùng & Giá trị kho")
        print("10. Xuất báo cáo kiểm kê ra file (.txt)")
        print("0. Lưu dữ liệu & Thoát chương trình")
        print("=" * 50)

    @staticmethod
    def display_medicines(medicines: list):
        """Hiển thị danh sách thuốc theo dạng bảng"""
        if not medicines:
            print(">> Danh sách rỗng!")
            return
        for m in medicines:
            print(f"- [{m.medicine_id}] {m.medicine_name} | Lô: {m.batch_number} | HSD: {m.expiry_date} | Tồn: {m.quantity} | Giá: {m.unit_price}")
