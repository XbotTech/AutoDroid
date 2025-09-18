from AutoDroid.py_page.base_page import BasePage



class LoginPage(BasePage):
    yaml_path = BasePage.get_yaml_path("login_page.yaml")

    # 手机号号密码登录
    def num_pwd_login(self):
        self.run_steps(self.yaml_path, "num_pwd_login")
        from AutoDroid.py_page.my_page import MyPage
        return MyPage(self.driver)

    def switch_password_login(self):
        self.run_steps(self.yaml_path, "switch_password_login")
        return self

