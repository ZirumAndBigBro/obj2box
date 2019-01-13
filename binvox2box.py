#binvox2box
#Python 3.6.2
#script BigБро
#idea Zirum

# example result in result.txt
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\Npcs\New\location.xml

#Example npc middle box 701016 / small box 700321 / or every other npc

import binvox_rw
import math

#insert here right name of your .binvox file
with open ('WoodenChessKnight.binvox', 'rb') as f:
    modell = binvox_rw.read_as_3d_array(f)

print(modell.dims)
print(modell.scale)

scale = 1 # Item size 1--> 1m x 1m x 1m --> middle wooden box (small box 0.5)

#insert your bottom left start point
x0 = 1524.0
y0 = 1507.57
z0 = 103.0
h0 = 30

file = open ('result.txt', 'w')
for i in range(0,modell.dims[0]):
    for j in range (0,modell.dims[1]):
        for k in range (0, modell.dims[2]):
              if (modell.data[i,j,k] == True):
                x = x0 + i*scale
                y = y0 + j*scale
                z = z0 + k*scale
                file.write('<spot h="{:d}" x="{:.2f}" y="{:.2f}" z="{:.2f}"/> \n'.format(h0, x, y, z))
                
file.close()

















