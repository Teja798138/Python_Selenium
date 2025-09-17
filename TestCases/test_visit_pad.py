import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.Modules_navigation import ModulesNavigation
from PageObjects.visit_page_page import Visit_pad
from conftest import setup


@pytest.mark.sanity
def test__004_visitpad(setup):
    #----- Driver Invoke ---------
    driver = setup
    #------- Login code -------
    login_page = LoginPage(driver)
    login_page.login()
    #----------- Patient search ---------------

    vp = Visit_pad(driver)
    vp.search_patient()