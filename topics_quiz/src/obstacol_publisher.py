#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def publish_cmd_vel(pub, front_distance, right_distance, left_distance):
    cmd = Twist()
    if front_distance > 1.0:
        cmd.linear.x = 0.5
        cmd.angular.z = 0.0
    elif right_distance < 1.0:
        cmd.linear.x = 0.0
        cmd.angular.z = 0.5
    elif left_distance < 1.0:
        cmd.linear.x = 0.0
        cmd.angular.z = -0.5
    else:
        cmd.linear.x = 0.0
        cmd.angular.z = 0.5
    pub.publish(cmd)


def publish_to_cmd_vel():
    rospy.init_node('obstacle_avoidance')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        front_distance = rospy.get_param('/front_distance', 0.0)
        right_distance = rospy.get_param('/right_distance', 0.0)
        left_distance = rospy.get_param('/left_distance', 0.0)
        publish_cmd_vel(pub, front_distance, right_distance, left_distance)
        rate.sleep()


if __name__ == '__main__':
    try:
        publish_to_cmd_vel()
    except rospy.ROSInterruptException:
        pass

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

while not rospy.is_shutdown():
    pub.publish(count)
    count.data += 1
    rate.sleep()
