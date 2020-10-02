#!/usr/bin/env python

import rospy
from AR_week4_test.msg import cubic_traj_coeffs, cubic_traj_params
from std_msgs.msg import Float32

def callback(request):
    print("Connected to Plotting")
    a0 = request.a0
    a1 = request.a1
    a2 = request.a2
    a3 = request.a3
    t0 = request.t0
    tf = request.tf

    #publishing all initialised data
    publish_position = rospy.Publisher('position_traj', Float32, queue_size = 0)
    publish_velocity = rospy.Publisher('velocity_traj', Float32, queue_size = 0)
    publish_acceleration = rospy.Publisher('acceleration_traj', Float32, queue_size = 0)
    while t0 < tf:
        position = a0 + (a1*t0) + (a2*t0*t0) + (a3*t0*t0*t0)
        velocity = a1 + (2*a2*t0) + (3*(a3*(t0**2)))
        acceleration = (2*a2) + (6*a3*t0)
        publish_position.publish(position)
	publish_velocity.publish(velocity)
        publish_acceleration.publish(acceleration)
        t0 += 0.001
        print("Positional Trajectory: {}".format(position))
        print("Velocity of Trajectory: {}".format(velocity))
        print("Acceleration of Trajectory: {}".format(acceleration))

def plot_cubic_traj():
    rospy.init_node('plot_cubic_traj', anonymous=True) #initialise new node
    rospy.Subscriber('coeffs', cubic_traj_coeffs, callback) #subscribe to cubic_traj_params and send data to callback
    rospy.spin() #keeps python from exiting until node has stopped

if __name__ == "__main__":
    plot_cubic_traj()
