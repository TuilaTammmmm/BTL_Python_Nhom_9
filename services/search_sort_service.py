class SearchSortService:
    """Nghiệp vụ tìm kiếm và sắp xếp dược phẩm"""

    @staticmethod
    def search_by_id(medicines: list, medicine_id: str) -> list:
        """Tìm kiếm chính xác theo mã thuốc"""
        pass

    @staticmethod
    def search_by_name(medicines: list, keyword: str) -> list:
        """Tìm kiếm gần đúng theo tên thuốc"""
        pass

    @staticmethod
    def search_by_batch(medicines: list, batch_number: str) -> list:
        """Tìm kiếm theo số lô sản xuất"""
        pass

    @staticmethod
    def sort_medicines(medicines: list, criterion: str = "expiry", reverse: bool = False) -> list:
        """Sắp xếp thuốc theo hạn dùng hoặc số lượng tồn kho"""
        pass
