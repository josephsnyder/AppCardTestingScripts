from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow
from selenium.webdriver.support.ui import Select

try:  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Edit Override Address").click()

  select = Select(driver.find_element_by_name("cbxInstitution"))
  select.select_by_value("1")

  driver.find_element_by_name("edtAddress1").send_keys("5")
  driver.find_element_by_name("btnPostOverAddSave").click()
  alert = driver.switch_to_alert()
  alert.accept()
  driver.switch_to_default_content()

  WebSignOff(driver)finally:  CloseWindow(driver)