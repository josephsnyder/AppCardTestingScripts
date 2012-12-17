from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow
from selenium.webdriver.support.ui import Select
import time

try:
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Delete Inactivation Reason").click()

  select = Select(driver.find_element_by_name("cbxInactivateReason"))
  select.select_by_visible_text(select.options[1].text)


  driver.find_element_by_name("btnGlobInactivDele").click()
  alert = driver.switch_to_alert().accept()
  time.sleep(2)
  alert = driver.switch_to_alert().accept()
  WebSignOff(driver)