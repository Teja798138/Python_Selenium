import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from Utilities.data_generator import generate_random_name, generate_random_mobile
from selenium.webdriver.support.ui import Select


class Appointmentpage(BasePage):
    # ----------- Locators to create patient and appointment ----------------------
    add_patient = (By.XPATH, "//i[@class='hx_person-add']")
    patient_name_placeholder = (By.XPATH, "//input[@placeholder='Enter Name']")
    patient_mobile_number_placeholder = (By.XPATH, "//input[@placeholder='Enter Number']")
    gender = (By.XPATH, '//*[@id="add-patient-modal"]/div[2]/div[2]/div[1]/div[2]/div/button[1]')
    age = (By.XPATH, "//input[@placeholder='Age' and @min = '0']")
    add_create_bill = (By.XPATH, '//*[@id="add-patient-modal"]/div[3]/div/div[2]/button[1]/div')
    add_button = (By.XPATH, "//button[@id='bpAddServiceButton']")
    con_button = (By.XPATH, "//button[@onclick='addConsultService()']")
    create_bill = (By.XPATH, "//button[@id='saveServices']")
    pay_bill = (By.XPATH, "//button[@id='allBillBtn']")
    close_popup = (By.XPATH, "//button[@class='close-btn-php']")

    #-------------------- Locators validations for patient appointed -------------------
    Appointments_nav = (By.XPATH, "//i[@class='hx_calendar-date']")
    Id = (By.XPATH, "//div[@id='first-appointments-table']/table/thead/tr/th[1]")
    patient_name_app = (By.XPATH, "//div[@id='first-appointments-table']/table/thead/tr/th[4]")
    visit_status = (By.XPATH, "//div[@id='first-appointments-table']/table/thead/tr/th[4]")
    status_state = (By.XPATH, "//div[@id='first-appointments-table']/table/thead/tr/th[9]")

    #------------------- Locators validations for search -------------------
    patient_search = (By.XPATH, "//input[@data-qa='testid_patientSearch']")
    search_result = (By.XPATH, '//*[@id="searchResult"]/div[2]/div[2]/div[1]')

    def __init__(self, driver):
        super().__init__(driver)
        self.select_service_dropdown = (By.XPATH, '//*[@id="serviceNames_chosen"]/a/span')
        #Dynamic locator for selecting a service by its name
        self.service_option_by_name = (By.XPATH, '//*[@id="serviceNames_chosen"]/div/ul/li[text()="{}"]')
        self.doctor_list_select = (By.XPATH, '//select[@id="dictorList"]')

    def select_service_by_name(self, service_name):
        print(f"Opening the service dropdown to select '{service_name}'...")
        self.click(self.select_service_dropdown)
        # Format the dynamic locator with the desired service name
        specific_service_locator = (self.service_option_by_name[0], self.service_option_by_name[1].format(service_name))
        print(f"'{service_name}', selected successfully")
        self.click(specific_service_locator)
        print(f"'{service_name}', select successfully")

    def select_doctor_by_name(self, doctor_name):
        print(f"Finding the doctor dropdown to select '{doctor_name}'....")
        doctor_dropdown_element = self.wait.until(EC.visibility_of_element_located(self.doctor_list_select))
        select = Select(doctor_dropdown_element)
        select.select_by_visible_text(doctor_name)
        print(f"Doctor {doctor_name}' selected successfully.")


    #------------------- Actions -------------------------
    def create_appointment(self):
        patient_name = generate_random_name()
        patient_mobile_number = generate_random_mobile()
        self.click(self.add_patient)
        self.enter_text(self.patient_name_placeholder, patient_name)
        self.enter_text(self.patient_mobile_number_placeholder, patient_mobile_number)
        self.click(self.gender)
        self.enter_text(self.age, 25)
        self.click(self.add_create_bill)
        self.select_service_by_name("First Consultation - [1234]")
        self.click(self.add_button)
        self.select_doctor_by_name("Dr Bose")
        self.click(self.con_button)
        self.click(self.create_bill)
        self.click(self.pay_bill)
        self.click(self.close_popup)

    def validate_appointment_details_displayed(self):
        time.sleep(2)
        return self.is_displayed(self.Id and self.patient_name_app and self.visit_status and self.status_state)

    def search_patient(self):
        self.click(self.patient_search)
        self.enter_text(self.patient_search, "test")
        print("Patient search filter was happened")
        self.click(self.search_result)
        print("Patient name was clicked")




