from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    # https://googlechromelabs.github.io/chrome-for-testing/

    browser.get('https://www.douban.com')
    time.sleep(1)

    browser.switch_to.frame(browser.find_elements(By.TAG_NAME, 'iframe')[0])
    btml = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]')
    btml.click()

    browser.find_element(By.XPATH, '//*[@id="username"]').send_keys('15055495@qq.com')
    browser.find_element(By.ID, 'password').send_keys('test123test456')
    time.sleep(1)
    browser.find_element(By.XPATH, '//a[contains(@class,"btn-account")]').click()

    # 获取cookies
    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()
