import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("DeleteOverri-2.png")
    wait("DeleteOverri-1.png",5)
    click("Selectzadivi.png")
    click(Pattern("SOETVVARESER.png").similar(0.40))
    click(Pattern("Delete-1.png").similar(0.50))
    wait("Readvtodelet.png",5)
    click("OK-1.png")
    wait("Theoverridea-1.png",5)
    click("OK-1.png")
    wait("DeleteOverri-1.png",5)
    WebSignOff()
finally:
    ExitWindow()