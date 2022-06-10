# nrobot1

## autonomous navigation using rtabmap
This project consists of mapping and then navigating a ground robot on a plane ground terrain.
The project uses rtabmap for mapping and localizing in the environment. The project uses iRobot Create 2 and
two sensors, which are RGBD camera and Laser scanner. The robot successfully navigates the
map by staying away from obstacles, thus avoiding collision.
## Steps for running
You can build a map on your own using this project. The map will give you a rtabmap.db database
file and a map (which is obtained from map server.) After building, you can follow the general 
steps given below for navigation. 

When downloaded the src folder, run catkin build by being at the top 
of src folder. Then, source the project on each terminal you use by doing devel/setup.bash by 
remaining at the top of src folder directory. Then run the respective commands shown below
1. roslaunch irbt_gazebo irbt_gazebo.launch
2. roslaunch rtbmp_nc rtbmp_trial.launch
3. roslaunch nc_navigtn navigtn.launch
4. rosrun navigation_goals gndrobt_goals.py

Finally, open rviz by typing rviz in a new terminal. Use the saved rviz configuration given in the
src folder shared to avoid setting up manually all the things.
When run, the gndrobt_goals python script will give you output of number of locations, the time
to be at a respective location and the x and y co-ordinates and orientation of robot at a location.
After inserting these parameters, the robot will do the actions.

## Sensors used
1. RGBD camera
2. 2D Laser
