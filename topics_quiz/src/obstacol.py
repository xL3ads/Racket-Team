#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class LaserScanSubscriber:
    def __init__(self):
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    def scan_callback(self, scan_msg):
        range_min = scan_msg.range_min
        range_max = scan_msg.range_max

        right_index = 0
        left_index = len(scan_msg.ranges) - 1
        right_range = scan_msg.ranges[right_index]
        left_range = scan_msg.ranges[left_index]
        center_index = len(scan_msg.ranges) // 2
        center_range = scan_msg.ranges[center_index]

        if center_range < 1:
            twist_msg = Twist()
            twist_msg.angular.z = 0.5
            self.vel_pub.publish(twist_msg)
        else:
            twist_msg = Twist()
            twist_msg.linear.x = 0.5
            self.vel_pub.publish(twist_msg)
            if right_range < 1:
                twist_msg = Twist()
                twist_msg.angular.z = 0.5
                self.vel_pub.publish(twist_msg)
            else:
                twist_msg = Twist()
                twist_msg.linear.x = 0.5
                self.vel_pub.publish(twist_msg)
                if left_range < 1:
                    twist_msg = Twist()
                    twist_msg.angular.z = -0.5
                    self.vel_pub.publish(twist_msg)
                else:
                    twist_msg = Twist()
                    twist_msg.linear.x = 0.5
                    self.vel_pub.publish(twist_msg)


rospy.init_node('laser_scan_subscriber')
laser_scan_subscriber = LaserScanSubscriber()
rospy.spin()
