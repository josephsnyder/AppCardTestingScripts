import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("DeleteInacti-1.png")
    wait("DeleteInacti.png",5)
    click(Pattern("Selectaninac-1.png").similar(0.40))
    click(Pattern("NEWINACTIVAT.png").similar(0.40))
    click(Pattern("Delete-1.png").similar(0.50))
    wait("Readytodelet.png",5)
    click("OK.png")
    wait("inactivation-1.png",5)
    click("OK.png")
    wait("DeleteInacti.png",5)
    WebSignOff()
finally:
    ExitWindow()