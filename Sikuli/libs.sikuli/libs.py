import os
from sikuli import *
def WebSignOn():
  try:
      openApp("C:/Program Files (x86)/Mozilla Firefox/firefox.exe")
  except:
      raise FindFailed("Browser not found")
  wait("VistALogin-1.png",30)
  type(Pattern("AccessCode-1.png").similar(0.60), 'fakedoc1')
  type(Pattern("VAVerifyCode-1.png").similar(0.40).targetOffset(30,0), '1Doc!@#$\r')
  
def WebSignOff():
    type(Key.PAGE_DOWN)
    wait(2)
    links = ["MainMenu-3.png","MainMenu.png"]
    for value in range(0,2):
        try:
            click(links[value])
        except:
            continue
    wait("MainMenu-2.png",5)
    click("LogoutofVist-1.png")
    wait("LogoutofVis.png")
    click("OK-2.png")
    wait(5)
    sys.exit(0)

def ExitWindow():
    type("f",KeyModifier.ALT)
    type("x")
