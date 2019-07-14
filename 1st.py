import time
import os
import unittest
import xlrd
import urllib3
import selenium
import traceback
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class NewToursTest(unittest.TestCase):
  driver = webdriver

  def setUp(self) :
      if(os.name =='nt'):
          self.driver=webdriver.Chrome("chromedriver.exe")
      else:
          self.driver=webdriver.Safari()

  def test_newToursLogin(self):
      driver=self.driver
      driver.set_page_load_timeout(10)
      driver.get("http://www.newtours.demoaut.com")
      driver.maximize_window()
      driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input").send_keys("mercury")
      driver.find_element_by_name("password").send_keys("mercury")
      driver.find_element_by_name("login").click()
      WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td")))
      time.sleep(5)
      element = driver.find_element_by_xpath(
          "/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/img")
      assert (element.get_attribute("src") == "http://newtours.demoaut.com/images/masts/mast_flightfinder.gif") ,"test failed"
      driver.close()

  def test_newToursLoginf(self):
          driver = self.driver
          driver.set_page_load_timeout(10)
          driver.get("http://www.newtours.demoaut.com")
          driver.maximize_window()
          driver.find_element_by_xpath(
              "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input").send_keys(
              "mercury")
          driver.find_element_by_name("password").send_keys("mercury1")
          driver.find_element_by_name("login").click()
          WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                          "/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td")))
          time.sleep(5)
          element = driver.find_element_by_xpath(
              "/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/img")
          assert (element.get_attribute(
              "src") == "http://newtours.demoaut.com/images/masts/mast_flightfinder.gif"), "test failed"
          driver.close()

  def tearDown(self):
       self.driver.quit()
    #  except:
    #    traceback.print_exc()
    #    driver.close()
    # # driver.quit()
    #
    #  else:
    #     pass
if __name__=="__main__":
    unittest.main()

