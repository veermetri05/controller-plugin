import pkgutil
import re
from xml.etree import ElementTree
from controller import replaceAddWithAnimated

nodeTypes = ["vector", "real", "angle", "color"]

patternRegex = {}

for node in nodeTypes:
    patternRegex[node] = pkgutil.get_data(__name__, "statics/regex/vector.txt").decode("utf-8")

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
  unbindVectors(root)
  unbindReals(root)
  unbindColors(root)
  unbindAngles(root)
  