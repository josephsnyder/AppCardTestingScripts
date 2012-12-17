from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow
from selenium.webdriver.support.ui import Select

try:  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Site Parameters").click()

  driver.find_element_by_name("edtClonClinSkipFlds").send_keys("K")

  driver.find_element_by_name("btnGlobSiteParSave").click()
  driver.switch_to_alert().accept()
  driver.switch_to_default_content()

  WebSignOff(driver)finally:  CloseWindow(driver)