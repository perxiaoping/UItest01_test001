from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog


log = GetLog.get_logger()


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        from tools.get_driver import GetDriver
        driver = GetDriver.get_driver(page.mp_url)
        # 获取统一入口类对象
        self.mp = PageIn(driver).page_mp_login()

    # 结束
    def teardown_class(self):
        GetDriver.quit_driver()

    # 调用登录业务方法
    def test_mp_login(self, code="macro123",expect="后台项目!"):
        self.mp.page_mp_login(code)
        try:
            # 断言
            assert expect == self.mp.page_get_text()
        except Exception as e:
            log.error("断言出错，输出错误信息 {}".format(e))
            # 输出错误信息
            print("错误信息为",e)
            # 截图
            self.mp.base_get_img()
            # 抛异常
            raise
