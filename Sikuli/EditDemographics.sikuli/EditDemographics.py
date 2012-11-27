import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    click("EditDemograp-1.png")
    wait("EditDemograp.png",5)
    click(Pattern("Selectzaclin.png").similar(0.50))
    click(Pattern("VISTAHEALTHC.png").similar(0.40))
    type("Friendlyname-1.png", "VistA Outpatient")
    type("Cliniclocati-1.png", "Bldg 214")
    type("Streetaddres-1.png", "154 Main St.")
    type("CityStateZip-1.png", "Anytown, NY 12014")
    click(Pattern("Save.png").similar(0.50))
    wait("Clinicdemogr.png",5)
    type("\r")
    wait("EditDemograp.png",5)
    WebSignOff()
finally:
    ExitWindow()