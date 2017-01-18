#! /usr/bin/python
"""

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import sys

d_arr = []
t_arr = []



compN2 = []
compHe = []
compList = ('1', '2', '3', '4','5','6','7','8','9','10','11','12','13','14','15','16')

width = 0.35  
maxpressure = 0.0
ceiling = []
nodectime = []
opacity = 0.4

if sys.stdin.isatty():
	exit()

for line in sys.stdin:
	toks = line.split(" ")
	
	t_arr.append(float(toks[0]))
	d_arr.append((float(toks[1])-1)*10)

	histline = []
	for i in range(2,len(toks)-2,2):
		histline.append(toks[i]) #1
		if (float(max(histline)) > maxpressure):
			maxpressure = float(max(histline))
	compN2.append(histline)

	histline = []
	for i in range(3,len(toks)-3,2):
		histline.append(toks[i]) 
		if (float(max(histline)) > maxpressure):
			maxpressure = float(max(histline))
	compHe.append(histline)


	if (float(toks[len(toks)-2]) < 1.0):
		ceiling.append(0.0)
	else:
		ceiling.append(float(toks[len(toks)-2]) - 1.0)



	nodectime.append(float(toks[len(toks)-1]))

fig = plt.figure()
fig.suptitle('Decompression', fontsize=14, fontweight='bold')
ax = fig.add_subplot(121)

plt.plot(t_arr,d_arr)
plt.plot(t_arr,ceiling)
plt.gca().invert_yaxis()


ax2 = fig.add_subplot(122)
ax2.set_ylim(0.7, maxpressure+0.5) 

nbComp = np.arange(16)


rect = ax2.bar(nbComp,compN2[0],width,alpha=opacity, color='b')
#rect = ax2.bar(nbComp,compHe[0],width +1 ,alpha=opacity, color='r')


ax2.set_ylabel('Pressure')
ax2.set_title('Pressure by compartment')
ax2.set_xticks(nbComp + width / 2 )
ax2.set_xticklabels(compList)

plt.xlabel('Compartment')
plt.ylabel('Pressure (bar)')

axtime = plt.axes([0.2, 0.02, 0.65, 0.03])
stime= Slider(axtime, 'Time', 0, len(compN2)-1, valinit=0,valfmt='%d')

def update(val):
	time = int(stime.val)
	ax2.clear()
	rect = ax2.bar(nbComp,compN2[time],width,alpha=opacity, color='b')
	
	ax2.set_xlabel('Compartment')
	ax2.set_ylabel('Pressure (bar)')
	ax2.set_xticks(nbComp + width / 2)
	ax2.set_xticklabels(compList)
	ax2.set_ylim(0.0, maxpressure+1) 
	


	ax.clear()
	ax.text(2, 3, "Ceiling : " + str("%.1f m" % ((ceiling[time]) *10)), fontsize=15)

	mins = int(nodectime[time])
	secs = int((nodectime[time] - mins) * 100)

	if (secs >= 60):
		mins = mins + 1
		secs = secs - 60

	ax.text(2, 6, "NoDec   : " + "{0} m {1} s".format(mins, secs) , fontsize=15)
	ax.plot(t_arr,d_arr)
	ax.plot(t_arr,ceiling)
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

