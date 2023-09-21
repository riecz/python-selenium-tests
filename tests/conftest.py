# '''
# The function in this file will run before the tests are run.
# Add all pre-execution logic into that function
# '''
import pytest
from src.common.selenium.drivers.driver_manager import DriverManager


@pytest.fixture(scope="function")
def driver():
    driver_manager = DriverManager()
    driver_instance = driver_manager.get_driver()
    yield driver_instance
    driver_manager.close_driver(driver_instance)
