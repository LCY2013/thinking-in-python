from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get('https://movie.douban.com/subject/1292052/')
    time.sleep(1)

    btml = browser.find_element(By.XPATH, '//*[@id="hot-comments"]/a')
    btml.click()
    time.sleep(10)
    print(browser.page_source)
except Exception as e:
    print(e)
finally:
    browser.close()
