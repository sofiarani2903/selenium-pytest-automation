import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()
def test_valid_login(setup):
     login = LoginPage(setup)
     login.enter_username("tomsmith")
     login.enter_password("SuperSecretPassword!")
     login.click_login_btn()
     assert "You logged into a secure area!" in login.get_message()
def test_invalid_login(setup):
    login = LoginPage(setup)
    login.enter_username("wrong")
    login.enter_password("wrong")
    login.click_login_btn()
    assert "Your username is invalid!" in login.get_message()

def test_empty_login(setup):
    login = LoginPage(setup)
    login.click_login_btn()
    assert "Your username is invalid!" in login.get_message()


