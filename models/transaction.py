class MedicineTransaction:
    """Lớp ghi nhận lịch sử giao dịch nhập và xuất kho"""

    def __init__(self, transaction_id: str, medicine_id: str, quantity: int, transaction_type: str, transaction_date: str = "", note: str = ""):
        self.transaction_id = transaction_id
        self.medicine_id = medicine_id
        self.quantity = quantity
        self.transaction_type = transaction_type  # "IMPORT" hoặc "EXPORT"
        self.transaction_date = transaction_date
        self.note = note

    def display_info(self) -> str:
        return f"[{self.transaction_id}] {self.transaction_type} Thuốc: {self.medicine_id} | SL: {self.quantity} | Ngày: {self.transaction_date}"

    def to_dict(self) -> dict:
        return {
            "transaction_id": self.transaction_id,
            "medicine_id": self.medicine_id,
            "quantity": self.quantity,
            "transaction_type": self.transaction_type,
            "transaction_date": self.transaction_date,
            "note": self.note,
        }
