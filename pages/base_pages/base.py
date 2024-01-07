from typing import Tuple

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """The basis for all pages."""

    IMPLICIT_WAIT_TIME = 10
    TIMEOUT = 30

    def __init__(self, driver):
        """
        Base constructor.
        Sets driver, implicit wait, and timeout.
        """
        self.driver = driver
        self.driver.implicitly_wait(self.IMPLICIT_WAIT_TIME)
        self.timeout = self.TIMEOUT

    def click(self, by_locator: Tuple[str, str], timeout: int = 10):
        return (
            WebDriverWait(self.driver, timeout)
            .until(expected_conditions.visibility_of_element_located(by_locator))
            .click()
        )

    def get_element(self, by_locator: Tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )

    def send_keys(self, by_locator: Tuple[str, str], text: str):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)
        ).send_keys(text)
