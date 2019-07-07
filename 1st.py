import time
import xlrd
import urllib3

from selenium import webdriver

driver = webdriver.Safari()

driver.set_page_load_timeout(10)
driver.get("https://www.google.com")
driver.fullscreen_window()
driver.find_element_by_name("q").send_keys("hello")
driver.minimize_window()
time.sleep(2000)
#driver.implicitly_wait(1000)
driver.quit()