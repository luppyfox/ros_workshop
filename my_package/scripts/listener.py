#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "Receive : %s",data.data )
    rospy.loginfo(rospy.get_caller_id() + f"Receive : {data.data}" )

def listener():
   rospy.init_node('listener', anonymous = True)
   rospy.Subscriber('chatter', String, callback)
   rospy.spin()


if __name__ == '__main__':
    listener()