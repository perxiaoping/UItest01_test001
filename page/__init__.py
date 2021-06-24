from selenium.webdriver.common.by import By
# Url
mp_url = "http://www.macrozheng.com/admin/#/login"
# mp_login的page页面元素
mp_login_pwd = By.CSS_SELECTOR,"[name='password']"
mp_login_btn = By.CSS_SELECTOR,".el-button--primary"
mp_login_text = By.CSS_SELECTOR,".layout-title"