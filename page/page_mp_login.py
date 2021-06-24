import page
from base.base import Base
from time import sleep

from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpLogin(Base):
    # 输入账户（可忽略）
    def page_input_username(self):
        pass

    # 输入密码
    def page_input_pwd(self, code):
        self.base_input(page.mp_login_pwd, code)

    # 点击登录
    def page_click_login(self):
        self.base_click(page.mp_login_btn)

    # 获取文本
    def page_get_text(self):
        return self.base_get_text(page.mp_login_text)

    # 组合方法
    def page_mp_login(self, code):
        log.info("正在调用登录方法，密码为{}".format(code))
        self.page_input_pwd(code)
        sleep(1)
        self.page_click_login()
