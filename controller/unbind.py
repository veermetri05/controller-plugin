import pkgutil
import re
from xml.etree import ElementTree

from controller.builders import createAngle, createColor, createReal, createVector

nodeTypes = ["vector", "real", "angle", "color"]

patternRegex = {}

for node in nodeTypes:
    patternRegex[node] = pkgutil.get_data(__name__, f"statics/regex/{node}.txt").decode("utf-8")


animatedElementStr = pkgutil.get_data(__name__, "statics/animatedElement.xml").decode("utf-8")

def replaceAddWithAnimated(elements: list, elementType: str, addNodeParent: ElementTree.Element, addNode: ElementTree.Element):
    animated = ElementTree.fromstring(animatedElementStr)
    firstElement = elements[0]
    animated.attrib["type"] = elementType
    if(elementType=="vector"):
        animated[0][0] = createVector(firstElement[0], firstElement[1])
        for i in range(1, 5):
            animated[i][0] = createVector(float(elements[i][0]) + float(firstElement[0]), float(elements[i][1]) + float(firstElement[1]))
    elif(elementType=="real"):
        animated[0][0] = createReal(firstElement)
        for i in range(1, 5):
            animated[i][0] =  createReal(float(elements[i]) + float(firstElement))
    elif(elementType=="angle"):
        animated[0][0] = createAngle(firstElement)
        for i in range(1, 5):
            animated[i][0] =  createAngle(float(elements[i]) + float(firstElement))

    elif(elementType=="color"):
        animated[0][0] = createColor(r=firstElement[0], g=firstElement[1], b=firstElement[2], a=firstElement[3])
        for i in range(1, 5):
            animated[i][0] =  createColor(r=float(elements[i][0]) + float(firstElement[0]),
            g=float(elements[i][1]) + float(firstElement[1]),
            b=float(elements[i][2]) + float(firstElement[2]),
            a=float(elements[i][3]) + float(firstElement[3])
            )
    addNodeParent.remove(addNode)
    addNodeParent.append(animated)


def unbindVectors(layer: ElementTree.Element):
    for addNodeParent in layer.findall(".//add[@type='vector']/.."):
        for addNode in addNodeParent:
            patternMatches = re.match(patternRegex["vector"], ElementTree.tostring(addNode).decode("utf-8"))
            if patternMatches:
                elements = [
                    [addNode[0][0][0][0][0][0][0].text, addNode[0][0][0][0][0][0][1].text],
                    [addNode[0][0][0][0][1][0][0][0][0].text, addNode[0][0][0][0][1][0][0][0][1].text],
                    [addNode[1][0][0][0][0][0][0].text, addNode[1][0][0][0][0][0][1].text],
                    [addNode[0][0][1][0][0][0][0].text, addNode[0][0][1][0][0][0][1].text],
                    [addNode[1][0][1][0][0][0][0].text, addNode[1][0][1][0][0][0][1].text]
                ]
                replaceAddWithAnimated(elements=elements, elementType="vector", addNodeParent=addNodeParent, addNode=addNode)

def unbindReals(layer: ElementTree.Element):
    for addNodeParent in layer.findall(".//add[@type='real']/.."):
        for addNode in addNodeParent:
            patternMatches = re.match(patternRegex["real"], ElementTree.tostring(addNode).decode("utf-8"))
            if patternMatches:
                elements = [
                    addNode[0][0][0][0][0][0].attrib["value"],
                    addNode[0][0][0][0][1][0][0][0].attrib["value"],
                    addNode[1][0][0][0][0][0].attrib["value"],
                    addNode[0][0][1][0][0][0].attrib["value"],
                    addNode[1][0][1][0][0][0].attrib["value"]
                ]
                replaceAddWithAnimated(elements=elements, elementType="real", addNodeParent=addNodeParent, addNode=addNode)

def unbindAngles(layer):
        for addNodeParent in layer.findall(".//add[@type='angle']/.."):
            for addNode in addNodeParent:
                patternMatches = re.match(patternRegex["angle"], ElementTree.tostring(addNode).decode("utf-8"))
                if patternMatches:
                    elements = [
                        addNode[0][0][0][0][0][0].attrib["value"],
                        addNode[0][0][0][0][1][0][0][0].attrib["value"],
                        addNode[1][0][0][0][0][0].attrib["value"],
                        addNode[0][0][1][0][0][0].attrib["value"],
                        addNode[1][0][1][0][0][0].attrib["value"]
                    ]
                    replaceAddWithAnimated(elements=elements, elementType="angle", addNodeParent=addNodeParent, addNode=addNode)

def unbindColors(layer: ElementTree.Element):
    for addNodeParent in layer.findall(".//add[@type='color']/.."):
        for addNode in addNodeParent:
            patternMatches = re.findall(patternRegex["color"], ElementTree.tostring(addNode).decode("utf-8"))
            if patternMatches:
                elements = [
                    [addNode[0][0][0][0][0][0][0].text, addNode[0][0][0][0][0][0][1].text, addNode[0][0][0][0][0][0][2].text, addNode[0][0][0][0][0][0][3].text ],
                    [addNode[0][0][0][0][1][0][0][0][0].text, addNode[0][0][0][0][1][0][0][0][1].text, addNode[0][0][0][0][1][0][0][0][2].text, addNode[0][0][0][0][1][0][0][0][3].text, addNode[0][0][0][0][1][0][0][0][3].text],
                    [addNode[1][0][0][0][0][0][0].text, addNode[1][0][0][0][0][0][1].text, addNode[1][0][0][0][0][0][2].text, addNode[1][0][0][0][0][0][3].text],
                    [addNode[0][0][1][0][0][0][0].text, addNode[0][0][1][0][0][0][1].text, addNode[0][0][1][0][0][0][2].text, addNode[0][0][1][0][0][0][3].text],
                    [addNode[1][0][1][0][0][0][0].text, addNode[1][0][1][0][0][0][1].text, addNode[1][0][1][0][0][0][2].text, addNode[1][0][1][0][0][0][3].text]
                ]
                replaceAddWithAnimated(elements=elements, elementType="color", addNodeParent=addNodeParent, addNode=addNode)

def unbindJoystick(root, fileRoot):
  unbindColors(root)
  unbindVectors(root)
  unbindReals(root)
  unbindAngles(root)
  