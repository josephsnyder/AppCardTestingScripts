import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("DetachTempla-1.png")
    wait("DetachTempla.png",5)
    click("Selectatemul.png")
    click(Pattern("TESTTEMPLATE.png").similar(0.40))
    wait(Pattern("VISTAHEALTHC.png").similar(0.40),5)
    click(Pattern("VISTAHEALTHC.png").similar(0.40))
    click("Detach-1.png")
    wait("Readytodetac.png",5)
    click("OK.png")
    wait("Theselectedt-1.png",5)
    click("OK.png")
    wait("DetachTempla.png",5)
    WebSignOff()
finally:
    ExitWindow()