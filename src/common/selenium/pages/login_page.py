from .base_page import BasePage
from src.common.selenium.resources.locators import Locators
from src.config import config


class LoginPage(BasePage):
    base_url = config["url"]
    username = config["username"]
    password = config["password"]

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(self.base_url)
        self.username_locator = Locators.login_page["username"]
        self.password_locator = Locators.login_page["password"]
        self.login_button_locator = Locators.login_page["login_button"]

    def login(self):
        """Login to the application."""
        self.find_element(*self.username_locator).send_keys(self.username)
        self.find_element(*self.password_locator).send_keys(self.password)
        self.find_element(*self.login_button_locator).click()
