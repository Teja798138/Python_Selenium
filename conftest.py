import pytest
from selenium import webdriver
from Utilities.readproperties import ReadConfig

@pytest.fixture(autouse=True)
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(ReadConfig.getApplicationURL())
    yield driver
    driver.quit()
