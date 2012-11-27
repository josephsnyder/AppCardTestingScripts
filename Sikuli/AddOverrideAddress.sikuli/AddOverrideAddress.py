import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("AddOverrideA-2.png")
    wait("AddOverrideA-1.png",5)
    click("Selectzadivi.png")
    #
    #click on the sample division.
    click("SOFTWARESERV-1.png")
    #
    type("Streetaddres-2.png", 'Room 144')
    type("Streetaddres-3.png", '123 Main St.')
    type("Ciry.png", 'Anytown')
    type("State-1.png", 'NY')
    type("Zip-1.png", '12586')
    click(Pattern("SaveClear.png").similar(0.40).targetOffset(-27,0))
    wait("Theoverridea-1.png",5)            
    click("OK-2.png")
    wait("AddOverrideA-1.png",5)
    WebSignOff()
finally:
    ExitWindow()