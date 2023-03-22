from xml.etree import ElementTree
import sys
import random
import uuid
import re
from controller import *
from controller.builders import *
from controller.draw import drawController


def connectController(typeTransition : str, list : list,  controller : str ):
    transitionList = []
    if(len(list) > 4):
      if(typeTransition == "vector"):
          transitionList.append(createVector(list[0][0], list[0][1]))
          transitionList.append(createVector(list[1][0]-list[0][0], list[1][1]-list[0][1]))
          transitionList.append(createVector(list[3][0]-list[0][0], list[3][1]-list[0][1]))
          transitionList.append(createVector(list[2][0]-list[0][0], list[2][1]-list[0][1]))
          transitionList.append(createVector(list[4][0]-list[0][0], list[4][1]-list[0][1]))
      elif(typeTransition == "real"):
          transitionList.append(createReal(list[0]))
          transitionList.append(createReal(list[1]-list[0]))
          transitionList.append(createReal(list[3]-list[0]))
          transitionList.append(createReal(list[2]-list[0]))
          transitionList.append(createReal(list[4]-list[0]))
      elif(typeTransition == "angle"):
          transitionList.append(createAngle(list[0]))
          transitionList.append(createAngle(list[1]-list[0]))
          transitionList.append(createAngle(list[3]-list[0]))
          transitionList.append(createAngle(list[2]-list[0]))
          transitionList.append(createAngle(list[4]-list[0]))
      elif(typeTransition == "color"):
          transitionList.append(createColor(list[0][0], list[0][1], list[0][1], list[0][3]))
          transitionList.append(createColor(list[1][0]-list[0][0], list[1][1]-list[0][1], list[1][2]-list[0][2], list[1][3]-list[0][3]))
          transitionList.append(createColor(list[3][0]-list[0][0], list[3][1]-list[0][1], list[3][2]-list[0][2], list[3][3]-list[0][3]))
          transitionList.append(createColor(list[2][0]-list[0][0], list[2][1]-list[0][1], list[2][2]-list[0][2], list[2][3]-list[0][3]))
          transitionList.append(createColor(list[4][0]-list[0][0], list[4][1]-list[0][1], list[4][2]-list[0][2], list[4][3]-list[0][3]))
      myxm = createAdd(
          type=typeTransition,
          lhsLink=createAdd(
              scalarLink=createReal(1.0),
              type=typeTransition,
              lhsLink=createAdd(
                  scalarLink=createReal(1.0),
                  type=typeTransition,
                  lhsLink=transitionList[0],
                  rhsLink=createScale(
                      type=typeTransition,
                      toLink=transitionList[1],
                      scalarLink=createRange(
                          type='real',
                          minLink=createReal(0),
                          maxLink=createReal(1.00),
                          toLink=createSubtract(
                              type='real',
                              scalarLink=createReciprocal(
                                  toLink=createReal(100),
                                  type="real"
                              ),
                              lhsLink=createScale(
                                  type="real",
                                  toLink=createVectorX(linkExported=controller),
                                  scalarLink=createReal(60.0)
                              ),
                              rhsLink=createReal(0)
                          )
                      )
                  )
              ),
              rhsLink=createScale(
                  type=typeTransition,
                  toLink=transitionList[2],
                  scalarLink=createRange(
                      type="real",
                      minLink=createReal("0.0"),
                      maxLink=createReal("1.00000"),
                      toLink=createSubtract(
                          type="real",
                          scalarLink=createReciprocal(
                              type='real',
                              toLink=createReal('100.000')
                          ),
                          lhsLink=createScale(
                              type='real',
                              toLink=createVectorY(linkExported= controller),
                              scalarLink=createReal("60.0")
                          ),
                          rhsLink=createReal("0")
                      )
                  )
              )
          ),
          rhsLink=createAdd(
              type=typeTransition,
              lhsLink=createScale(
                  type=typeTransition,
                  toLink=transitionList[3],
                  scalarLink=createSubtract(
                      type='real',
                      scalarLink=createReciprocal(
                          type='real',
                          toLink=createReal(-100)
                      ),
                      lhsLink=createRange(
                          type="real",
                          minLink=createReal(-100),
                          maxLink=createReal(0),
                          toLink=createScale(
                              type='real',
                              toLink=createVectorX(linkExported=controller),
                              scalarLink=createReal(60)
                          )
                      ),
                      rhsLink=createReal(0)
                  )
              ),
              rhsLink=createScale(
                  type=typeTransition,
                  toLink=transitionList[4],
                  scalarLink=createSubtract(
                      type='real',
                      scalarLink=createReciprocal(
                          type='real',
                          toLink=createReal(-100),
                      ),
                      lhsLink=createRange(
                          type='real',
                          minLink=createReal(-100.0000000000),
                          maxLink=createReal(0),
                          toLink=createScale(
                              type='real',
                              toLink=createVectorY(linkExported=controller),
                              scalarLink=createReal(60.0)
                          )
                      ),
                      rhsLink=createReal(0)
                  ),
              ),
              scalarLink=createReal(1.0)
          ),
          scalarLink=createReal(1.0),
      )
      return myxm


