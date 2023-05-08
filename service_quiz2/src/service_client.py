#! /usr/bin/env python
import rospy
from service_quiz.srv import CustomMSG, CustomMSGRequest
import sys

rospy.init_node('service_client')
rospy.wait_for_service('/quiz_square')
rotate_service = rospy.ServiceProxy('/quiz_square', CustomMSG)
rotate_object = CustomMSGRequest()
rotate_object.repetions = 2
rotate_object.side = 2

result = rotate_service(rotate_object)
print (result)