#! /bin/python
import argparse
from xml.dom import minidom

parser = argparse.ArgumentParser(description='Parse a dive in xml formt.')
parser.add_argument('-f', '--file',  required=True,
					dest='path', help='path to xml file')

args = parser.parse_args()
path = args.path
doc = minidom.parse(path)
nodes = doc.getElementsByTagName('Dive.Sample')

for node in nodes:
	depth = (float(node.childNodes[2].childNodes[0].nodeValue) / 10 )+ 1
	time = float(node.childNodes[8].childNodes[0].nodeValue) / 60
	
	print ("%.2f %.2f" % (time , depth))