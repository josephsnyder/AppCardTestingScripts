from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow

try:  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Add Inactivation").click()
  driver.find_element_by_name("edtInactivateReason").send_keys('NEW INACTIVATION REASON')
  inputElement=driver.find_element_by_name("btnGlobInactivSave").click()
  alert = driver.switch_to_alert()
  alert.accept()
  WebSignOff(driver)finally:  CloseWindow(driver)