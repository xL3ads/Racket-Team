#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan


def scan_callback(scan_msg):
    center_index = len(scan_msg.ranges) / 2
    front_distance = scan_msg.ranges[center_index]
    right_index = len(scan_msg.ranges) * 3 / 4
    right_distance = scan_msg.ranges[right_index]
    left_index = len(scan_msg.ranges) / 4
    left_distance = scan_msg.ranges[left_index]
    rospy.set_param('/front_distance', front_distance)
    rospy.set_param('/right_distance', right_distance)
    rospy.set_param('/left_distance', left_distance)


def subscribe_to_scan():
    rospy.init_node('obstacle_avoidance')
    rospy.Subscriber('/scan', LaserScan, scan_callback)
    rate = rospy.Rate(2)
