#!/usr/bin/python

import argparse

ascrate=15
decrate=20
sampling=.1
time=0.0
depth=0.0
stime=10.0

def check_negative(value):
    dvalue = float(value)
    if dvalue < 0:
         raise argparse.ArgumentTypeError("%s is an invalid value" % value)
    return dvalue


parser = argparse.ArgumentParser(description='Generate a dive profile.')

parser.add_argument('-d', '--depth',  type=check_negative, required=True,
					dest='depth', help='depth of the dive in meters.')

parser.add_argument('-t', '--time', type=check_negative, required=True,
                   dest='time',help='bottom time in minutes.')

args = parser.parse_args()


btime = args.time
maxdepth = args.depth

#descent
while (time < btime and depth < maxdepth):
	print (str(time) + " " +str(depth/10+1))
	depth = depth + (decrate * sampling)
	time = time + sampling
depth = maxdepth
print (str(time) + " " +str(depth/10+1))

#bottom
time = time + sampling
while (time < btime):
	print (str(time) + " " +str(depth/10+1))
	time = time + sampling

#ascent
depth = depth - (ascrate * sampling)
time = time + sampling
while (depth > 0.0):
	print (str(time) + " " +str(depth/10+1))
	depth = depth - (ascrate * sampling)
	time = time + sampling

depth = 0.0
while (stime > 0):
	time = time + sampling
	stime = stime - sampling
	print (str(time) + " " +str(depth/10+1))
