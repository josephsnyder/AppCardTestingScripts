from selenium import webdriver
from selenium.webdriver.common.by import By
from libs import WebSignOn,WebSignOff,CloseWindow

try:  driver=webdriver.Firefox()
  WebSignOn(driver)
  driver.find_element(By.PARTIAL_LINK_TEXT,"Add Template").click()
  driver.find_element_by_name("edtTemplate").send_keys('TESTTEMPLATE')
  text = ['AAAAA','BBBBB','CCCCC','DDDDD','EEEEE','FFFFF','GGGGG','HHHHHH','IIIII','JJJJJ']
  var = ["01","02","03","04","05","07","08","10","12","13"]
  for i in var:
    for j in range(1,10):
      driver.find_element_by_name("edtBP"+i+"-"+str(j)).send_keys(text[var.index(i)])
  inputElement=driver.find_element_by_name("btnTempAddTempSave").click()
  alert = driver.switch_to_alert()
  alert.accept()
  WebSignOff(driver)finally:  CloseWindow(driver)