import time

from selenium.webdriver.common.by import By
from AutoDroid.common.log import Logger

'''
basepage.find/finds 方法的装饰器，用于处理黑名单弹框，保证业务进行
'''
logging = Logger(__name__).get_logger()


def handle_black(fun):  # fun == find
    def run(*args, **kwargs):
        # args = (self, by, locator)
        # 黑名单列表
        black_list = [(By.XPATH, "//android.widget.ImageView[@content-desc='Close']"),
                      (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"),
                      (By.ID, "com.android.permissioncontroller:id/permission_allow_button")]
        by_self = args[0]  # args->(self,by,locator)  args[0]->self
        try:
            # 如果找到对象就把对象返回
            ele = fun(*args, **kwargs)  # find/finds  调用find/finds来定位元素
            return ele
        except Exception as e:

            # 如果没有找到对象就遍历黑名单列表
            for black in black_list:
                logging.info(f"在黑名单中查找元素{black}")
                eles = by_self.driver.find_elements(*black)  # find_elements返回的是一个列表

                # 如果黑名单中的元素存在，就对该元素进行处理
                if len(eles) > 0:
                    eles[0].click()
                    time.sleep(1)
                    logging.info(f"查找到黑名单元素{black}，并对该元素进行处理")
                    ele = fun(*args, **kwargs)
                    return ele
                else:
                    logging.info(f"在黑名单中元素{black}未在页面中定位到")
            raise e

    return run


if __name__ == '__main__':
    ...
# res1 = handle_black("func")
# # res1 = run
# res2 = res1("参数1", "参数2")
# # res2 = func("参数1", "参数2")
