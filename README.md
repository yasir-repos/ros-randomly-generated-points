# ros-randomly-generated-points

AR_week4_test is a ros package which randomly generates point to point cubic parameters and uses them to calculate the cubic trajectories

## Installation
To install this file, move the AR_week4_test folder to ~HOME/catkin_ws/src

Open a new terminal window. 

Before continuing source your new setup.*sh file:

$ source devel/setup.bash

Open file using $ cd ~HOME/catkin_ws/src/AR_week4_test/scripts

Run the following in that terminal window:

$ chmod +x points_generator.py

$ chmod +x cubic_traj_planner.py

$ chmod +x compute_cubic_coeffs.py

$ chmod +x plot_cubic_traj.py

In new terminal:

$ cd ~HOME/catkin_ws/
$ catkin_make

## Usage
ROSLAUNCH APPROACH

Open a terminal window and type:

$ cd ~HOME/catkin_ws/src/AR_week4_test

$ roslaunch AR_week4_test cubic_traj_gen.launch


MANUAL APPROACH

To launch manually, open a new terminal window and type $ roscore

In new terminals, type:

$ rosrun AR_week4_test points_generator.py

$ rosrun AR_week4_test cubic_traj_planner.py

$ rosrun AR_week4_test compute_cubic_coeffs.py

$ rosrun AR_week4_test plot_cubic_traj.py


Plotting

To plot the coefficients, launch all the scripts as seen above. Open a new terminal and type:

$ rqt_plot

In the top left type in /velocity_traj , /position_traj , or /acceleration_traj for the corresponding plotting of the values. 
