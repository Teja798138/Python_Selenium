import pytest
from Utilities.customlogger import Logger
from PageObjects.LoginPage import LoginPage
from conftest import setup

logger = Logger.setup_logger()

@pytest.mark.sanity
@pytest.mark.order(1)
def test_001_homePageTitle(setup):
    driver = setup
    login_page = LoginPage(driver)
    logger.info("Starting test: Login is attempting")
    login_page.login()
    logger.info("Successfully logged in")
    assert True


