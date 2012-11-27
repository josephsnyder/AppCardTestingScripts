import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("CloneTemplat-1.png")
    wait("CloneTemplat.png",5)
    click("Selecttemple.png")
    click(Pattern("TESTTEMPLATE.png").similar(0.40))
    type(Pattern("Newtemplaten.png").similar(0.60), 'TESTTEMPLATE2')
    click(Pattern("Clone.png").similar(0.60))
    wait("Theselectedt-1.png",5)
    click("OK.png")
    wait("CloneTemplat.png",5)
    WebSignOff()
finally:
    ExitWindow()