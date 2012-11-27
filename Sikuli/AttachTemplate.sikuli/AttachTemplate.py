import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("AttachTempla-1.png")
    wait("AttachTempla.png")
    click("Selectzatemo.png")
    click(Pattern("TESTTEMPLATE.png").similar(0.50))
    click(Pattern("VISTAHEALTHC.png").similar(0.40))
    click("Attach.png")
    wait("Readytoattac.png",5)
    click("OK.png")
    wait("Theselectedt-1.png",5)
    click("OK.png")
    wait("AttachTempla.png")
    WebSignOff()
finally:
    ExitWindow()  