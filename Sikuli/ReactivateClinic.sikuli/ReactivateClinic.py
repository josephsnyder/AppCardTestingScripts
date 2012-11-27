import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("ReactivateCl-2.png")
    wait("ReactivateCl-1.png",5)
    click("Selectaninac.png")
    click(Pattern("NEWINACTIVAT.png").similar(0.40))
    click(Pattern("VISTAHEALTHC.png").similar(0.40))
    click("Reactivate.png")
    wait("Readytoreact.png",5)
    click("OK.png")
    wait("Theselectedc-1.png",5)
    click("OK.png")
    wait("ReactivateCl-1.png",5)
    WebSignOff()
finally:
    ExitWindow()