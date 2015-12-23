#!/usr/bin/python

import argparse

ascrate=15
decrate=20
sampling=.1
time=0.0
depth=0.0
gas="21,0"
O2=21.0
he=0.0
stime=10.0

def check_negative(value):
    dvalue = float(value)
    if dvalue < 0.0:
         raise argparse.ArgumentTypeError("%s is an invalid value" % value)
    return dvalue


parser = argparse.ArgumentParser(description='Generate a dive profile.')

parser.add_argument('-d', '--depth',  type=check_negative, required=True,
					dest='depth', help='depth of the dive in meters.')

parser.add_argument('-t', '--time', type=check_negative, required=True,
                   dest='time',help='bottom time in minutes.')

parser.add_argument('-g', '--gas', dest='gas', nargs='+',help='gas used for this dive, format : [depth],[n2],[he]; default is air for all the dive. ex: -g 0,66,0 20,')

args = parser.parse_args()


btime = float(args.time) 
maxdepth = float(args.depth)

gas = args.gas
if gas:
	nbgas = len(gas)
else:
	nbgas = 0

if (nbgas == 1):
	pasedgas = gas[0].split(',')
	if (len(pasedgas) == 3):
		O2=float(pasedgas[1])
		he=float(pasedgas[2])

print gas
#descent
while (time < btime and depth < maxdepth):
	print ("%.2f %.2f %.2f %.2f" % (time , (depth/10+1), O2, he))
	depth = depth + (decrate * sampling)
	time = time + sampling
depth = float(maxdepth)
print ("%.2f %.2f %.2f %.2f" % (time , (depth/10+1), O2, he))

#bottom
time = time + sampling
while (time < btime):
	print ("%.2f %.2f %.2f %.2f" % (time , (depth/10+1), O2, he))
	time = time + sampling

#ascent
depth = depth - (ascrate * sampling)
time = time + sampling
while (depth > 0.0):
	print ("%.2f %.2f %.2f %.2f" % (time , (depth/10+1), O2, he))
	depth = depth - (ascrate * sampling)
	time = time + sampling

depth = 0.0
while (stime > 0):
	time = time + sampling
	stime = stime - sampling
	print ("%.2f %.2f %.2f %.2f" % (time , (depth/10+1), O2, he))
