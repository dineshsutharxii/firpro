import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from BasePage.BasePage import BasePage


class RevenueCalculatorpage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.rev_cal_ele = None
        self.driver = driver
        self.wait = wait

    # locators
    __rpm_and_ccm = (By.XPATH, "//*[normalize-space()='RPM and CCM Programs - CPT code reimbursement (Non-Facility Rates) NOTE: These Numbers Vary State to State']")
    __slider_circle = (By.XPATH, "//span[contains(@class, 'MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium')]/input")
    __whole_slider = (By.XPATH, "//span[contains(@class, 'MuiSlider-root MuiSlider-colorPrimary MuiSlider-sizeMedium')]")
    __medicare_eligible_patients_textbox = (By.XPATH, "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall')]")

    # locator methods
    def get_rpm_and_ccm(self):
        rpm_and_ccm = self.wait.until(EC.presence_of_all_elements_located(self.__rpm_and_ccm))
        return rpm_and_ccm

    def get_xpath_element(self, xpath_locator):
        return self.wait.until(EC.presence_of_element_located(xpath_locator))

    def check_visiblity_of_rpm_and_ccm(self):
        r_and_c_elements = self.get_rpm_and_ccm()
        for element in r_and_c_elements:
            if element.text != 'RPM and CCM Programs - CPT code reimbursement (Non-Facility Rates) NOTE: These Numbers Vary State to State':
                return True
        return True

    def scroll_till_slider_section(self):
        slider_section = self.get_rpm_and_ccm()
        self.scroll_to_elememt(slider_section[0])
        slider_section = self.get_xpath_element(self.__slider_circle)
        return slider_section.is_displayed()

    def slide_the_slider(self, target_value):
        slider_circle = self.get_xpath_element(self.__slider_circle)
        whole_slider = self.get_xpath_element(self.__whole_slider)
        current_slider = self.move_slider(whole_slider, slider_circle, target_value)
        return int(current_slider) == int(target_value)

    def check_slider_textbox_value(self, value):
        text_value_in_slider_textbox = self.get_attribute_value(self.get_xpath_element(self.__medicare_eligible_patients_textbox), 'value')
        return int(text_value_in_slider_textbox) == int(value)

    def check_silder_value(self, value):
        value_in_slider = self.get_attribute_value(self.get_xpath_element(self.__slider_circle), 'aria-valuenow')
        return int(value_in_slider) == int(value)

    def enter_text_in_slider_text(self, slider_value):
        self.enter_text(self.get_xpath_element(self.__medicare_eligible_patients_textbox), slider_value)



