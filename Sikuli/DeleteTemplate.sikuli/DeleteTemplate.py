import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("DeleteTempla-2.png")
    wait("DeleteTempla-1.png",5)
    click("Selectatemul.png")
    click(Pattern("TESTTEIVIPIA.png").similar(0.40))
    click(Pattern("Delete.png").similar(0.50))
    wait("Readytodelet.png",5)
    click("OK.png")
    wait("Theselectedt-1.png",5)
    click("OK.png")
    wait("DeleteTempla-1.png",5)
    WebSignOff()
finally:
    ExitWindow()