def createController(root, controllerName = None):
    for item in root:
        if item.tag == "defs":
            exportedDefs = item
    try:
      exportedDefs
    except NameError:
      exportedDefs = ElementTree.Element('defs')
      root.insert(list(root).index(list(root.findall(".//layer"))[0]) - 1, exportedDefs)
    

    if controllerName is None:
      controllerId = "controller" + random.randint(0, 9999)
    else:
      if exportedDefs.findall(".//*/[@id='{id}']".format(id = controllerName)):
        return controllerName
      controllerId = controllerName
    controller = ElementTree.fromstring(
        '''
    <vector id="{id}">
      <x>0</x>
      <y>0</y>
    </vector>
'''.format(id=controllerId))
    controlElements = [controller]
    exportedDefs.extend(controlElements)
    drawController(root, str(controllerId))
    return controllerId

animatedElementStr = '''
                <animated type="vector">
            <waypoint time="0f" before="clamped" after="clamped">
            <vector>
                <x>0</x>
                <y>0</y>
            </vector>
            </waypoint>
            <waypoint time="1f" before="clamped" after="clamped">
            <vector>
                <x>0</x>
                <y>0</y>
            </vector>
            </waypoint>
            <waypoint time="2f" before="clamped" after="clamped">
            <vector>
                <x>0</x>
                <y>0</y>
            </vector>
            </waypoint>
            <waypoint time="3f" before="clamped" after="clamped">
            <vector>
                <x>0</x>
                <y>0</y>
            </vector>
            </waypoint>
            <waypoint time="4f" before="clamped" after="clamped">
            <vector>
                <x>0</x>
                <y>0</y>
            </vector>
            </waypoint>
        </animated>
'''

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
            patternMatches = re.match(r'''<add\s+type="vector">\n\s+<lhs>\n\s+<add\s+type="vector">\n\s+<lhs>\n\s+<add\s+type="vector">\n\s+<lhs>\n\s+<vector>\n\s+<x>.*<\/x>\n\s+<y>.*<\/y>\n\s+<\/vector>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="vector">\n\s+<link>\n\s+<vector>\n\s+<x>.*<\/x>\n\s+<y>.*<\/y>\n\s+<\/vector>\n\s+<\/link>\n\s+<scalar>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectorx\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/link>\n\s+<\/range>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="vector">\n\s+<link>\n\s+<vector>\n\s+<x>.*<\/x>\n\s+<y>.*<\/y>\n\s+<\/vector>\n\s+<\/link>\n\s+<scalar>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectory\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/link>\n\s+<\/range>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/lhs>\n\s+<rhs>\n\s+<add\s+type="vector">\n\s+<lhs>\n\s+<scale\s+type="vector">\n\s+<link>\n\s+<vector>\n\s+<x>.*<\/x>\n\s+<y>.*<\/y>\n\s+<\/vector>\n\s+<\/link>\n\s+<scalar>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectorx\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/link>\n\s+<\/range>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="vector">\n\s+<link>\n\s+<vector>\n\s+<x>.*<\/x>\n\s+<y>.*<\/y>\n\s+<\/vector>\n\s+<\/link>\n\s+<scalar>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectory\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/link>\n\s+<\/range>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>''', ElementTree.tostring(addNode).decode("utf-8"))
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
            patternMatches = re.match(r'''<add\s+type="real">\n\s+<lhs>\n\s+<add\s+type="real">\n\s+<lhs>\n\s+<add\s+type="real">\n\s+<lhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectorx\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/link>\n\s+<\/range>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectory\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/link>\n\s+<\/range>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/lhs>\n\s+<rhs>\n\s+<add\s+type="real">\n\s+<lhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectorx\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/link>\n\s+<\/range>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectory\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/link>\n\s+<\/range>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>''', ElementTree.tostring(addNode).decode("utf-8"))
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
                patternMatches = re.match(r'''<add\s+type="angle">\n\s+<lhs>\n\s+<add\s+type="angle">\n\s+<lhs>\n\s+<add\s+type="angle">\n\s+<lhs>\n\s+<angle\s+value=".*"\s*\/>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="angle">\n\s+<link>\n\s+<angle\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectorx\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/link>\n\s+<\/range>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="angle">\n\s+<link>\n\s+<angle\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectory\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/link>\n\s+<\/range>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/lhs>\n\s+<rhs>\n\s+<add\s+type="angle">\n\s+<lhs>\n\s+<scale\s+type="angle">\n\s+<link>\n\s+<angle\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectorx\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/link>\n\s+<\/range>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="angle">\n\s+<link>\n\s+<angle\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectory\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/link>\n\s+<\/range>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>''', ElementTree.tostring(addNode).decode("utf-8"))
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
            patternMatches = re.findall(r'''<add\s+type="color">\n\s+<lhs>\n\s+<add\s+type="color">\n\s+<lhs>\n\s+<add\s+type="color">\n\s+<lhs>\n\s+<color>\n\s+<r>.*<\/r>\n\s+<g>.*<\/g>\n\s+<b>.*<\/b>\n\s+<a>.*<\/a>\n\s+<\/color>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="color">\n\s+<link>\n\s+<color>\n\s+<r>.*<\/r>\n\s+<g>.*<\/g>\n\s+<b>.*<\/b>\n\s+<a>.*<\/a>\n\s+<\/color>\n\s+<\/link>\n\s+<scalar>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectorx\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/link>\n\s+<\/range>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="color">\n\s+<link>\n\s+<color>\n\s+<r>.*<\/r>\n\s+<g>.*<\/g>\n\s+<b>.*<\/b>\n\s+<a>.*<\/a>\n\s+<\/color>\n\s+<\/link>\n\s+<scalar>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectory\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/link>\n\s+<\/range>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/lhs>\n\s+<rhs>\n\s+<add\s+type="color">\n\s+<lhs>\n\s+<scale\s+type="color">\n\s+<link>\n\s+<color>\n\s+<r>.*<\/r>\n\s+<g>.*<\/g>\n\s+<b>.*<\/b>\n\s+<a>.*<\/a>\n\s+<\/color>\n\s+<\/link>\n\s+<scalar>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectorx\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/link>\n\s+<\/range>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/lhs>\n\s+<rhs>\n\s+<scale\s+type="color">\n\s+<link>\n\s+<color>\n\s+<r>.*<\/r>\n\s+<g>.*<\/g>\n\s+<b>.*<\/b>\n\s+<a>.*<\/a>\n\s+<\/color>\n\s+<\/link>\n\s+<scalar>\n\s+<subtract\s+type="real">\n\s+<scalar>\n\s+<reciprocal\s+type="real">\n\s+<link>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/link>\n\s+<epsilon>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/epsilon>\n\s+<infinite>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/infinite>\n\s+<\/reciprocal>\n\s+<\/scalar>\n\s+<lhs>\n\s+<range\s+type="real">\n\s+<min>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/min>\n\s+<max>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/max>\n\s+<link>\n\s+<scale\s+type="real">\n\s+<link>\n\s+<vectory\s+type="real"\s+vector=".*"\s*\/>\n\s+<\/link>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/link>\n\s+<\/range>\n\s+<\/lhs>\n\s+<rhs>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/rhs>\n\s+<\/subtract>\n\s+<\/scalar>\n\s+<\/scale>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>\n\s+<\/rhs>\n\s+<scalar>\n\s+<real\s+value=".*"\s*\/>\n\s+<\/scalar>\n\s+<\/add>''', ElementTree.tostring(addNode).decode("utf-8"))
            if patternMatches:
                elements = [
                    [addNode[0][0][0][0][0][0][0].text, addNode[0][0][0][0][0][0][1].text, addNode[0][0][0][0][0][0][2].text, addNode[0][0][0][0][0][0][3].text ],
                    [addNode[0][0][0][0][1][0][0][0][0].text, addNode[0][0][0][0][1][0][0][0][1].text, addNode[0][0][0][0][1][0][0][0][2].text, addNode[0][0][0][0][1][0][0][0][3].text, addNode[0][0][0][0][1][0][0][0][3].text],
                    [addNode[1][0][0][0][0][0][0].text, addNode[1][0][0][0][0][0][1].text, addNode[1][0][0][0][0][0][2].text, addNode[1][0][0][0][0][0][3].text],
                    [addNode[0][0][1][0][0][0][0].text, addNode[0][0][1][0][0][0][1].text, addNode[0][0][1][0][0][0][2].text, addNode[0][0][1][0][0][0][3].text],
                    [addNode[1][0][1][0][0][0][0].text, addNode[1][0][1][0][0][0][1].text, addNode[1][0][1][0][0][0][2].text, addNode[1][0][1][0][0][0][3].text]
                ]
                replaceAddWithAnimated(elements=elements, elementType="color", addNodeParent=addNodeParent, addNode=addNode)

