from abc import ABC, abstractmethod
from datetime import datetime


class Medicine(ABC):
    """
    Lớp trừu tượng (Abstract Base Class) đại diện cho Dược phẩm tổng quát.
    Thể hiện tính Trừu tượng (Abstraction) và Đóng gói (Encapsulation).
    """

    def __init__(self, medicine_id: str, medicine_name: str, batch_number: str, expiry_date: str, quantity: int, unit_price: float):
        # Thuộc tính protected (có tiền tố _) để các lớp con có thể kế thừa và truy cập
        self._medicine_id = str(medicine_id).strip()
        self._medicine_name = str(medicine_name).strip()
        self._batch_number = str(batch_number).strip()
        self._expiry_date = str(expiry_date).strip()

        # Gọi trực tiếp qua setter để kiểm tra hợp lệ dữ liệu ngay khi khởi tạo
        self.quantity = quantity
        self.unit_price = unit_price

    # --- TÍNH ĐÓNG GÓI: CÁC PROPERTY GETTER & SETTER VÀ KIỂM TRA DỮ LIỆU ĐẦU VÀO ---

    @property
    def medicine_id(self) -> str:
        """Getter: Lấy mã định danh duy nhất của thuốc"""
        return self._medicine_id

    @property
    def medicine_name(self) -> str:
        """Getter: Lấy tên thuốc"""
        return self._medicine_name

    @medicine_name.setter
    def medicine_name(self, value: str):
        """Setter: Cập nhật tên thuốc, kiểm tra không được để trống"""
        val = str(value).strip() if value else ""
        if not val:
            raise ValueError("Tên thuốc không được để trống!")
        self._medicine_name = val

    @property
    def batch_number(self) -> str:
        """Getter: Lấy số lô sản xuất"""
        return self._batch_number

    @batch_number.setter
    def batch_number(self, value: str):
        """Setter: Cập nhật số lô, kiểm tra không được để trống"""
        val = str(value).strip() if value else ""
        if not val:
            raise ValueError("Số lô sản xuất không được để trống!")
        self._batch_number = val

    @property
    def expiry_date(self) -> str:
        """Getter: Lấy hạn sử dụng dạng chuỗi YYYY-MM-DD"""
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value: str):
        """Setter: Cập nhật hạn sử dụng, kiểm tra đúng định dạng YYYY-MM-DD và ngày hợp lệ"""
        val = str(value).strip() if value else ""
        try:
            datetime.strptime(val, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Hạn sử dụng '{val}' không hợp lệ! Vui lòng nhập đúng định dạng YYYY-MM-DD.")
        self._expiry_date = val

    @property
    def quantity(self) -> int:
        """Getter: Lấy số lượng tồn kho"""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Setter: Cập nhật số lượng tồn kho, kiểm tra không được là số âm (< 0)"""
        try:
            val = int(value)
        except (ValueError, TypeError):
            raise ValueError("Số lượng tồn kho phải là số nguyên!")
        if val < 0:
            raise ValueError("Số lượng tồn kho không được là số âm (< 0)!")
        self._quantity = val

    @property
    def unit_price(self) -> float:
        """Getter: Lấy đơn giá thuốc"""
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        """Setter: Cập nhật đơn giá thuốc, kiểm tra đơn giá phải lớn hơn 0 (> 0)"""
        try:
            val = float(value)
        except (ValueError, TypeError):
            raise ValueError("Đơn giá thuốc phải là số thực!")
        if val <= 0:
            raise ValueError("Đơn giá thuốc phải lớn hơn 0 (> 0)!")
        self._unit_price = val

    # --- CÁC PHƯƠNG THỨC XỬ LÝ HẠN DÙNG VÀ NGHIỆP VỤ ---

    def is_expired(self) -> bool:
        """
        Kiểm tra thuốc đã hết hạn hay chưa.
        So sánh ngày hết hạn của thuốc với ngày hiện tại của hệ thống.
        Trả về True nếu ngày hết hạn < ngày hiện tại, ngược lại trả về False.
        """
        exp_date = datetime.strptime(self._expiry_date, "%Y-%m-%d").date()
        today = datetime.now().date()
        return exp_date < today

    def days_until_expiry(self) -> int:
        """
        Tính số ngày còn lại đến khi thuốc hết hạn.
        - Trả về số nguyên dương: Số ngày còn hạn sử dụng.
        - Trả về số âm: Số ngày thuốc đã quá hạn sử dụng.
        """
        exp_date = datetime.strptime(self._expiry_date, "%Y-%m-%d").date()
        today = datetime.now().date()
        return (exp_date - today).days

    def __str__(self) -> str:
        """Phương thức biểu diễn chuỗi thông tin cơ bản của dược phẩm"""
        return f"[{self._medicine_id}] {self._medicine_name} | Lô: {self._batch_number} | HSD: {self._expiry_date} | Tồn: {self._quantity} | Giá: {self._unit_price:,.0f}đ"

    # --- TÍNH ĐA HÌNH: CÁC PHƯƠNG THỨC TRỪU TƯỢNG BẮT BUỘC LỚP CON GHI ĐÈ ---

    @abstractmethod
    def calculate_stock_value(self) -> float:
        """Tính tổng giá trị tồn kho của mặt hàng thuốc này (Số lượng * Đơn giá)"""
        pass

    @abstractmethod
    def display_info(self) -> str:
        """Hiển thị chi tiết toàn bộ thông tin thuốc bao gồm thông tin đặc thù của từng loại"""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Chuyển đổi đối tượng thành dictionary phục vụ lưu trữ file JSON bền vững"""
        pass


class PrescriptionMedicine(Medicine):
    """
    Lớp Thuốc kê đơn (ETC) - Thể hiện tính Kế thừa (Inheritance) từ Medicine.
    Đặc thù: Cần có chỉ định của bác sĩ và lưu trữ thông tin giấy phép bác sĩ kê đơn.
    """

    def __init__(self, medicine_id: str, medicine_name: str, batch_number: str, expiry_date: str, quantity: int, unit_price: float, doctor_license: str = ""):
        # Gọi hàm khởi tạo của lớp cha Medicine
        super().__init__(medicine_id, medicine_name, batch_number, expiry_date, quantity, unit_price)
        # Thuộc tính riêng của thuốc kê đơn
        self._doctor_license = str(doctor_license).strip()

    @property
    def doctor_license(self) -> str:
        """Getter: Lấy giấy phép hoặc mã chứng chỉ bác sĩ kê đơn"""
        return self._doctor_license

    @doctor_license.setter
    def doctor_license(self, value: str):
        """Setter: Cập nhật giấy phép bác sĩ"""
        self._doctor_license = str(value).strip()

    # --- TÍNH ĐA HÌNH (POLYMORPHISM): GHI ĐÈ CÁC PHƯƠNG THỨC TRỪU TƯỢNG ---

    def calculate_stock_value(self) -> float:
        """Tính giá trị tồn kho thuốc kê đơn: Số lượng tồn * Đơn giá"""
        return self._quantity * self._unit_price

    def display_info(self) -> str:
        """Hiển thị thông tin thuốc kê đơn kèm trạng thái hạn dùng và thông tin bác sĩ"""
        status = "ĐÃ HẾT HẠN" if self.is_expired() else f"Còn {self.days_until_expiry()} ngày"
        bs = self._doctor_license if self._doctor_license else "Chưa chỉ định"
        return f"[KÊ ĐƠN] {self.__str__()} | GP Bác sĩ: {bs} | Trạng thái: {status}"

    def to_dict(self) -> dict:
        """Xuất thông tin thuốc kê đơn ra dictionary để lưu JSON"""
        return {
            "type": "Prescription",
            "medicine_id": self._medicine_id,
            "medicine_name": self._medicine_name,
            "batch_number": self._batch_number,
            "expiry_date": self._expiry_date,
            "quantity": self._quantity,
            "unit_price": self._unit_price,
            "doctor_license": self._doctor_license,
        }


class OTCMedicine(Medicine):
    """
    Lớp Thuốc không kê đơn (OTC) - Thể hiện tính Kế thừa (Inheritance) từ Medicine.
    Đặc thù: Thuốc bán tự do không cần đơn, có hướng dẫn sử dụng hoặc chỉ định riêng.
    """

    def __init__(self, medicine_id: str, medicine_name: str, batch_number: str, expiry_date: str, quantity: int, unit_price: float, usage_note: str = ""):
        # Gọi hàm khởi tạo của lớp cha Medicine
        super().__init__(medicine_id, medicine_name, batch_number, expiry_date, quantity, unit_price)
        # Thuộc tính riêng của thuốc OTC
        self._usage_note = str(usage_note).strip()

    @property
    def usage_note(self) -> str:
        """Getter: Lấy hướng dẫn chỉ định sử dụng thuốc"""
        return self._usage_note

    @usage_note.setter
    def usage_note(self, value: str):
        """Setter: Cập nhật hướng dẫn sử dụng"""
        self._usage_note = str(value).strip()

    # --- TÍNH ĐA HÌNH (POLYMORPHISM): GHI ĐÈ CÁC PHƯƠNG THỨC TRỪU TƯỢNG ---

    def calculate_stock_value(self) -> float:
        """Tính giá trị tồn kho thuốc không kê đơn: Số lượng tồn * Đơn giá"""
        return self._quantity * self._unit_price

    def display_info(self) -> str:
        """Hiển thị thông tin thuốc OTC kèm trạng thái hạn dùng và chỉ định sử dụng"""
        status = "ĐÃ HẾT HẠN" if self.is_expired() else f"Còn {self.days_until_expiry()} ngày"
        note = self._usage_note if self._usage_note else "Đọc kỹ hướng dẫn trước khi dùng"
        return f"[OTC] {self.__str__()} | Chỉ định: {note} | Trạng thái: {status}"

    def to_dict(self) -> dict:
        """Xuất thông tin thuốc OTC ra dictionary để lưu JSON"""
        return {
            "type": "OTC",
            "medicine_id": self._medicine_id,
            "medicine_name": self._medicine_name,
            "batch_number": self._batch_number,
            "expiry_date": self._expiry_date,
            "quantity": self._quantity,
            "unit_price": self._unit_price,
            "usage_note": self._usage_note,
        }


if __name__ == "__main__":
    import sys
    # Hỗ trợ in tiếng Việt có dấu trên Windows Console
    if sys.stdout.encoding != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    # Khối kiểm thử độc lập cho module medicine.py
    print("=== KIỂM THỬ MODULE MEDICINE (TÂM) ===")
    
    # Tạo thử thuốc kê đơn (còn hạn)
    p_med = PrescriptionMedicine(
        medicine_id="TH01",
        medicine_name="Amoxicillin 500mg",
        batch_number="LOT-2026-01",
        expiry_date="2026-12-31",
        quantity=100,
        unit_price=25000,
        doctor_license="BS_CHUYEN_KHOA_01"
    )
    print(p_med.display_info())
    print("Giá trị tồn kho:", f"{p_med.calculate_stock_value():,.0f} VNĐ")
    print("Đã hết hạn chưa?:", p_med.is_expired())

    # Tạo thử thuốc OTC (giả lập đã hết hạn để test)
    otc_med = OTCMedicine(
        medicine_id="TH02",
        medicine_name="Panadol Extra",
        batch_number="LOT-2024-02",
        expiry_date="2024-01-01",
        quantity=50,
        unit_price=12000,
        usage_note="Giảm đau hạ sốt nhanh"
    )
    print("\n" + otc_med.display_info())
    print("Đã hết hạn chưa?:", otc_med.is_expired(), f"(Quá hạn {abs(otc_med.days_until_expiry())} ngày)")

    # Kiểm tra tính đóng gói: Chặn số lượng âm
    try:
        otc_med.quantity = -10
        print("LỖI: Chưa chặn được số lượng âm!")
    except ValueError as e:
        print("\nBắt lỗi số lượng âm thành công:", e)

    print("\n=== HOÀN THÀNH KIỂM THỬ MODULE MEDICINE THÀNH CÔNG ===")
