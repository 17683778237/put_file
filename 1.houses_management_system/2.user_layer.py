from business_logic_layer import HouseManagerController

class HouseManagerView:
    def __init__(self):
        self.__controller = HouseManagerController()

    def __display_menu(self):
        print("1键查看所有房源信息")
        print("2键查看总价最高的房源信息")
        print("3键查看面积最小的房源信息")
        print("4键显示户型种类")

    def __select_menu(self):
        item = int(input("请输入选项:"))
        if item == 1:
            self.__display_all()
        if item == 2:
            self.__display_max()
        if item == 3:
            self.__display_min()
        if item == 4:
            self.__show_house_type()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_all(self):
        for house_infos in self.__controller.list_houses:
            print(house_infos.__dict__)

    def __display_max(self):
        print(self.__controller.display_max_total_price().__dict__)

    def __display_min(self):
        print(self.__controller.display_min_area().__dict__)

    def __show_house_type(self):
        for type,count in self.__controller.show_house().items():
            print(type,"有",count,"个")



