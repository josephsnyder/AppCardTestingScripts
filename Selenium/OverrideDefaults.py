from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow
from selenium.webdriver.support.ui import Select

try:  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Override Defaults").click()

  select = Select(driver.find_element_by_name("cbxPostCard"))
  select.select_by_value("10")

  select = Select(driver.find_element_by_name("cbxStopCode"))
  select.select_by_value("280")

  driver.find_element_by_name("edtClinNameMatch").send_keys("VISTA HEALTH CARE")

  driver.find_element_by_name("btnPostOverDefSave").click()
  driver.switch_to_alert().accept()
  driver.switch_to_default_content()
  WebSignOff(driver)finally:  CloseWindow(driver)