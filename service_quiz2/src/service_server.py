#! /usr/bin/env python

import rospy
from service_quiz.srv import CustomMSG, CustomMSGResponse
from geometry_msgs.msg import Twist
import time


def my_callback(request):
    for i in range(4*request.repetions):
        # Move forward
        move_cmd = Twist()
        current_time = time.time()
        while (time.time() < current_time + request.side):
            move_cmd.linear.x = 0.5
            pub.publish(move_cmd)

        # Turn left
        move_cmd = Twist()
        current_time = time.time()
        while (time.time() < current_time + 2.97):
            move_cmd.angular.z = 0.5
            pub.publish(move_cmd)
        rospy.sleep(2.0)

    response.succes = True
    return response


rospy.init_node('quiz')
response = CustomMSGResponse()
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_cmd = Twist()
rate = rospy.Rate(1)
move_tb_in_circle = rospy.Service('/quiz_square', CustomMSG, my_callback)
rospy.loginfo("Service /quiz_square Ready")
rospy.spin()