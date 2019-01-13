# obj2box
A script collection to build in Aion on the basis of the existing game objects 

This script collection converts 3D-file (.obj) to voxel agglomeration and then to npc coordinates (result.txt) for AION online game.
example result in result.txt
<spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
for integration in \AC-Game\data\static_data\spawns\(Npcs or gather)\New\location.xml file.

1. find the 3D Model (.obj was tested) you want to build in Aion. 
some free models you can find here: 
https://free3d.com/
thefree3dmodels.com
www.turbosquid.com/3d
https://archive3d.net/

2. modificate the binvox_start.bat file and run it. Instructions how to use and adjust the binvox.exe you will find here: https://www.patrickmin.com/binvox/ 
3. this program will convert .obj file to voxel agglomeration. To view your .binvox file use viewvox.exe (to start: modificate and start view.bat).
4. to convert .binvox to game coordinates use binvox2box.py. But first adjust the .binvox file name and game coordinates in this file. 
5. copy coordinates from result.txt and put it in \AC-Game\data\static_data\spawns\(Npcs or gather)\New\location.xml file.

Note: large 3D models generates a lot of objects. Be sure your server has enough RAM.
Note2: this programs are not optimized for Aion, means the in game constuctions are filled with unnecessary objects. 
