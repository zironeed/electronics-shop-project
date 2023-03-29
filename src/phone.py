from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int = 1) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim
        if self.__number_of_sim < 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim: int) -> None or ValueError:
        if new_number_of_sim >= 1:
            self.__number_of_sim = new_number_of_sim
            return new_number_of_sim
        raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Item) or isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise ValueError('Можно складывать только экземпляры классов Phone и Item')
