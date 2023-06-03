#!/usr/bin/env python3
import rospy
import subprocess
from my_package.srv import EspeakExercise, EspeakExerciseRequest

def speak_service_client(message):
    rospy.init_node('speak_client')
    rospy.wait_for_service('speak')
    try:
        speak = rospy.ServiceProxy('speak', EspeakExercise)
        req = EspeakExerciseRequest()
        req.input = message
        result = speak(req)
        print(result.message)
        subprocess.call(["espeak", result.message])
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__=='__main__':
    msg = input("let's type ur message : ")
    speak_service_client(msg)


