from page.page_mp_login import PageMpLogin


class PageIn:
    def __init__(self,driver):
        self.driver = driver
    # 前端登录方法
    def page_mp_login(self):
        return PageMpLogin(self.driver)