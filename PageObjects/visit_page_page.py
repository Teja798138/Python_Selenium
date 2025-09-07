import time

from selenium.webdriver.common.by import By

from PageObjects.appointment_page import Appointmentpage
from PageObjects.base_page import BasePage

class Visit_pad(BasePage):
    #------ Locators for patient search -----------------------------------
    custom_patient_search = (By.XPATH, '//input[@placeholder="Search Patient  🔍"]')
    select_patient_name = (By.XPATH, '//*[@id="searchResult"]/div[2]/div[2]/div[1]/div[2]')

    #--------- Locators for Visit page page and text boxes --------

    def search_patient(self):
        self.click(self.custom_patient_search)
        time.sleep(3)
        self.enter_text(self.custom_patient_search, "test")
        self.click(self.select_patient_name)



