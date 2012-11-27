import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("SiteParamete-2.png")
    wait("SiteParamete-1.png",5)
    doubleClick("DefaultHstAl.png")
    type("Cloneclinics-1.png", "DEFG")
    click(Pattern("Save.png").similar(0.50))
    wait("Thesiteparam-1.png",5)
    click("OK.png")
    wait("SiteParamete-1.png",5)
    WebSignOff()
finally:
    ExitWindow()