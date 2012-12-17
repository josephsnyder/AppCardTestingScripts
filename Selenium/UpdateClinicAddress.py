from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow
from selenium.webdriver.support.ui import Select
import time

try:
  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Update Clinic Address").click()
  
  
  driver.find_element_by_name("rbtAddressType").click()
  select = Select(driver.find_element_by_name("lbxClinic"))
  select.select_by_visible_text("VISTA HEALTH CARE")
  driver.find_element_by_name("btnClinUpdateAddrs").click()
  alert = driver.switch_to_alert().accept()
  time.sleep(2)
  alert = driver.switch_to_alert().accept()

  # driver.find_element_by_name("edtStreetAddress").send_keys("123 Main St.")
  # driver.find_element_by_name("edtCityStateZip").send_keys("ANYTOWN, NY 12852")
  # select = Select(driver.find_element_by_name("lbxClinic"))
  # select.select_by_visible_text("VISTA HEALTH CARE")
  
  # driver.find_element_by_name("btnClinUpdateAddrs").click()
  # alert = driver.switch_to_alert().accept()
  # time.sleep(2)
  # alert = driver.switch_to_alert().accept()
  WebSignOff(driver)
finally:
  CloseWindow(driver)
