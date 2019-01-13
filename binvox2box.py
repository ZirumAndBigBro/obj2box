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


scale = 0.9 # Item size 0.9--> 0.9m x 0.9m x 0.9m --> middle wooden box (small box 0.5)

#insert your bottom left start point
x0 = 1521.8
y0 = 1481.75
z0 = 103.0
h0 = 30

run1 = [[[False for a in range(modell.dims[0])] for b in range(modell.dims[1])] for c in range(modell.dims[2])]
run2 = [[[False for a in range(modell.dims[0])] for b in range(modell.dims[1])] for c in range(modell.dims[2])]
run3 = [[[False for a in range(modell.dims[0])] for b in range(modell.dims[1])] for c in range(modell.dims[2])]
modell_end = [[[False for a in range(modell.dims[0])] for b in range(modell.dims[1])] for c in range(modell.dims[2])]


for i in range(0,modell.dims[0]):
    for j in range (0,modell.dims[1]):
        for k in range (0, modell.dims[2]-1):
            if (modell.data[i,j,k] == False) and (modell.data[i,j,k+1] == True):
                run1[i][j][k+1] =  True
            if (modell.data[i,j,k] == True) and (modell.data[i,j+1,k+1] == False):
                run1[i][j][k] =  True
            if (modell.data[i,j,k] == True) and (k == 0):
                run1[i][j][k] =  True
            if (modell.data[i,j,modell.dims[2]-1] == True):
                run1[i][j][modell.dims[2]-1] =  True


for i in range(0,modell.dims[0]):
    for k in range (0,modell.dims[2]):
        for j in range (0, modell.dims[1]-1):
            if (modell.data[i,j,k] == False) and (modell.data[i,j+1,k] == True):
                run2[i][j+1][k] =  True
            if (modell.data[i,j,k] == True) and (modell.data[i,j+1,k] == False):
                run2[i][j][k] =  True
            if (modell.data[i,j,k] == True) and (j == 0):
                run2[i][j][k] =  True
            if (modell.data[i,modell.dims[1]-1,k] == True):
                run2[i][modell.dims[1]-1][k] =  True


for j in range(0,modell.dims[1]):
    for k in range (0,modell.dims[2]):
        for i in range (0, modell.dims[0]-1):
            if (modell.data[i,j,k] == False) and (modell.data[i+1,j,k] == True):
                run3[i+1][j][k] =  True
            if (modell.data[i,j,k] == True) and (modell.data[i+1,j,k] == False):
                run3[i][j][k] =  True
            if (modell.data[i,j,k] == True) and (i == 0):
                run3[i][j][k] =  True
            if (modell.data[modell.dims[0]-1,j,k] == True):
                run3[modell.dims[0]-1][j][k] =  True


for i in range(0,modell.dims[0]):
    for j in range (0,modell.dims[1]):
        for k in range (0, modell.dims[2]):
            if (run1[i][j][k] == True) or (run2[i][j][k] == True) or (run3[i][j][k] == True):
                modell_end[i][j][k] = True


file = open ('result.txt', 'w')
for i in range(0,modell.dims[0]):
    for j in range (0,modell.dims[1]):
        for k in range (0, modell.dims[2]):
            if (modell_end[i][j][k] == True):
                x = x0 + i*scale
                y = y0 + j*scale
                z = z0 + k*scale
                file.write('<spot h="{:d}" x="{:.2f}" y="{:.2f}" z="{:.2f}"/> \n'.format(h0, x, y, z))
                
file.close()

















