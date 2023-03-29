import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    item = Item('Samsa', 100000.0, 10)
    return item


@pytest.fixture
def phone():
    phone = Phone('Ifone', 120000, 10, 2)
    return phone


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


def test_setter_name(item):
    item.name = 'WOK'
    assert item.name == 'WOK'


def test_repr(item):
    assert repr(item) == "Item('Samsa', 100000.0, 10)"


def test_str(item):
    assert str(item) == 'Samsa'


def test_add(item, phone):
    assert item + phone == 20
