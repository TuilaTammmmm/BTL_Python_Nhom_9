import sys

# Hỗ trợ hiển thị tiếng Việt trên Windows Console
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from models.medicine import PrescriptionMedicine, OTCMedicine
from services.inventory_service import InventoryService
from services.storage_service import StorageService
from services.search_sort_service import SearchSortService
from services.statistic_service import StatisticService
from ui.console_view import ConsoleView


def main():
    inventory = InventoryService()
    storage = StorageService()

    while True:
        ConsoleView.show_menu()
        choice = input("Vui lòng nhập lựa chọn (0-10): ").strip()

        if choice == "1":
            print("\n>> Chức năng 1: Thêm mới dược phẩm")
        elif choice == "2":
            print("\n>> Chức năng 2: Cập nhật thông tin dược phẩm")
        elif choice == "3":
            print("\n>> Chức năng 3: Xóa dược phẩm")
        elif choice == "4":
            print("\n>> Chức năng 4: Hiển thị danh sách dược phẩm")
            ConsoleView.display_medicines(inventory.medicines)
        elif choice == "5":
            print("\n>> Chức năng 5: Sắp xếp dược phẩm")
        elif choice == "6":
            print("\n>> Chức năng 6: Tìm kiếm dược phẩm")
        elif choice == "7":
            print("\n>> Chức năng 7: Nhập kho theo lô")
        elif choice == "8":
            print("\n>> Chức năng 8: Xuất kho an toàn")
        elif choice == "9":
            print("\n>> Chức năng 9: Thống kê & Báo cáo kho")
        elif choice == "10":
            print("\n>> Chức năng 10: Xuất file báo cáo .txt")
        elif choice == "0":
            print("\n>> Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print(">> Lựa chọn không hợp lệ, vui lòng chọn lại từ 0 đến 10!")


if __name__ == "__main__":
    main()
