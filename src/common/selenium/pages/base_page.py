class BasePage:
    """
    BasePage serves as a foundation for all page objects.
    It encapsulates common web page interactions and attributes.
    """

    def __init__(self, driver):
        """
        Initializes the BasePage instance.
        """
        self.driver = driver

    def find_element(self, *locator):
        """
        Finds an element on the page using the provided locator.
        """
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        """
        Finds multiple elements on the page using the provided locator.
        """
        return self.driver.find_elements(*locator)

    def navigate_to(self, url):
        """
        Navigates to the specified URL.
        """
        self.driver.get(url)

    def navigate_to_by_element(self, locator):
        """
        Navigates to a page by clicking on an element identified
        by the provided locator.
        """
        self.find_element(*locator).click()
