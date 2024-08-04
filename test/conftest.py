from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='class')
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument('--disable-save-password-bubble')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    service_obj = Service(executable_path=ChromeDriverManager().install())
    # service_obj = Service(r'C:\Users\dines\MedDream\Drivers\chromedriver.exe')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.get("https://fitpeo.com/")
    wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()
    driver.quit()
