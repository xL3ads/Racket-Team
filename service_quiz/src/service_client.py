#! /usr/bin/env python
import rospy
from std_srvs.srv import Empty
import sys

rospy.init_node('service_client')
rospy.wait_for_service('/quiz_square')
rotate_service = rospy.ServiceProxy('/quiz_square', Empty)

rotatie = rospy.ServiceProxy('/quiz_square', Empty)
rotatie()