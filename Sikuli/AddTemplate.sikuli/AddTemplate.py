import sys
from libs import *

try:
    WebSignOn()
    wait("ppoiutmentPo.png",5)
    import sys
    wait("MainMenu-2.png",5)
    click("AddTemglate.png")
    wait("AddTemplate.png",5)
    type("Templatename-1.png", 'TESTTEMPLATE')
    region = [Region(17,424,520,306),Region(16,83,520,300),Region(16,83,520,300),Region(16,83,520,300),Region(16,83,520,300),Region(16,83,520,300),Region(16,83,520,300),Region(16,83,520,300),Region(16,83,520,300),Region(16,83,520,300),Region(16,83,520,300),Region(16,83,520,300)]
    text = ['AAAAA','BBBBB','CCCCC','DDDDD','EEEEE','FFFFF','GGGGG','HHHHHH','IIIII','JJJJJ']
    templatejump=[Pattern("OuickJumnlle.png").similar(0.40).targetOffset(-100,0),Pattern("OuickJumnlle.png").similar(0.40).targetOffset(0,-2),Pattern("OuickJumnlle.png").similar(0.40).targetOffset(100,0),Pattern("OuickJumnlle.png").similar(0.40).targetOffset(200,0),Pattern("OuickJumnlle.png").similar(0.40).targetOffset(-200,25),Pattern("OuickJumnlle.png").similar(0.40).targetOffset(-100,25),Pattern("OuickJumnlle.png").similar(0.40).targetOffset(0,25),Pattern("OuickJumnlle.png").similar(0.40).targetOffset(100,25),Pattern("OuickJumnlle.png").similar(0.40).targetOffset(200,25)]
    for value in range(0,10):
        with region[value].findAll("1351604870518.png") as template:
            while template.hasNext():
                region[value].type(template.next(),text[value])
            if value < 9:
                click(templatejump[value])
    click("Save.png")
    wait("Thetemolateh.png",5)
    click("OK.png")
    wait("AddTemplate-1.png")
    click("Bottom-1.png")
    WebSignOff()
finally:
    ExitWindow()