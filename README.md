### Selenium Testing using POM
This repository contains a comprehensive Selenium integration for testing web applications using the Page Object Model design pattern. 

In order to run tests with selenium, you either need to have a webbrowser installed on your machine and a webdriver.

If you do the development on Window, you might need to install a (Firefox) webdriver: gecko driver, found at: https://github.com/mozilla/geckodriver/releases

Beside that, simply do ``` pip install -r requirements.txt``` and the needed Selenium package will be installed.

Below are the key components related to Selenium:

#### 1. Driver Manager
The DriverManager class is responsible for initializing and managing Selenium web drivers. It supports both local and remote modes and can be configured to use different browsers like Firefox and Chrome. The driver manager reads configurations from a central config file to determine the browser preferences and modes.

#### 2. Base Page
The BasePage class serves as a foundation for all page objects. It encapsulates common web page interactions and attributes, such as finding elements and navigating to URLs.

#### 3. Login Page
The LoginPage class extends the BasePage and provides functionalities specific to the login page of the application. It includes methods to input username, password, and initiate the login process.

#### 4. Locators
The Locators class provides a centralized location for all the locators used in the application. Locators are grouped by page for better organization. This ensures that any changes in the UI can be easily updated in one place.

#### 5. Selenium Test
This file contains a test to validate the login functionality of a web application. The test navigates to the login page, inputs the credentials, and verifies successful login by checking the URL of the landing page.

#### 6. GitHub Workflows
There are two GitHub action workflows set up for running Selenium tests under ```/tests/selenium/test_selenium_pom.py``` :
- Single Browser Test Workflow: This workflow allows you to run tests on a single browser (either Firefox or Chrome) of your choice.
- Multi-Browser Test Workflow: This workflow runs tests on multiple browsers (Firefox and Chrome) simultaneously.

