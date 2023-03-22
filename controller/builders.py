import uuid
from xml.etree import ElementTree


def new_guid():
    return uuid.uuid4().hex


def createReal(value, withGuid = False ):
    real = ElementTree.Element('real')
    if(withGuid):
        withGuid = new_guid()
        real.set('guid', withGuid)
    real.set('value', str(value))
    return real


def createAngle(value, withGuid = False):
    angle = ElementTree.Element('angle')
    if(withGuid):
        withGuid = new_guid()
        angle.set("guid", withGuid)
    angle.set('value', str(value))
    return angle


def createVector(xValue, yValue):
    vector = ElementTree.Element('vector')

    x = ElementTree.SubElement(vector, 'x')
    x.text = str(xValue)

    y = ElementTree.SubElement(vector, 'y')
    y.text = str(yValue)

    return vector

def createColor(r, g, b, a):
    color = ElementTree.Element('color')

    red = ElementTree.SubElement(color, 'r')
    red.text = str(r)

    green = ElementTree.SubElement(color, 'g')
    green.text = str(g)

    blue = ElementTree.SubElement(color, 'b')
    blue.text = str(b)

    alpha = ElementTree.SubElement(color, 'a')
    alpha.text = str(a)

    return color


def createVectorX(toLink=None, linkExported=None, type='real'):
    vectorX = ElementTree.Element('vectorx')
    vectorX.set('type', type)
    if linkExported is not None:
        vectorX.set('vector', linkExported)

    if linkExported is None:
        vector = ElementTree.SubElement(vectorX, 'vector')
        vector.append(toLink)

    return vectorX


def createVectorY(toLink=None, linkExported=None, type='real'):
    vectorY = ElementTree.Element('vectory')
    vectorY.set('type', type)
    if linkExported is not None:
        vectorY.set('vector', linkExported)

    if linkExported is None:
        vector = ElementTree.SubElement(vectorY, 'vector')
        vector.append(toLink)

    return vectorY

def createReciprocal(toLink, linkExported=None, type='real'):
    reciprocal = ElementTree.Element('reciprocal')
    reciprocal.set('type', type)
    if linkExported is not None:
        reciprocal.set('link', linkExported)

    if linkExported is None:
        link = ElementTree.SubElement(reciprocal, 'link')
        link.append(toLink)

    epsilon = ElementTree.SubElement(reciprocal, 'epsilon')
    epsilon.append(createReal("0.0000010000"))

    infinite = ElementTree.SubElement(reciprocal, 'infinite')
    infinite.append(createReal(999999.0000000000))

    return reciprocal


def createScale(scalarLink, type=None, linkExported=None, toLink=None):
    scale = ElementTree.Element('scale')
    scale.set('type', str(type))
    if linkExported is not None:
        scale.set('link', linkExported)

    if linkExported is None:
        link = ElementTree.SubElement(scale, 'link')
        link.append(toLink)

    scalar = ElementTree.SubElement(scale, 'scalar')
    scalar.append(scalarLink)

    return scale


def createSubtract(lhsLink, rhsLink, scalarLink, type):
    subtract = ElementTree.Element('subtract')
    subtract.set('type', type)

    scalar = ElementTree.SubElement(subtract, 'scalar')
    scalar.append(scalarLink)

    lhs = ElementTree.SubElement(subtract, 'lhs')
    lhs.append(lhsLink)

    rhs = ElementTree.SubElement(subtract, 'rhs')
    rhs.append(rhsLink)

    return subtract


def createAdd(lhsLink, rhsLink, scalarLink, type):
    add = ElementTree.Element('add')
    add.set('type', type)

    lhs = ElementTree.SubElement(add, 'lhs')
    lhs.append(lhsLink)

    rhs = ElementTree.SubElement(add, 'rhs')
    rhs.append(rhsLink)

    scalar = ElementTree.SubElement(add, 'scalar')
    scalar.append(scalarLink)

    return add


def createRange(minLink, maxLink, toLink, type, linkExported=None):
    range = ElementTree.Element('range')
    range.set('type', type)
    if linkExported is not None:
        range.set('link', linkExported)

    min = ElementTree.SubElement(range, 'min')
    min.append(minLink)

    max = ElementTree.SubElement(range, 'max')
    max.append(maxLink)

    if linkExported is None:
        link = ElementTree.SubElement(range, 'link')
        link.append(toLink)

    return range


def createPower(type, baseLink, powerRLink):
    power = ElementTree.Element('power')
    power.set('type', type)

    base = ElementTree.SubElement(power, 'base')
    base.append(baseLink)

    powerR = ElementTree.SubElement(power, 'power')
    powerR.append(powerRLink)

    epsilon = ElementTree.SubElement(power, 'epsilon')
    epsilon.append(createReal("0.0000010000"))

    infinite = ElementTree.SubElement(power, 'infinite')
    infinite.append(createReal("999999.0000000000"))

    return power

def createWaypoint(time: str, before: str, after: str, child: ElementTree.Element):
    waypoint = ElementTree.Element("waypoint")
    waypoint.set("time", time)
    waypoint.set("before", before)
    waypoint.set("after", after)
    waypoint.append(child)
