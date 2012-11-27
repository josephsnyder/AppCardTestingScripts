import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("OverrideDefa-2.png")
    wait("OverrideDefa-1.png",5)
    click(Pattern("Selectaoostc.png").similar(0.50))
    click(Pattern("APPIBring3.png").similar(0.50))
    click(Pattern("Blank.png").similar(0.50))
    click(Pattern("AUDIOLOGY203.png").similar(0.50))
    type("Clinicnamema-1.png", "VistA Health Care")
    click(Pattern("Save-1.png").similar(0.50))
    wait("Theoverrided-1.png",5)
    click("OK.png")
    wait("OverrideDefa-1.png",5)
    WebSignOff()
finally:
    ExitWindow()