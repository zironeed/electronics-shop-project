import csv
import os
import math


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError('Можно складывать только экземпляры классов Phone и Item')

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name) -> None or Exception:
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        csv_data = []
        count = 0

        script_dir = os.path.dirname(__file__)
        rel_path = "items.csv"
        abs_file_path = os.path.join(script_dir, rel_path)
        cls.all.clear()

        with open(abs_file_path) as file:
            reader = csv.reader(file, delimiter=",")
            for line in reader:
                if count == 0:
                    count += 1
                    continue
                csv_data.append(line)
        for data in csv_data:
            cls(*data)

    @staticmethod
    def string_to_number(number: str):
        return math.floor(float(number))
