import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.Modules_navigation import ModulesNavigation
from PageObjects.appointment_page import Appointmentpage
from conftest import setup

@pytest.mark.sanity
@pytest.mark.order(2)
def test_002_appointments_creation(setup):
    #---------- driver Invoke ---------------------
    driver = setup
    #---------- Login code -------------------------
    login_page = LoginPage(driver)
    login_page.login_check()
    # ------------------ Navigation to appointment ------------------
    nav = ModulesNavigation(driver)
    nav.Navigate_appointment_page()
    #-------------- Patient and Appointment creation code ---------
    app_page = Appointmentpage(driver)
    app_page.create_appointment()
    app_page.validate_appointment_details_displayed()
    assert app_page.validate_appointment_details_displayed() is True, "Id is not visible"
    print("Appointment ID is visible")
    print("Patient Name header is visible")
    print("Visit header is visible")
    print("Status state is visible")
    app_page.search_patient()












