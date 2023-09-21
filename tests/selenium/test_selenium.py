from selenium.webdriver.common.by import By


# Configuration values for the tests
page_url = "https://practicetestautomation.com/practice-test-login/"
home_page_url = "https://practicetestautomation.com/logged-in-successfully/"
username = "student"
password = "Password123"
login_page_locators = {
    "username": (By.ID, "username"),
    "password": (By.ID, "password"),
    "login_button": (By.ID, "submit")
}


def test_login(driver):
    """
    Test the login functionality.
    """
    print("Testing login functionality...")
    driver.get(page_url)
    username_locator = login_page_locators["username"]
    password_locator = login_page_locators["password"]
    login_button_locator = login_page_locators["login_button"]
    driver.save_screenshot("screenshots/step1.png")
    driver.find_element(*username_locator).send_keys(username)
    driver.find_element(*password_locator).send_keys(password)
    driver.save_screenshot("screenshots/step2.png")
    driver.find_element(*login_button_locator).click()
    driver.save_screenshot("screenshots/step3.png")
    assert driver.current_url == home_page_url
    print("Login test passed!")
