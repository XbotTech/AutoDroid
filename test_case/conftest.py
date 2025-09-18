import pytest
from AutoDroid.py_page.base_page import BasePage


@pytest.fixture
def get_driver():
    diver = BasePage().driver
    yield diver
    diver.quit()
