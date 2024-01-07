import time

from pages.home import HomePage
from tests.base.base_test import BaseTest


class Test_메인_홈_페이지(BaseTest):
    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)

    def test_홈_페이지_각종_버튼을_클릭한다(self):
        self.assert_button1_클릭하면_버튼_라벨이_touch_로_변경된다()
        self.home_page.click_button_2()
        self.home_page.input_text_edit("오우! 테스트 자동화 개꿀!!")
        self.home_page.click_check_box()
        self.home_page.click_switch_button()
        time.sleep(5)  # 잠시 확인을 위해

    def assert_button1_클릭하면_버튼_라벨이_touch_로_변경된다(self):
        self.home_page.click_button_1()
        time.sleep(1)
        self.home_page.get_element(self.home_page.button_1_touch)
