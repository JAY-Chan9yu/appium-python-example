from appium.webdriver.common.appiumby import AppiumBy

from pages.base_pages.base import BasePage


class HomePage(BasePage):
    button_1 = (AppiumBy.ACCESSIBILITY_ID, "button_1")
    button_1_touch = (AppiumBy.ACCESSIBILITY_ID, "touch!")  # 버튼1 클릭하면 변경됨
    button_2 = (AppiumBy.ACCESSIBILITY_ID, "button_2")
    text_edit = (AppiumBy.XPATH, "//android.widget.EditText")
    check_box = (AppiumBy.XPATH, "//android.widget.CheckBox")
    switch_button = (AppiumBy.XPATH, "//android.widget.Switch")

    def click_button_1(self):
        self.click(self.button_1)

    def click_button_2(self):
        self.click(self.button_2)

    def input_text_edit(self, text: str):
        self.click(self.text_edit)
        self.send_keys(self.text_edit, text)

    def click_check_box(self):
        self.click(self.check_box)

    def click_switch_button(self):
        self.click(self.switch_button)
