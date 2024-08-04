from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from BasePage.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.rev_cal_ele = None
        self.driver = driver
        self.wait = wait

    # locators
    __revenue_calculator = (By.XPATH, "//a[normalize-space()='Revenue Calculator']")

    # locator methods
    def get_revenue_calculator(self):
        rev_cal_ele = self.wait.until(EC.presence_of_element_located(self.__revenue_calculator))
        return rev_cal_ele
    
    def click_revenue_calculator(self):
        self.click_element(self.get_revenue_calculator())