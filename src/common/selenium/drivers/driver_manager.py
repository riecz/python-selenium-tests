from selenium import webdriver
import geckodriver_autoinstaller


class DriverManager:

    def install_driver(self):
        """Install the latest Firefox webdriver."""
        geckodriver_autoinstaller.install()

    def get_driver(self):
        """Initialize and return a Firefox webdriver instance."""
        driver = webdriver.Firefox()

        print("Driver instance:", driver)
        return driver

    def close_driver(self, driver):
        """Close the provided webdriver instance."""
        if driver:
            driver.quit()
