import os 
from xml.etree import ElementTree
from controller.builders import new_guid
import pkgutil

def drawController(root, controllerId):
    data = pkgutil.get_data(__name__, "statics/controller.xml").decode("utf-8").format(controllerId=controllerId)
    controllerLayer = ElementTree.fromstring(data)
    guids = controllerLayer.findall("*//*[@guid='new_guid']")
    for item in guids:
        item.attrib['guid'] = new_guid()
    root.append(controllerLayer)


def drawSliderUI(root, sliderName):
    data = pkgutil.get_data(__name__, "statics/slider.xml").decode("utf-8").format(sliderName=sliderName)
    sliderLayer = ElementTree.fromstring(data)
    guids = sliderLayer.findall("*//*[@guid='new_guid']")
    for item in guids:
        item.attrib['guid'] = new_guid()
    root.append(sliderLayer)
