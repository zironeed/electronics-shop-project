import pytest
from src.item import Item


@pytest.fixture
def item():
    item = Item('Samsa', 100000.0, 10)
    return item


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 1000000.0


def test_apply_discount(item):
    assert item.apply_discount() == 100000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('10.5') == 10


def test_name(item):
    assert item.name == 'Samsa'


def test_setter_name():
    item.name = 'WOK'
    assert item.name == 'WOK'


def test_repr():
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str():
    assert str(item) == 'Смартфон'
