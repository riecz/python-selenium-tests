from selenium.webdriver.common.by import By


class Locators:
    """
    Locators class provides a centralized location for all the locators
    used in the Route Builder application.
    Locators are grouped by page for better organization and clarity.
    Locators can be for buttons, text fields, tables, etc by using the
    By class. For example, "By.ID" or "By.PARTIAL_LINK_TEXT"
    """

    # Locators for the login page
    login_page = {
        "username": (By.ID, "username"),
        "password": (By.ID, "password"),
        "login_button": (By.ID, "submit")
    }

    # Locators for the home page
    home_page = {
        "loggedIn_checker":
            (By.XPATH, ".//td[contains(text(), 'Successfully')]"),
    }
