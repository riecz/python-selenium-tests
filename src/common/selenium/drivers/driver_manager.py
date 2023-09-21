from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions
from dotenv import load_dotenv
import os


class DriverManager:
    load_dotenv()

    def __init__(self):
        self.browser_name = os.environ["BROWSER"]

    def get_driver(self):
        """Initialize and return a webdriver instance based on the browser name."""
        if self.browser_name == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=options
            )
        elif self.browser_name == "chrome":
            options = ChromeOptions()
            driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=options
            )
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

        print("Driver instance:", driver)
        return driver

    def get_driver_local(self):
        if self.browser_name == "firefox":
            driver = webdriver.Firefox()
        elif self.browser_name == "chrome":
            driver = webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")
        print("Driver instance:", driver)
        return driver

    def close_driver(self, driver):
        """Close the provided webdriver instance."""
        if driver:
            driver.quit()
