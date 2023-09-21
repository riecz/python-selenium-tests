from src.common.selenium.pages.login_page import LoginPage
from src.common.selenium.resources.locators import Locators


class PageObjects:
    """
     Page objects forbase test of the Route Builder application.
     This class contains the web elements used by the tests.
    """

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.login_page_locators = Locators.login_page


class BaseTest:
    """
    Base test class for the Route Builder application.
    This class contains the common methods used by all tests.
    """

    def __init__(self, driver):
        # Initialize the web driver and set up the page objects for the test
        self.driver = driver
        self.pages = PageObjects(driver)
