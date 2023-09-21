# '''
# The function in this file will run before the tests are run.
# Add all pre-execution logic into that function
# '''
import pytest
from src.common.selenium.drivers.driver_manager import DriverManager
from src.config import config


@pytest.fixture(scope="function")
def driver():
    is_local = config["isLocal"]
    driver_manager = DriverManager()
    if is_local:
        driver_instance = driver_manager.get_driver_local()
    else:
        driver_instance = driver_manager.get_driver()
    yield driver_instance
    driver_manager.close_driver(driver_instance)
