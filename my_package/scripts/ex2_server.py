#!/usr/bin/env python3
import rospy
import subprocess
from my_package.srv import EspeakExercise, EspeakExerciseResponse

def callback(data):
    print(data.input)
    subprocess.call(["espeak", data.input])
    return EspeakExerciseResponse("Finish Speaking")

def speak_service_server():
    rospy.init_node('speak_server')
    msg = rospy.Service('speak', EspeakExercise, callback)
    rospy.spin()

if __name__=='__main__':
    speak_service_server()