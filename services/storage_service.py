import json
import os


class StorageService:
    """Dịch vụ lưu trữ và đọc dữ liệu từ file JSON"""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def save_data(self, filename: str, data: list):
        """Ghi danh sách đối tượng ra file JSON"""
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([item.to_dict() for item in data], f, ensure_ascii=False, indent=2)

    def load_data(self, filename: str) -> list:
        """Đọc dữ liệu từ file JSON"""
        filepath = os.path.join(self.data_dir, filename)
        if not os.path.exists(filepath):
            return []
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
