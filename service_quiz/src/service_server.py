#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist
import time


def my_callback(request):
    while not rospy.is_shutdown():
        # Move forward
        move_cmd = Twist()
        current_time = time.time()
        while (time.time() < current_time + 2):
            move_cmd.linear.x = 0.5
            pub.publish(move_cmd)
        rospy.sleep(2.0)

        # Turn left
        move_cmd = Twist()
        current_time = time.time()
        while (time.time() < current_time + 2.6):
            move_cmd.angular.z = 0.5
            pub.publish(move_cmd)
        rospy.sleep(2.0)
    return EmptyResponse


rospy.init_node('quiz')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
z = Twist()
rate = rospy.Rate(1)
move_tb_in_circle = rospy.Service('/quiz_square', Empty, my_callback)
rospy.loginfo("Service /quiz_square Ready")
rospy.spin()