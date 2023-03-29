import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone():
    phone = Phone('Samsung', 120000, 5, 2)
    return phone


@pytest.fixture
def item():
    item = Item('Xiaomi', 10000, 40)
    return item


def test_repr(phone):
    assert repr(phone) == "Phone('Samsung', 120000, 5, 2)"


def test_number_of_sim_getter(phone):
    assert phone.number_of_sim == 2


def test_number_of_sim_setter(phone):
    phone.number_of_sim = 4
    assert phone.number_of_sim == 4


def test_add(phone, item):
    assert phone + item == 45
