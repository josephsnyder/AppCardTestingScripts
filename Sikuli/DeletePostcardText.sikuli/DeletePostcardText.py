import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("DeletePostca-2.png")
    wait("DeletePostca-1.png",5)
    click(Pattern("VISTAHEALTHC.png").similar(0.40))
    click(Pattern("Delete.png").similar(0.50))
    wait("Readytodelet.png",5)
    click("OK-1.png")
    wait("Thepostcardt-1.png",10)
    click("OK-1.png")
    wait("DeletePostca-1.png",5)
    WebSignOff()
finally:
    ExitWindow()