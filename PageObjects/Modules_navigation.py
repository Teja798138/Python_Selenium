from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from PageObjects.base_page import BasePage

class ModulesNavigation(BasePage):
    Appointments_nav = (By.XPATH, '//*[@id="root"]/header/div[1]/div[1]/div[2]/a[1]/div/div/div')
    Consults_nav = (By.XPATH, "//i[@class='hx_people']")
    Tele_consults_nav = (By.XPATH,"//i[@class='hx_video-filled']")
    Menu_icon_nav = (By.XPATH, "//i[@class='hx_f-menu emr3tw-text-5']")
    Front_desk_nav = (By.XPATH, '//*[@id="root"]/header/div[1]/div[2]/div[8]/div/div[2]/div')
    Lab_nav = (By.XPATH, '//*[@id="root"]/header/div[1]/div[2]/div[8]/div/div[4]/div')
    Ipd_nav = (By.XPATH, '//*[@id="root"]/header/div[1]/div[2]/div[8]/div/div[5]/div')
    Pharmacy_nav = (By.XPATH, '//*[@id="root"]/header/div[1]/div[2]/div[8]/div/div[7]/div')

    def Navigate_appointment_page(self):
        self.wait.until(EC.element_to_be_clickable(self.Appointments_nav)).click()

    def Navigate_consutls_page(self):
        self.click(self.Consults_nav)

    def Navigate_teleconsults_page(self):
        self.click(self.Navigate_teleconsults_page())

    def Navigate_frondesk_page(self):
        self.click(self.Menu_icon_nav)
        self.click(self.Front_desk_nav)

    def Navigate_lab_page(self):
        self.click(self.Menu_icon_nav)
        self.click(self.Lab_nav)

    def Navigate_ipd_page(self):
        self.click(self.Menu_icon_nav)
        self.click(self.Ipd_nav)

    def Navigate_pharmacy_page(self):
        self.click(self.Menu_icon_nav)
        self.click(self.Pharmacy_nav)

