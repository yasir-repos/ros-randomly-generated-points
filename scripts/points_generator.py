#!/usr/bin/env python
# license removed for brevity

import rospy
import random
from AR_week4_test.msg import cubic_traj_params

def generator():
    pub = rospy.Publisher('points', cubic_traj_params, queue_size=0) #initialise new topic
    rospy.init_node('generator', anonymous=True) #initialise new node	
    rate = rospy.Rate(0.05) #0.05Hz = once every 20 seconds
    message = cubic_traj_params()
    while not rospy.is_shutdown():
	    message.p0 =  random.uniform(-10, 10)
	    message.pf = random.uniform(-10, 10)
	    message.v0 = random.uniform(-10, 10)
	    message.vf = random.uniform(-10, 10)
	    message.t0 = 0
	    message.tf = message.t0 + round(random.uniform(5, 10),0) #random parameters
	    rospy.loginfo(message)
	    pub.publish(message)
	    print(message)
	    rate.sleep()


if __name__ == '__main__':
    try:
        generator()
    except rospy.ROSInterruptExceprion:
        pass

    rospy.spin()
        
