import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("InactivateCl.png")
    wait("IuactivateCl.png",5)
    click("Selectaninac.png")
    click(Pattern("NEWINACTIVAT.png").similar(0.40))
    click(Pattern("VISTAHEALTHC.png").similar(0.40))
    click(Pattern("Inactivate.png").similar(0.50))
    wait("Readytoinact.png",5)
    click("OK.png")
    wait("Theselectedc-1.png",5)
    click("OK.png")
    wait("IuactivateCl.png",5)
    WebSignOff()
finally:
    ExitWindow()