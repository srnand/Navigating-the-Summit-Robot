# Navigating-the-Summit-Robot
Navigation of the Summit Robot, performing Mapping, Localization, Path Planning, and Obstacle Avoidance.

## Mapping

* Used the Hukoyu Laser of the Summit for creating Map.
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
* Started with a random distribution of the particles predicting the position of the robot and localized the summit, after serios amount of teleoperation.
* Created a custom service which registers into a file, label and their respective pose(positional and orientational) used to store some spots of the environment.

