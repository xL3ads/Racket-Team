#!/usr/bin/env python

import rospy
import actionlib
from ardrone_autonomy.msg import *
from ardrone_action_server.msg import ArdroneAction, ArdroneGoal, ArdroneResult

class ArdroneActionServer(object):
    _feedback = ArdroneResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, ArdroneAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()

        self._pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=10)
        self._pub_land = rospy.Publisher('/ardrone/land', Empty, queue_size=10)
        self._rate = rospy.Rate(1)

    def execute_cb(self, goal):
        success = True

        # Takeoff action
        if goal.action == "TAKEOFF":
            self._feedback.action = "Taking off"
            self._as.publish_feedback(self._feedback)

            self._pub_takeoff.publish(Empty())

            while not rospy.is_shutdown():
                if self._as.is_preempt_requested():
                    rospy.loginfo('%s: Preempted' % self._action_name)
                    self._as.set_preempted()
                    success = False
                    break

                self._feedback.action = "Taking off"
                self._as.publish_feedback(self._feedback)

                self._rate.sleep()

        # Land action
        elif goal.action == "LAND":
            self._feedback.action = "Landing"
            self._as.publish_feedback(self._feedback)

            self._pub_land.publish(Empty())

            while not rospy.is_shutdown():
                if self._as.is_preempt_requested():
                    rospy.loginfo('%s: Preempted' % self._action_name)
                    self._as.set_preempted()
                    success = False
                    break

                self._feedback.action = "Landing"
                self._as.publish_feedback(self._feedback)

                self._rate.sleep()

        else:
            rospy.logerr("Invalid action: %s" % goal.action)
            success = False

        if success:
            self._as.set_succeeded()

if __name__ == '__main__':
    rospy.init_node('ardrone_action_server')
    server = ArdroneActionServer(rospy.get_name())
    rospy.spin()
