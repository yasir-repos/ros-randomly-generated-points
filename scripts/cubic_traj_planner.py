#!/usr/bin/env python

import rospy
from AR_week4_test.srv import *
from AR_week4_test.msg import cubic_traj_params
from AR_week4_test.msg import cubic_traj_coeffs

def planner(data): #receives values from the trajectory coefficients and publishes the trajectory coefficients
    pub = rospy.Publisher('coeffs', cubic_traj_coeffs, queue_size = 0) #initialising publishing

    try: #try to connect to service
        compute_coeffs = rospy.ServiceProxy('compute_service', compute_cubic_traj) #using data obtained to compute trajectories
        #response = compute_coeffs(data.p0, data.pf, data.v0, data.vf, data.t0, data.tf)
	response = compute_coeffs(data)

        #now to construct a message
        msg = cubic_traj_coeffs()
        msg.a0 = response.a0
        msg.a1 = response.a1
	msg.a2 = response.a2
	msg.a3 = response.a3
	msg.t0 = data.t0
	msg.tf = data.tf
	print msg
	pub.publish(msg) #publish obtained data
    except rospy.ServiceException, e:
	print "Service call failed: %s"%e

def cubic_traj_planner():
    rospy.init_node('cubic_traj_planner', anonymous=True) #initialising new node
    rospy.wait_for_service('compute_service') #holding on and waiting for service
    rospy.Subscriber('points', cubic_traj_params, planner)#making the node subscribe to compute_traj_params and send data to planner
    rospy.spin() #keeps python from exiting until the node is stopped

if __name__ == "__main__": #calls subscriber method when script is called
    cubic_traj_planner()
    
