from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow
from selenium.webdriver.support.ui import Select
import time

try:  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Inactivate Clinic").click()

  select = Select(driver.find_element_by_name("cbxInactivateReason"))
  select.select_by_visible_text(select.options[1].text)

  select = Select(driver.find_element_by_name("lbxClinic"))
  select.select_by_visible_text("VISTA HEALTH CARE")

  driver.find_element_by_name("btnClinInactivSave").click()
  alert = driver.switch_to_alert().accept()
  time.sleep(2)
  alert = driver.switch_to_alert().accept()
  WebSignOff(driver)finally:  CloseWindow(driver)