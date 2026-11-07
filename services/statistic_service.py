class StatisticService:
    """Nghiệp vụ thống kê, cảnh báo hạn dùng và tính giá trị tồn kho"""

    @staticmethod
    def get_expired_medicines(medicines: list) -> list:
        """Lấy danh sách thuốc đã hết hạn"""
        pass

    @staticmethod
    def get_near_expiry_medicines(medicines: list, days: int = 30) -> list:
        """Lấy danh sách thuốc sắp hết hạn"""
        pass

    @staticmethod
    def get_low_stock_medicines(medicines: list, threshold: int = 20) -> list:
        """Lấy danh sách thuốc có lượng tồn thấp"""
        pass

    @staticmethod
    def calculate_total_value(medicines: list) -> dict:
        """Tính tổng giá trị tồn kho theo loại thuốc"""
        pass

    @staticmethod
    def export_report_txt(medicines: list, filename: str = "Bao_cao_kho.txt"):
        """Xuất báo cáo kiểm kê kho ra file text"""
        pass
