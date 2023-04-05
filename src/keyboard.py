from src.item import Item


class MixinLanguage:
    """Миксин для смены раскладки"""
    def __init__(self):
        """Инициализация раскладки клавиатуры"""
        self.__language = 'EN'

    def change_lang(self):
        """Метод для смены языка"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        """Метод для вывода состояния раскладки"""
        return self.__language


class Keyboard(Item, MixinLanguage):
    """Класс клавиатуры"""
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Инициализация класса Item и миксина MixinLanguage"""
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
