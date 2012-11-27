import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo-1.png",5)
    click("AddInactivat.png")
    wait("AddInactivat-1.png",5)
    type(Pattern("Newinactivat.png").similar(0.60),'NEW INACTIVATION REASON')
    click(Pattern("Save.png").similar(0.60))
    wait("Inactivation-1.png",5)
    click("OK.png")
    wait("AddInactivat-1.png",5)
    WebSignOff()
finally:
    ExitWindow()