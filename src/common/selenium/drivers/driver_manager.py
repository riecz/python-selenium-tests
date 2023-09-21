from selenium import webdriver
from selenium.webdriver import FirefoxOptions


class DriverManager:

    options = FirefoxOptions()
    options.browser_name = "firefox"

    def get_driver(self):
        """Initialize and return a Firefox webdriver instance."""
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=self.options
        )
        # driver = webdriver.Firefox()

        print("Driver instance:", driver)
        return driver

    def close_driver(self, driver):
        """Close the provided webdriver instance."""
        if driver:
            driver.quit()
