from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow
from selenium.webdriver.support.ui import Select

try:  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Add Override Address").click()

  select = Select(driver.find_element_by_tag_name("select"))
  select.select_by_visible_text(select.options[1].text)
  driver.find_element_by_name("edtAddress1").send_keys("Room 144")
  driver.find_element_by_name("edtAddress2").send_keys("123 Main St.")
  driver.find_element_by_name("edtCity").send_keys("ANYTOWN")
  driver.find_element_by_name("edtState").send_keys("NY")
  driver.find_element_by_name("edtZip").send_keys("12385")

  driver.find_element_by_name("btnPostOverAddSave").click()
  alert = driver.switch_to_alert()
  alert.accept()
  WebSignOff(driver)finally:  CloseWindow(driver)
