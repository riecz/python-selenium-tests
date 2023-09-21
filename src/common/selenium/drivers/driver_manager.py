from selenium import webdriver


class DriverManager:

    def get_driver(self):
        """Initialize and return a Firefox webdriver instance."""
        driver = webdriver.Firefox()
        print("Driver instance:", driver)
        return driver

    def close_driver(self, driver):
        """Close the provided webdriver instance."""
        if driver:
            driver.quit()
