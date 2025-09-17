from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def is_displayed(self, locator):
        """Check if element is displayed"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def select_dropdown_by_visible_text(self, locator, text):
        try:
            element = self.driver.find_element(*locator)
            dropdown = Select(element)
            dropdown.select_by_visible_text(text)
            print(f"Successfully selected '{text}' from dropdown with locator {locator}")
        except Exception as e:
            print(f"Error selecting option '{text}' from dropdown with locator {locator}: {e}")
            raise