def generateJoystick(root, fileRoot):
  controller = str(createController(fileRoot, root.attrib['desc']))
  for parameters in root.findall(".//*/animated[@type='vector']/.."):
      for values in parameters:
          if(values.tag == "animated"):
              vectorValues = []
              for waypoint in values.findall("waypoint"):
                  vectorValues.append([float(waypoint[0][0].text), float(waypoint[0][1].text)])
              myxm = connectController(
                  typeTransition="vector", list=vectorValues, controller=controller)
              if(myxm is not None):
                parameters.remove(parameters[0])
                parameters.append(myxm)

  for parameters in root.findall(".//*/animated[@type='real']/.."):
      for values in parameters:
          if(values.tag == "animated"):
              realValues = []
              for waypoint in values.findall("waypoint"):
                  realValues.append(float(waypoint[0].attrib['value']))
              myxm = connectController(typeTransition='real', list=realValues, controller=controller)
              if(myxm is not None):
                parameters.remove(parameters[0])
                parameters.append(myxm)

  for parameters in root.findall(".//*/animated[@type='angle']/.."):
      for values in parameters:
          if(values.tag == "animated"):
              waypointAngles = []
              for waypoint in values.findall("waypoint"):
                  waypointAngles.append(float(waypoint[0].attrib['value']))
              myxm = connectController(
                  typeTransition="angle", list=waypointAngles, controller=controller)
              if(myxm is not None):
                parameters.remove(parameters[0])
                parameters.append(myxm)

  for parameters in root.findall(".//*/animated[@type='color']/.."):
      for values in parameters:
          if(values.tag == "animated"):
              waypointAngles = []
              for waypoint in values.findall("waypoint"):
                  waypointAngles.append([float(list(list(waypoint)[0])[0].text), float(list(list(waypoint)[0])[1].text), float(list(list(waypoint)[0])[2].text), float(list(list(waypoint)[0])[3].text) ])
              myxm = connectController(
                  typeTransition="color", list=waypointAngles, controller=controller)
              if(myxm is not None):
                parameters.remove(parameters[0])
                parameters.append(myxm)

