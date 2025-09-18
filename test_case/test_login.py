from common.screen_shot import getScreenShot
from py_page.main_page import MainPage
from common.log import Logger
from appium.webdriver.common.appiumby import AppiumBy

logger = Logger().get_logger()


class TestLoginPage:
    def test_num_pwd_right(self, get_driver):
        try:
            name, text = (MainPage(
                get_driver).agree().goto_my_page().goto_login_page().switch_password_login().num_pwd_login(
                "15371972593", "jxx321").xbg_agree().
                          get_user_name())

            # '//android.widget.TextView[@index="4"]'
            logger.info(f"获取用户名：{name}")
            logger.info(f"获取到提示：{text}")
            assert (text, name) == ("登录成功", "jxx")
        except Exception as e:
            logger.error(f"执行登录用例失败，错误：{e}")
            getScreenShot(get_driver, __name__)
            raise e

    def test_num_pwd_wrong(self, get_driver):
        try:
            text = (MainPage(
                get_driver).agree().goto_my_page().goto_login_page().switch_password_login().num_pwd_login(
                "15371972593", "jxx31").xbg_agree().my_page_toast_text())

            # '//android.widget.TextView[@index="4"]'
            logger.info(f"获取到提示：{text}")
            assert text == "用户名或密码错误"
        except Exception as e:
            logger.error(f"执行登录用例失败，错误：{e}")
            getScreenShot(get_driver, __name__)
            raise e

    def test_num_wrong_pwd(self, get_driver):
        try:
            text = (MainPage(
                get_driver).agree().goto_my_page().goto_login_page().switch_password_login().num_pwd_login(
                "15371972", "jxx31").xbg_agree().my_page_toast_text())

            # '//android.widget.TextView[@index="4"]'
            logger.info(f"获取到提示：{text}")
            assert text == "用户名或密码错误"
        except Exception as e:
            logger.error(f"执行登录用例失败，错误：{e}")
            getScreenShot(get_driver, __name__)
            raise e

    def test_num_none_pwd(self, get_driver):
        try:
            text = (MainPage(
                get_driver).agree().goto_my_page().goto_login_page().switch_password_login().num_pwd_login(
                "", "jxx31").is_button_enabled())

            # '//android.widget.TextView[@index="4"]'
            logger.info(f"获取到提示：{text}")
            assert text == "false"
        except Exception as e:
            logger.error(f"执行登录用例失败，错误：{e}")
            getScreenShot(get_driver, __name__)
            raise e

    def test_num_pwd_none(self, get_driver):
        try:
            text = (MainPage(
                get_driver).agree().goto_my_page().goto_login_page().switch_password_login().num_pwd_login(
                "15371972593", "").is_button_enabled())

            # '//android.widget.TextView[@index="4"]'
            logger.info(f"获取到提示：{text}")
            assert text == "false"
        except Exception as e:
            logger.error(f"执行登录用例失败，错误：{e}")
            getScreenShot(get_driver, __name__)
            raise e

    def test_num_pwd_none(self, get_driver):
        try:
            text = (MainPage(
                get_driver).agree().goto_my_page().goto_login_page().switch_password_login().num_pwd_login(
                "15371972593", "").is_button_enabled())

            # '//android.widget.TextView[@index="4"]'
            logger.info(f"获取到提示：{text}")
            assert text == "false"
        except Exception as e:
            logger.error(f"执行登录用例失败，错误：{e}")
            getScreenShot(get_driver, __name__)
            raise e

    def test_num_pwd_all_none(self, get_driver):
        try:
            text = (MainPage(
                get_driver).agree().goto_my_page().goto_login_page().switch_password_login().num_pwd_login(
                "", "").is_button_enabled())

            # '//android.widget.TextView[@index="4"]'
            logger.info(f"获取到提示：{text}")
            assert text == "false"
        except Exception as e:
            logger.error(f"执行登录用例失败，错误：{e}")
            getScreenShot(get_driver, __name__)
            raise e
