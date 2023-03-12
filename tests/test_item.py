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
