
import math
import random
from controller.builders import createAdd, createNode, createReal, createScale, getDefs
from controller.draw import drawSliderUI
from controller.const import nodeTypes

def createAdditions(valuesToAdd,  controllerIds, nodeType):
    for i in range(1, len(valuesToAdd)):
        if nodeType == 'real' or nodeType == "angle": 
            valuesToAdd[i] = valuesToAdd[i] - valuesToAdd[0]
        if nodeType == "vector":
                valuesToAdd[i] = [valuesToAdd[i][0] - valuesToAdd[0][0], valuesToAdd[i][1] - valuesToAdd[0][1]]
        if nodeType == "color":
                valuesToAdd[i] = [valuesToAdd[i][j] - valuesToAdd[0][j] for j in range(4)]
    addConvertedList = []
    if nodeType == "real" or nodeType == "angle":
        baseValue = createNode(valuesToAdd[0], nodeType)
    elif nodeType == "vector":
        baseValue = createNode(
            (valuesToAdd[0][0], valuesToAdd[0][1]), nodeType)
    elif nodeType == "color":
            baseValue = createNode(
                (valuesToAdd[0][0], valuesToAdd[0][1], valuesToAdd[0][2], valuesToAdd[0][3]), nodeType)
    addConvertedList.append(baseValue)
    for i in range(1, len(valuesToAdd)):
        if nodeType == "real" or nodeType == "angle":
                baseValue = createNode(valuesToAdd[i], nodeType)
        elif nodeType == "vector":
                baseValue = createNode(
                    (valuesToAdd[i][0], valuesToAdd[i][1]), nodeType)
        elif nodeType == "color":
                baseValue = createNode(
                    (valuesToAdd[i][0], valuesToAdd[i][1], valuesToAdd[i][2], valuesToAdd[i][3]), nodeType)
        toLinkValue = createNode(valuesToAdd[i], nodeType)
        addConvertedList.append(createScale(
            type=nodeType, toLink=toLinkValue, scalarLinkExported=controllerIds[i-1]))
    while (len(addConvertedList) >= 2):
        for i in range(math.ceil(len(addConvertedList)/2)):
            try:
                addConvertedList[i] = createAdd(
                    lhsLink=addConvertedList[i*2], rhsLink=addConvertedList[(i*2)+1], scalarLink=createReal("1.0"), type=nodeType)
            except:
                addConvertedList[i] = addConvertedList[i*2]
        for i in range(len(addConvertedList) - math.ceil(len(addConvertedList)/2)):
            del addConvertedList[-1]
    return addConvertedList[0]


def connectSlider(parentsToConnect, nodeType, controllerIdsList):
        for parent in parentsToConnect:
            animated = parent[0]
            valuesToPass = []
            for waypoint in animated:
                if nodeType == "real" or nodeType == "angle":
                        valuesToPass.append(
                            float(list(waypoint)[0].attrib['value']))
                if nodeType == "vector":
                        valuesToPass.append([float(list(list(waypoint)[0])[0].text), float(
                            list(list(waypoint)[0])[1].text)])
                if nodeType == "color":
                        valuesToPass.append([float(list(list(waypoint)[0])[0].text), float(list(list(waypoint)[0])[
                                            1].text), float(list(list(waypoint)[0])[2].text), float(list(list(waypoint)[0])[3].text)])
            for i in parent:
                parent.remove(i)
            print(valuesToPass)
            parent.append(createAdditions(valuesToPass, controllerIdsList, nodeType))


def generateSlider(fileRoot,  layer ):
        exportedDefs = getDefs(fileRoot)
        controllerIdsList = []
        animatedAtUniqueTime = set({})
        for nodeType in nodeTypes:
            animatedElements = layer.findall(f".//*/animated[@type='{nodeType}']/..")
            for parent in animatedElements:
                animated = parent[0]
                for waypoint in animated:
                     waypointTime = waypoint.attrib['time']    
                     animatedAtUniqueTime.add(waypointTime)
        for _ in range(len(animatedAtUniqueTime) - 1):
            sliderId = "Slider " + \
            layer.attrib['desc']         + "_" + str(random.randint(1000, 9999))
            controllerIdsList.append(sliderId)
            exportedDefs.append(createReal(value=0, id=sliderId))
            drawSliderUI(fileRoot, sliderId)
        exportedValues = list(exportedDefs)
        exportedDefs.clear()
        for ele in reversed(exportedValues):
            exportedDefs.append(ele)
        for nodeType in nodeTypes:
            parentsToConnectSlider = []
            animatedElements = layer.findall(f".//*/animated[@type='{nodeType}']/..")
            for parent in animatedElements:
                parentsToConnectSlider.append(parent)
            connectSlider(parentsToConnectSlider, nodeType,
                        controllerIdsList=controllerIdsList)
