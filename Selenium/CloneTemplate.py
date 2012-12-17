from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow
from selenium.webdriver.support.ui import Select

try:  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Clone Template").click()

  select = Select(driver.find_element_by_name("cbxTemplate"))
  select.select_by_index("1")

  driver.find_element_by_name("edtTemplate").send_keys("CLONETEMPLATE")

  driver.find_element_by_name("btnTempClnTempSave").click()
  driver.switch_to_alert().accept()
  driver.switch_to_default_content()

  WebSignOff(driver)finally:  CloseWindow(driver)
