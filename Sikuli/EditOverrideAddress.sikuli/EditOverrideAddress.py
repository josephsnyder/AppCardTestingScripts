import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("EditOverride-2.png")
    wait("EditOverride-1.png",5)
    click("Selectzadivi.png")
    click(Pattern("SOEIWARESERV.png").similar(0.50))
    doubleClick("Room144Stree.png")
    type("155 ")
    click("Save-1.png")
    wait("Theoverridea.png",5)
    click("OK.png")
    wait("EditOverride-1.png",5)
    WebSignOff()
finally:
    ExitWindow()