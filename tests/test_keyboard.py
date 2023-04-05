from src.keyboard import Keyboard

import pytest

@pytest.fixture
def keyboard():
    keyboard = Keyboard('HyperX Alloy FPS', 6999, 10)
    return keyboard


def test_init(keyboard):
    assert repr(keyboard) == "Keyboard('HyperX Alloy FPS', 6999, 10)"


def test_change_lang(keyboard):
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang().change_lang()
    assert keyboard.language == 'RU'
