from src.common.selenium.pages.login_page import LoginPage
from src.config import config

# Configuration values for the tests
page_url = config["url"]
home_page_url = "https://practicetestautomation.com/logged-in-successfully/"


def test_login(driver):
    """
    Test the login functionality.
    """
    print("Testing login functionality...")
    login_page = LoginPage(driver)
    login_page.login()
    assert driver.current_url == home_page_url
    print("Login test passed!")
