from AutoDroid.common.screen_shot import getScreenShot
from AutoDroid.py_page.main_page import MainPage
from AutoDroid.common.log import Logger

logger = Logger().get_logger()


class TestLoginPage:
    def test_num_pwd_right(self, get_driver):
        try:
            name = (MainPage(
                get_driver).agree().goto_my_page().goto_login_page().switch_password_login().num_pwd_login().
                    get_user_name())
            # '//android.widget.TextView[@index="4"]'
            logger.info(f"获取用户名：{name}")
            assert name == "jxxniupi"
        except Exception as e:
            logger.error(f"执行登录用例失败，错误：{e}")
            getScreenShot(get_driver, __name__)
            raise e
