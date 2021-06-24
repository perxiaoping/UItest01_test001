from selenium.webdriver.support.wait import WebDriverWait
import allure

from tools.get_log import GetLog

log = GetLog.get_logger()


class Base:
    # 获取driver
    def __init__(self, driver):
        log.info("正在调用driver： {}".format(driver))
        self.driver = driver

    # 查找元素方法----显示等待
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在调用查找元素方法 元素为：{}".format(loc))
        """
        :param loc: 元素定位
        :param timeout: 等待最长时间
        :param poll: 查找间隔
        :return: 返回查找元素
        """
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 输入方法
    def base_input(self, loc, value):
        """
        :param loc: 元素定位
        :param value: 输入数值
        """
        # 获取元素
        el = self.base_find(loc)
        # 清空操作
        log.info("正在执行置空元素 {} 操作".format(loc))
        el.clear()
        # 输入
        log.info("正在调用输入方法 元素为：{}，输入值为：{}".format(loc, value))
        el.send_keys(value)

    # 点击方法
    def base_click(self, loc):
        log.info("正在调用点击元素 {} 方法".format(loc))
        """

        :param loc: 元素定位
        """
        self.base_find(loc).click()

    # 获取方法
    def base_get_text(self, loc):
        log.info("正在调用获取文本方法,获取的元素为 {},获取文本值为 {}".format(loc, self.base_find(loc).text))
        """

        :return: 返回获取的文本
        """
        return self.base_find(loc).text

    # 截图方法
    def base_get_img(self):
        log.error("断言出错了，正在调用截图方法")
        # 调用截图
        self.driver.get_screenshot_as_file("./image/err.png")
        log.error("正在将错误图片写入报告")
        # 调用写入报告方法
        self.__base_write_img_report()

    # 将截图写入报告方法
    def __base_write_img_report(self):
        # 获取文件流
        with open("./image/err.png", "rb") as f:
            # 使用allure的添加方法
            allure.attach("错误原因：", f.read(), allure.attachment_type.PNG)
