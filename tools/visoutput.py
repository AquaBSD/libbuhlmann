#!/usr/bin/env python
"""
An animated image
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import sys

d_arr = []
t_arr = []


hs =[]

width = 0.35  
maxpressure = 0.0

for line in sys.stdin:
	toks = line.split(" ")
	
	t_arr.append(toks[0])
	d_arr.append((float(toks[1])-1)*10)
	
	histline = []
	histline.append(toks[3]) #1
	histline.append(toks[3]) #2
	histline.append(toks[5]) #3
	histline.append(toks[7]) #4
	histline.append(toks[9]) #5
	histline.append(toks[11])#6
	histline.append(toks[13])#7
	histline.append(toks[15])#8
	histline.append(toks[17])#9
	histline.append(toks[19])#10
	histline.append(toks[21])#11
	histline.append(toks[23])#12
	histline.append(toks[25])#13
	histline.append(toks[27])#14
	histline.append(toks[29])#15
	histline.append(toks[31])#16
	if (float(max(histline)) > maxpressure):
		maxpressure = float(max(histline))

	hs.append(histline)

fig = plt.figure()
fig.add_subplot(121)

l, = plt.plot(t_arr,d_arr)
plt.gca().invert_yaxis()


ax = fig.add_subplot(122)
ax.set_ylim(0.7, maxpressure) 

nbComp = np.arange(len(histline))


rect = ax.bar(nbComp,hs[0],width)


ax.set_ylabel('Pressure')
ax.set_title('Pressure by compartment')
ax.set_xticks(nbComp + width)
ax.set_xticklabels(('C01', 'C02', 'C03', 'C04', 'C05','C06','C07','C08','C09','C10','C11','C12'))


axtime = plt.axes([0.2, 0.02, 0.65, 0.03])
stime= Slider(axtime, 'Time', 0, len(hs)-1, valinit=0,valfmt='%d')

def update(val):
	time = int(stime.val)
	ax.clear()
	rect = ax.bar(nbComp,hs[time],width)
	ax.set_ylim(0.7, maxpressure) 
	fig.canvas.draw()
	

stime.on_changed(update)

# plt.subplot(2, 1, 2)
# plt.plot(t_arr,bc1_arr, label="cmp 1")
# plt.plot(t_arr,bc2_arr, label="cmp 2")
# plt.plot(t_arr,bc3_arr, label="cmp 3")
# plt.plot(t_arr,bc4_arr, label="cmp 4")
# plt.plot(t_arr,bc5_arr, label="cmp 5")
# plt.plot(t_arr,bc6_arr, label="cmp 6")
# plt.plot(t_arr,bc7_arr, label="cmp 7")
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


plt.show()