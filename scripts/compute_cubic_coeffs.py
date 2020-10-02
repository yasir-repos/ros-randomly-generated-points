#!/usr/bin/env python

from AR_week4_test.srv import *
import rospy
import numpy as np #package for managing matricies

def cubic_traj_callback(request):
    parameters = request.pa #creates two matrices
    print 'Computation Request Confirmed'
    matrix_one = np.matrix('1 %d %d %d; 0 1 %d %d; 1 %d %d %d; 0 1 %d %d' % (parameters.t0, parameters.t0**2, parameters.t0**3, 2*parameters.t0, 3*(parameters.t0**2), parameters.tf, parameters.tf**2, parameters.tf**3, 2*parameters.tf, 3*(parameters.tf**2)))

    matrix_two = np.matrix('%d %d %d %d' % (parameters.p0, parameters.v0, parameters.pf, parameters.vf))
    # multiply inverse of matrix_one by matrix_two
    product = matrix_two * matrix_one.getI()
    result = product.getA1().tolist()
    print 'Returning %s' % result
    return compute_cubic_trajResponse(result[0], result[1], result[2], result[3])

def compute_cubic_coeffs():
    rospy.init_node('compute_cubic_coeffs') #initialising the node
    s = rospy.Service('compute_service', compute_cubic_traj, cubic_traj_callback) #initalising the service
    print "Ready to Compute Cubic Coefficients."
    
    rospy.spin()


if __name__ == "__main__":
    compute_cubic_coeffs()
