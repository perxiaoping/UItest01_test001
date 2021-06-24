from selenium import webdriver
import page
class GetDriver:
    # 1.设置变量
    driver = None
    # 2.获取driver
    @classmethod
    def get_driver(cls,url):
        # 判断是否为空
        if cls.driver == None:
            # 是空，设置driver
            # 获取driver
            chrome_xpath = '/Applications/Google Chrome.app/Contents/chromedriver'
            cls.driver = webdriver.Chrome(executable_path=chrome_xpath)
            # 最大化
            cls.driver.maximize_window()
            # 打开URL
            cls.driver.get(url)
        return cls.driver
    # 3.关闭driver
    @classmethod
    def quit_driver(cls):
        # 判断是否为空
        if cls.driver:
            # 不为空，关闭driver
            cls.driver.quit()
            # 置空
            cls.driver = None