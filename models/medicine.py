from abc import ABC, abstractmethod


class Medicine(ABC):
    """Lớp trừu tượng đại diện cho dược phẩm"""

    def __init__(self, medicine_id: str, medicine_name: str, batch_number: str, expiry_date: str, quantity: int, unit_price: float):
        self._medicine_id = medicine_id
        self._medicine_name = medicine_name
        self._batch_number = batch_number
        self._expiry_date = expiry_date
        self._quantity = quantity
        self._unit_price = unit_price

    @property
    def medicine_id(self):
        return self._medicine_id

    @property
    def medicine_name(self):
        return self._medicine_name

    @property
    def batch_number(self):
        return self._batch_number

    @property
    def expiry_date(self):
        return self._expiry_date

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value

    def is_expired(self) -> bool:
        """Kiểm tra thuốc đã hết hạn hay chưa"""
        pass

    def days_until_expiry(self) -> int:
        """Tính số ngày còn lại đến khi hết hạn"""
        pass

    @abstractmethod
    def calculate_stock_value(self) -> float:
        """Tính tổng giá trị tồn kho"""
        pass

    @abstractmethod
    def display_info(self) -> str:
        """Hiển thị thông tin thuốc"""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Chuyển đổi dữ liệu thành dictionary để lưu file"""
        pass


class PrescriptionMedicine(Medicine):
    """Thuốc kê đơn (ETC)"""

    def __init__(self, medicine_id: str, medicine_name: str, batch_number: str, expiry_date: str, quantity: int, unit_price: float, doctor_license: str = ""):
        super().__init__(medicine_id, medicine_name, batch_number, expiry_date, quantity, unit_price)
        self._doctor_license = doctor_license

    def calculate_stock_value(self) -> float:
        return self._quantity * self._unit_price

    def display_info(self) -> str:
        pass

    def to_dict(self) -> dict:
        pass


class OTCMedicine(Medicine):
    """Thuốc không kê đơn (OTC)"""

    def __init__(self, medicine_id: str, medicine_name: str, batch_number: str, expiry_date: str, quantity: int, unit_price: float, usage_note: str = ""):
        super().__init__(medicine_id, medicine_name, batch_number, expiry_date, quantity, unit_price)
        self._usage_note = usage_note

    def calculate_stock_value(self) -> float:
        return self._quantity * self._unit_price

    def display_info(self) -> str:
        pass

    def to_dict(self) -> dict:
        pass
