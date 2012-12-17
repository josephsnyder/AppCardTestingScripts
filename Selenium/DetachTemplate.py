from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow
from selenium.webdriver.support.ui import Select,WebDriverWait
import time

try:  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Detach Template").click()

  select = Select(driver.find_element_by_name("cbxTemplate"))
  select.select_by_visible_text("TESTTEMPLATE")

  select = Select(driver.find_element_by_name("lbxClinic"))
  select.select_by_visible_text("VISTA HEALTH CARE")

  driver.find_element_by_name("btnClinDttTempSave").click()
  alert = driver.switch_to_alert().accept()
  time.sleep(2)
  alert = driver.switch_to_alert().accept()

  WebSignOff(driver)finally:  CloseWindow(driver)