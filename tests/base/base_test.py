import os
import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options

USE_DEVICE_FARM = os.getenv("use_device_farm")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class BaseTest(unittest.TestCase):
    """Basis for all tests."""

    def setUp(self):
        """
        Sets up desired capabilities and the Appium driver.

        참고: DeviceFarm에서 사용하는 경우 별도의 Capability 설정이 필요없습니다.
            로컬에서 사용하는 경우에만 정의해주세요!
        """
        desired_caps = {}

        if USE_DEVICE_FARM:
            url = "http://127.0.0.1:4723/wd/hub"
        else:
            url = "http://127.0.0.1:4723"
            desired_caps["platformName"] = "Android"
            desired_caps["deviceName"] = "emulator-5554"
            desired_caps["automationName"] = "uiautomator2"
            # 샘플앱 출처: https://goddessbest-qa.tistory.com/263 by Zeromk2
            desired_caps[
                "app"
            ] = f"{os.path.dirname(os.path.dirname(BASE_DIR))}/_sample_apps/sample.apk"

        self.driver = webdriver.Remote(
            url, options=UiAutomator2Options().load_capabilities(desired_caps)
        )

    def tearDown(self):
        """Shuts down the driver."""
        self.driver.quit()
