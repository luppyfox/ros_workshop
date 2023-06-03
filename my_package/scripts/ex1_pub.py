#!/usr/bin/env python3

import rospy
from my_package.msg import age_gender


def ex1_pub(age,gender):
    pub_age = rospy.Publisher('ppl_classification', age_gender, queue_size = 10)
    rospy.init_node('ex1_publish', anonymous = True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        msg = age_gender()
        msg.age = age
        msg.gender = gender
        pub_age.publish(msg)
        rate.sleep()

if __name__=='__main__':
    try:
        age = int(input("Age : "))
        gender = input("Gender :")
        ex1_pub(age,gender)
    except rospy.ROSInterruptException:
      pass