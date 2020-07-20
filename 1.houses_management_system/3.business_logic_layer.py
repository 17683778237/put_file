import collections
from typing import List, Dict

from dal import HouseDao
from model import HouseModel

class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

    @property
    def list_houses(self) -> List[HouseModel]:
        return self.__list_houses

    def display_max_total_price(self):
        # max_total_price = self.__list_houses[0]
        # for i in range(1,len(self.__list_houses)):
        #     if max_total_price.total_price < self.__list_houses[i].total_price:
        #         max_total_price = self.__list_houses[i]
        # return max_total_price
        return max(self.__list_houses,key=(lambda house:house.total_price))

    def display_min_area(self):
        return min(self.__list_houses)

    def show_house(self):
        return collections.Counter(map(lambda house:house.house_type,self.__list_houses))
