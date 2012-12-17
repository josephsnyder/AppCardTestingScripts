from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow
from selenium.webdriver.support.ui import Select

try:
  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Edit Demographics").click()

  select = Select(driver.find_element_by_name("cbxClinic"))
  select.select_by_index(3)
  driver.find_element_by_name("edtFriendlyName").send_keys("VISTA Medical")
  driver.find_element_by_name("edtStreetAddress").send_keys("123 Main St.")
  driver.find_element_by_name("edtCityStateZip").send_keys("ANYTOWN, NY 1285")

  driver.find_element_by_name("btnClinDemoEdtSave").click()
  alert = driver.switch_to_alert()
  alert.accept()
  WebSignOff(driver)
finally:
  CloseWindow(driver)
