# Navigating-the-Summit-Robot
Navigation of the Summit Robot, performing Mapping, Localization, Path Planning, and Obstacle Avoidance.

## Mapping

* Used the Hokuyu Laser of the Summit for creating Map.
* Performed gmapping and created a map of the environment and saved it in the maps folder.
* Created a package which provides the so created map to the localizer and path planner.

### Environment 
<img src="images/Screen Shot 2018-08-06 at 3.46.40 AM.png" width=650 height=350 >
<br/>

### Map of the Environment 
<img src="images/Screen Shot 2018-08-06 at 4.00.23 AM.png" width=650 height=400 >
<br/>

## Localization

* Used the map generated in the mapping part and used the map-server node for monte carlo localization(amcl).
* Started with a random distribution of the particles predicting the position of the robot and localized the summit, after serious amount of teleoperation.
* Created a custom service which registers into a file, label and their respective pose(positional and orientational) used to store some spots of the environment.

### Environment with initial random distribution of particles
<img src="images/Screen Shot 2018-08-07 at 3.09.14 AM.png" width=650 height=350 >
<br/>

### Environment after localization
<img src="images/Screen Shot 2018-08-07 at 3.06.58 AM.png" width=650 height=400 >
<br/>

## Path Planning

* Used the map generated in the mapping part and the amcl launch file from the previous parts.
* Launched a move_base node with common parameters.
* Performed autonomous navigation using Navfn planner which uses Dijkstra's Algorithm. 

### Path Planning In Action
<img src="images/Screen Shot 2018-08-08 at 1.51.47 AM.png" width=650 height=400 >
<br/>


