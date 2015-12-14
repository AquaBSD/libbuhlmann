#! /usr/bin/python
"""

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
	for i in range(3,len(toks),2):
		histline.append(toks[i]) #1
		if (float(max(histline)) > maxpressure):
			maxpressure = float(max(histline))
	hs.append(histline)
fig = plt.figure()
ax = fig.add_subplot(121)

plt.plot(t_arr,d_arr)
plt.gca().invert_yaxis()


ax2 = fig.add_subplot(122)
ax2.set_ylim(0.7, maxpressure) 

nbComp = np.arange(len(histline))


rect = ax2.bar(nbComp,hs[0],width)


ax2.set_ylabel('Pressure')
ax2.set_title('Pressure by compartment')
#ax2.set_xticks(nbComp + width,1)
ax2.set_xticklabels(('C01', 'C02', 'C03', 'C04', 'C05','C06','C07','C08','C09','C10','C11','C12','C13','C14','C15','C16'))


axtime = plt.axes([0.2, 0.02, 0.65, 0.03])
stime= Slider(axtime, 'Time', 0, len(hs)-1, valinit=0,valfmt='%d')

def update(val):
	time = int(stime.val)
	ax2.clear()
	rect = ax2.bar(nbComp,hs[time],width)
	ax2.set_ylim(0.7, maxpressure) 
	ax.clear()
	ax.plot(t_arr,d_arr)
	ax.plot(t_arr[time], d_arr[time], 'or')

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

