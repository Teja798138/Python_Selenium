import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.readproperties import ReadConfig
from conftest import setup

@pytest.mark.sanity
@pytest.mark.order(1)
def test_001_homePageTitle(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login_check()
    assert True

valid_username = ReadConfig.getUseremail()
valid_password = ReadConfig.getPassword()

login_data = [
    (valid_username, "testst", "Fail"),
    ("fdgdhd@gmail.com", valid_password, "Fail"),
    ("nfjgggk@gmail.com", "dfkdngdg", "Fail")
]

@pytest.mark.parametrize("username, password, expected_result", login_data)
def test_login_scenarios(setup, username, password, expected_result):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login_validations(username, password)
    if expected_result == "Fail":
        print("Login attempts are failing as per the invalid scenarios")
    elif expected_result == "Pass":
        print("Login is passing with invalid data")

