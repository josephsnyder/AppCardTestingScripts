from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



def WebSignOn(driver):
  driver.implicitly_wait(10)
  driver.get("http://localhost:57772/pcard/r1acglobLogin.csp")
  inputElement=driver.find_element_by_name("edtAccessCode")
  inputElement.send_keys("fakedoc1")
  inputElement=driver.find_element_by_name("edtVerifyCode")
  inputElement.send_keys("1Doc!@#$")
  inputElement=driver.find_element_by_name("btnLogin")
  inputElement.click()
  
def WebSignOff(driver):
  inputElement=driver.find_element(By.PARTIAL_LINK_TEXT,"Main Menu").click()
  inputElement=driver.find_element(By.PARTIAL_LINK_TEXT,"Logout").click()
  alert = driver.switch_to_alert()
  alert.accept()
  
def CloseWindow(driver):
  driver.close()