def unbindJoystick(root, fileRoot):
  unbindVectors(root)
  unbindReals(root)
  unbindColors(root)
  unbindAngles(root)

root = ElementTree.parse(sys.argv[1]).getroot()

# Create new exported value controller

viewBox = list(map(lambda x: float(x), root.attrib['view-box'].split(' ')))
center = [((viewBox[0] + viewBox[2]) / 2), ((viewBox[1] + viewBox[3]) / 2)]

def findInnerChild(elem):
    for layer in elem.findall(".//layer[@type='group']"):
        if("desc" in layer.attrib):
            if( re.search( "joystick_.+" , layer.attrib["desc"]) ):
                if( filter( lambda a : re.search("joystick_.+" , a.attrib["desc"]), layer.findall(".//layer[@type='group']")) ):
                    findInnerChild(elem = layer)
                    layer.attrib["desc"] = layer.attrib["desc"][9:]
                    generateJoystick(root = layer, fileRoot=root)
                    print(layer.attrib["desc"])
                
for layer in root.findall("layer"):
    findInnerChild(layer)
    if("desc" in layer.attrib and re.search("joystick_unbind_.+", layer.attrib["desc"])):
        layer.attrib["desc"] = layer.attrib["desc"][16:]
        unbindJoystick(layer, root)
        print(layer.attrib["desc"])
    if("desc" in layer.attrib and re.search( "joystick_.+" , layer.attrib["desc"])):
        layer.attrib['desc'] = layer.attrib["desc"][9:]
        generateJoystick(root=layer, fileRoot=root)
        print(layer.attrib["desc"])        


writeTo = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1]

with open(writeTo, "wb") as files:
    files.write(ElementTree.tostring(root, encoding="utf-8", xml_declaration=True))