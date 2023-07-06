# Master_Thesis
All Python codes related to my master thesis at IMS, TU Darmstadt: High-speed camera imaging on a planet gear stage deformation.

# folder_change
main.py is used to change the folder of NX output environment setting files, so that the NX model can be opened in the target PC with new path.

# gear_motion
simulate.py is used to get the animation of the epicycloid.  
HypoCycloid_01.py track the trajectory of a triangle comsists of three points.  
HypoCycloid.y track the trajectory of a single point.  
speed.py calculates the maximum speed of a point on the planet gear surface. 

# laser engrave
shortest_path.py outputs the Eulerian path for given node connections.  
node_connections.py contains the node connections (edges) for each gear mesh, some data may not be the newest.  
transform.py transforms the coordinats of each gear mesh by rotating a certain angle. Then the entire mesh can be construced by combining the single meshes.
## animation
animation.py creates an animation for the Eulerian path.
## dxf
creat_dxf.py outputs the .dxf file of the mesh to be opened in NX and get .prt file.

# mesh_raw_data
Raw data for each gear mesh, will open in LS-PrePost-4.5-x64.
