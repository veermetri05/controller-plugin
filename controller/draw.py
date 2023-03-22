import os 
from xml.etree import ElementTree
from controller.builders import new_guid
def drawController(root, controllerId):
    with open("./controller.xml", 'r') as controllerXML:
        controllerLayer = ElementTree.fromstring(controllerXML.read().format(**locals()))
        root.append(controllerLayer)

