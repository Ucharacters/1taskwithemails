#создание виртуального подкласса
from abc import ABC,abstractmethod

class IRoadSign(ABC):
    def __init__(self):
        self.location= None
        self.size= None
        self.number= None
	
    @abstractmethod
    def vertical_location_policy():
        """Do nothing"""

class SpecificRoad(list):
    install = list.append
    def deinstall(self, mark):
        del self[self.index(mark)]     
    pass

@IRoadSign.register  #функции расширены типичными функциями класса list
class InfoSign(SpecificRoad):
    def vertical_location_policy():
        """знаки можно размещать не более 3 один над другим"""
        pass
    pass

print("функции расширены ", InfoSign.mro()) 

road_from_spb_to_moscow=[]
newsign=InfoSign(road_from_spb_to_moscow)


newsign.install(28.155)
print("установлен новый знак на отметке", newsign,"м")
newsign.install(101.155)
print("добавляем ещё один новый знак на отметке 101.155 м", newsign)
print("удаляем знак 28.155 м")
newsign.deinstall(28.155)
print("оставшиеся знаки", newsign)
newsign.number="предупреждающий знак №..."
print("также знак унаследовал свойства IRoadSign=", newsign.number)




    
