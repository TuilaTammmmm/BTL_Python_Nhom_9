class Supplier:
    """Lớp quản lý thông tin nhà cung cấp dược phẩm"""

    def __init__(self, supplier_id: str, supplier_name: str, phone: str = "", address: str = ""):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.phone = phone
        self.address = address

    def display_info(self) -> str:
        return f"[{self.supplier_id}] {self.supplier_name} - SĐT: {self.phone} - ĐC: {self.address}"

    def to_dict(self) -> dict:
        return {
            "supplier_id": self.supplier_id,
            "supplier_name": self.supplier_name,
            "phone": self.phone,
            "address": self.address,
        }
