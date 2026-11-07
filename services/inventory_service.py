from models.medicine import Medicine


class InventoryService:
    """Nghiệp vụ quản lý kho dược phẩm"""

    def __init__(self):
        self.medicines = []
        self.transactions = []

    def add_medicine(self, medicine: Medicine):
        """Thêm mới dược phẩm vào kho"""
        pass

    def update_medicine(self, medicine_id: str, **kwargs):
        """Cập nhật thông tin dược phẩm"""
        pass

    def delete_medicine(self, medicine_id: str):
        """Xóa dược phẩm theo mã"""
        pass

    def import_medicine(self, medicine_id: str, quantity: int, batch_number: str = ""):
        """Nhập kho dược phẩm theo lô"""
        pass

    def export_medicine(self, medicine_id: str, quantity: int):
        """Xuất kho dược phẩm (chặn xuất thuốc hết hạn, chặn xuất vượt tồn)"""
        pass
