import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("DeleteClinic-2.png")
    wait("DeleteClinic-1.png",5)
    click(Pattern("VISTAHEALTHC.png").similar(0.40))
    click("Delete-1.png")
    wait("Readytodelet-1.png",5)
    click("OK.png")
    wait("Theselectedc-1.png",5)
    type("\r")
    wait("DeleteClinic-1.png",5)
    WebSignOff()
finally:
    ExitWindow()