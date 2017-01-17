#!/usr/bin/python

import argparse
import sys



def check_negative(value):
    dvalue = float(value)
    if dvalue < 0.0:
         raise argparse.ArgumentTypeError("%s is an invalid value" % value)
    return dvalue

def initialize():

	parser = argparse.ArgumentParser(description='Generate a dive profile.')

	parser.add_argument('-d', '--depth',  type=check_negative, required=True,
						dest='depth', help='depth of the dive in meters.')

	parser.add_argument('-t', '--time', type=check_negative, required=True,
	                   dest='time',help='bottom time in minutes.')

	parser.add_argument('-g', '--gas', dest='gases', nargs='+',help='gas used for this dive, format : [depth],[o2],[he]; default is air for all the dive. ex: -g 90,14,58 for a trimix used at 60m with 14%% O2 and 58%% He')

	parser.add_argument('-o', '--deco',dest='decos', nargs='+',help='gas used for decompression, format : [depth],[o2],[he],[time]; ex: -o 20,50,0 for a 50%% nitrox for deco')

	args = parser.parse_args()

	btime = float(args.time) 
	maxdepth = float(args.depth)

	gases = []
	decogasses = []

	if args.gases:
		nbgas = len(args.gases)
		for gas in args.gases:
			splitedgas = gas.split(',')
			if (len(splitedgas) == 3):
				dict = {}
				dict['depth'] = float(splitedgas[0])
				dict['o2'] = float(splitedgas[1])/100
				dict['he'] = float(splitedgas[2])/100
				gases.append(dict)
			else:
				raise argparse.ArgumentTypeError("%s is an invalid formated gas" % gas)
	else:
		dict = {}
		dict['depth'] = 0.0
		dict['o2'] = .21
		dict['he'] = 0.0
		gases.append(dict)

	

	#deco gas parsing

	if args.decos:
		for gas in args.decos:
			splitedgas = gas.split(',')
			if (len(splitedgas) == 4):
				dict = {}
				dict['depth'] = float(splitedgas[0])
				dict['o2'] = float(splitedgas[1])/100
				dict['he'] = float(splitedgas[2])/100
				dict['time'] = float(splitedgas[3])
				decogasses.append(dict)
			else:
				raise argparse.ArgumentTypeError("%s is an invalid formated gas" % gas)
	generate_dive(btime, maxdepth, gases, decogasses)

def generate_dive(btime, maxdepth, gases, decogasses, out=sys.stdout):
	O2=.20948
	sampling=.1
	he=0.0
	stime=1.0
	nbgas = 0
	time=0.0
	depth=0.0
	ascrate=15
	decrate=20
	currgas = gases[0]

	#descent
	while (time < btime and depth < maxdepth):
		out.write ("%.2f %.2f %.2f %.2f\n" % (time , (depth/10+1), currgas['o2'], currgas['he']))
		depth = depth + (decrate * sampling)
		time = time + sampling
	depth = float(maxdepth)
	out.write ("%.2f %.2f %.2f %.2f\n" % (time , (depth/10+1), O2, he))

	#bottom
	time = time + sampling
	while (time < btime):
		out.write ("%.2f %.2f %.2f %.2f\n" % (time , (depth/10+1), O2, he))
		time = time + sampling

	#ascent
	depth = depth - (ascrate * sampling)
	time = time + sampling

	nbdeco = 0


	while (depth > 0.0):
		if nbdeco < len(decogasses) and decogasses[nbdeco]['depth'] >= depth:
			ascrate = 10
			O2 = decogasses[nbdeco]['o2']
			h2 = decogasses[nbdeco]['he']
			

		out.write ("%.2f %.2f %.2f %.2f\n" % (time , (depth/10+1), O2, he))
		if nbdeco < len(decogasses) and decogasses[nbdeco]['depth'] >= depth and decogasses[nbdeco]['time'] > 0:
			decogasses[nbdeco]['time'] -=  sampling
			if (decogasses[nbdeco]['time'] < 0):
				nbdeco += 1
		else:
			depth = depth - (ascrate * sampling)
			
		time = time + sampling

	depth = 0.0
	while (stime > 0):
		time = time + sampling
		stime = stime - sampling
		out.write ("%.2f %.2f %.2f %.2f\n" % (time , (depth/10+1), O2, he))


if __name__ == "__main__":
    import sys
    initialize()

