#! /usr/bin/python
import argparse
from xml.dom import minidom

O2=21
H2=0

parser = argparse.ArgumentParser(description='Parse a dive in xml formt.')
parser.add_argument('-f', '--file',  required=True,
					dest='path', help='path to xml file')

args = parser.parse_args()
path = args.path
doc = minidom.parse(path)

gas = doc.getElementsByTagName('DiveMixture')


for subNode in gas.item(0).childNodes:
	if (subNode.nodeName == "Oxygen"):
		O2=float(subNode.childNodes[0].nodeValue)/100
	if (subNode.nodeName == "Helium"):
		H2=float(subNode.childNodes[0].nodeValue)/100

nodes = doc.getElementsByTagName('Dive.Sample')

for node in nodes:
    if node.hasChildNodes() and len(node.childNodes) > 8:
        for subNode in node.childNodes:
            if (subNode.nodeName == "Depth" and subNode.hasChildNodes()):
                depth = (float(subNode.childNodes[0].nodeValue) / 10) + 1
            if (subNode.nodeName == "Time" and subNode.hasChildNodes()):
                time = float(subNode.childNodes[0].nodeValue) / 60

    print ("%.2f %.2f %.2f %.2f" % (time , depth, O2, H2))
