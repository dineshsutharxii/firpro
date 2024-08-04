import pytest
import selenium
from pages.fitpeo_home_page import HomePage
from pages.fitpeo_reveneue_calculate_page import RevenueCalculatorpage


@pytest.mark.usefixtures('setup')
class TestFitPeo:
    def test_check_url(self):
        page_title = self.driver.title
        assert page_title == "Remote Patient Monitoring (RPM) - fitpeo.com"

    def test_go_to_revenue_page(self):
        home_page = HomePage(self.driver, self.wait)
        revenue_calculator = RevenueCalculatorpage(self.driver, self.wait)
        home_page.click_revenue_calculator()
        assert revenue_calculator.check_visiblity_of_rpm_and_ccm()

    def test_scroll_till_slider_section(self):
        revenue_calculator = RevenueCalculatorpage(self.driver, self.wait)
        slider = revenue_calculator.scroll_till_slider_section()
        assert slider

    def test_adjust_slider(self, value = 820):
        revenue_calculator = RevenueCalculatorpage(self.driver, self.wait)
        assert revenue_calculator.slide_the_slider(value)

    def test_update_the_text_field(self, value=560):
        revenue_calculator = RevenueCalculatorpage(self.driver, self.wait)
        revenue_calculator.enter_text_in_slider_text(value)
        assert revenue_calculator.check_slider_textbox_value(value)

    def test_validate_slider_value(self, slider_value=560):
        revenue_calculator = RevenueCalculatorpage(self.driver, self.wait)
        assert revenue_calculator.check_silder_value(slider_value)

    def test_select_cpt_codes(self):
        pass