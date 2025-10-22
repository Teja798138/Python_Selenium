import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.visit_page_page import Visit_pad
from conftest import setup


@pytest.mark.sanity
@pytest.mark.order(3)
def test__004_visitpad(setup):
    #----- Driver Invoke ---------
    driver = setup
    #------- Login code ---------
    login_page = LoginPage(driver)
    login_page.login_check()
    #----------- Patient search ---------------
    vp = Visit_pad(driver)
    vp.search_patient()
    vp.visit_pad_test()
