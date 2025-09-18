import pytest
from py_page.base_page import BasePage


@pytest.fixture
def get_driver():
    driver = BasePage().driver
    yield driver
    driver.quit()
