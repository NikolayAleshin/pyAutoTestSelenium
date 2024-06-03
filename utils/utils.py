import yaml
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
