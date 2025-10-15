from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Visit_pad(BasePage):
    #------ Locators for patient search -----------------------------------
    custom_patient_search = (By.XPATH, '//input[@placeholder="Search Patient  🔍"]')
    select_patient_name = (By.XPATH, '//*[@id="searchResult"]/div[2]/div[2]/div')
    visit_pad_page_confirm = '//*[@id="react_emr_mfe_patient_header"]/div[1]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div'
    vital1_select = (By.XPATH,'//*[@id="react_emr_mfe_body_container"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/input')
    vital2_select = (By.XPATH, '//*[@id="react_emr_mfe_body_container"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div/input')
    vital3_select = (By.XPATH, '//*[@id="react_emr_mfe_body_container"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[4]/div/div[2]/div/input')
    vital4_select = (By.XPATH, '//*[@id="react_emr_mfe_body_container"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[4]/div/div[2]/div/input')
    vital5_select = (By.XPATH, '//*[@id="react_emr_mfe_body_container"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[5]/div/div[2]/div/input')
    #--------- Locators for Visit page and text boxes --------

    def search_patient(self):
        self.wait.until(EC.presence_of_element_located(self.custom_patient_search))
        self.click(self.custom_patient_search)
        self.enter_text(self.custom_patient_search, "teststss")
        self.wait.until(EC.element_to_be_clickable(self.select_patient_name))
        self.click(self.select_patient_name)
        print("Patient Name was clicked from search bar")

    def visit_pad_test(self):
        self.is_displayed(self.visit_pad_page_confirm)
        print("Visitpad Home page is displaying")
        self.wait.until(EC.element_to_be_clickable(self.vital1_select))
        self.click(self.vital1_select)
        self.enter_text(self.vital1_select, 45)
        self.click(self.vital2_select)
        self.enter_text(self.vital2_select, 55)
        self.click(self.vital3_select)
        self.enter_text(self.vital3_select, 66)
        self.click(self.vital4_select)
        self.enter_text(self.vital4_select, 67)
        self.click(self.vital5_select)
        self.enter_text(self.vital5_select, 58)







