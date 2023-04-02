import pkgutil
import random
import re
from xml.etree import ElementTree
from controller.builders import *

from controller.draw import drawController
from controller.slider import generateSlider
from controller.unbind import unbindJoystick


def connectController(typeTransition : str, list : list,  controller : str ):
    itemSequence = [1, 3, 2,4]
    transitionList = []
    if(len(list) > 4):
      if(typeTransition == "vector"):
          transitionList.append(createVector(list[0][0], list[0][1]))
          for i in itemSequence:
            transitionList.append(createVector(list[i][0]-list[0][0], list[i][1]-list[0][1]))
      elif(typeTransition == "real"):
          transitionList.append(createReal(list[0]))
          for i in itemSequence:
            transitionList.append(createReal(list[i]-list[0]))
      elif(typeTransition == "angle"):
          transitionList.append(createAngle(list[0]))
          for i in itemSequence:
            transitionList.append(createAngle(list[i]-list[0]))
      elif(typeTransition == "color"):
          transitionList.append(createColor(list[0][0], list[0][1], list[0][1], list[0][3]))
          for i in itemSequence:
            transitionList.append(createColor(list[i][0]-list[0][0], list[i][1]-list[0][1], list[i][2]-list[0][2], list[i][3]-list[0][3]))
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


def findInnerChild(elem, root):
        for layer in elem.findall("layer"):
            if("desc" in layer.attrib):
                if( re.search( "joystick_unbind_.+" , layer.attrib["desc"]) ):
                    layer.attrib["desc"] = layer.attrib["desc"][16:]
                    unbindJoystick(root = layer, fileRoot=root)
                if( re.search( "joystick_.+" , layer.attrib["desc"]) ):
                    layer.attrib["desc"] = layer.attrib["desc"][9:]
                    generateJoystick(root = layer, fileRoot=root)
                if( re.search( "slider_.+" , layer.attrib["desc"]) ):
                    layer.attrib["desc"] = layer.attrib["desc"][7:] 
                    generateSlider(fileRoot=root,  layer=layer )
        if(len(elem.findall("layer/param[@name='canvas']/")) != 0):
            canvas = elem.findall("layer/param[@name='canvas']/")[0]
            findInnerChild(elem = canvas, root = root)