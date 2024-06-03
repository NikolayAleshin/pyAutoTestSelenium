import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from utils.wait_utils import wait_for_page_to_load


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--verbose')
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')  # Set window size to 1920x1080

    # Specify the path to the ChromeDriver binary
    service = ChromeService(executable_path='/usr/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(30)
    wait_for_page_to_load(driver)
    yield driver
    driver.quit()
