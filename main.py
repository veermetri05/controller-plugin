import os
import pkgutil
from xml.etree import ElementTree
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import random
import uuid
import re
import controller
import controller.builders
import controller.draw
import controller.unbind



def main():
  root = ElementTree.parse(sys.argv[1]).getroot()

  # Create new exported value controller

  viewBox = list(map(lambda x: float(x), root.attrib['view-box'].split(' ')))
  center = [((viewBox[0] + viewBox[2]) / 2), ((viewBox[1] + viewBox[3]) / 2)]

  controller.findInnerChild(root, root)


  writeTo = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1]

  with open(writeTo, "wb") as files:
      files.write(ElementTree.tostring(root, encoding="utf-8", xml_declaration=True))

if __name__ == "__main__":
  main()