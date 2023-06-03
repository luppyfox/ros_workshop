#!/usr/bin/env python3

import rospy
from my_package.msg import age_gender

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + f"I found {data.age} year-old {data.gender}")

def ex1_sub():
    rospy.init_node('ex1_sub', anonymous = True)
    rospy.Subscriber('ppl_classification', age_gender, callback)
    rospy.spin()

if __name__=='__main__':
    ex1_sub()