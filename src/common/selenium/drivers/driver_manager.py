from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver import FirefoxOptions


class DriverManager:

    options = FirefoxOptions()
    options.browser_name = "firefox"

    def install_driver(self):
        """Install the latest Firefox webdriver."""
        geckodriver_autoinstaller.install()

    def get_driver(self):
        """Initialize and return a Firefox webdriver instance."""
        driver = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            options=self.options
        )
        # driver = webdriver.Firefox()

        print("Driver instance:", driver)
        return driver

    def close_driver(self, driver):
        """Close the provided webdriver instance."""
        if driver:
            driver.quit()
