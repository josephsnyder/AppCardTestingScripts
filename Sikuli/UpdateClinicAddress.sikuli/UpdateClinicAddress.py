import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo-1.png",5)
    click("UpdateClinic.png")
    wait("UndatcClinic.png",5)
    click(Pattern("Thisaddress.png").targetOffset(-42,0))
    type(Pattern("StreetAddres.png").targetOffset(0,9),'155 MAIN ST')
    type(Pattern("CityStateZip.png").targetOffset(0,9),'Anytown, NY 12101')         
    click("VISTAHEALTHC.png")
    click("Update.png")    
    wait("Readytoupdat.png",5)
    click("OK.png")
    wait("Theaddresses.png",5)
    click("OK.png")
    wait("UndatcClinic.png",5)
    click(Pattern("Divisionaddr.png").targetOffset(-59,-1))
    click("VISTAHEALTHC.png")
    click("Update.png")    
    wait("Readytoupdat.png",5)
    click("OK.png")
    wait("Theaddresses.png",5)
    click("OK.png")
    WebSignOff()
finally:
    ExitWindow()