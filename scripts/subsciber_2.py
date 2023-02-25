#!/usr/bin/env

import rospy
import time
from std_msgs.msg import String

class listner():
    def __init__(self):
        rospy.init_node("listner")
        rospy.loginfo("started the Subscriber_2 node")
        self.message = ""
        self.msg_to_pub = rospy.Subscriber("/talking_topic", String, self.message_callback)
    def message_callback(self, msg):
        self.message = msg.data

    def listner(self):
        print(self.message)

if __name__== '__main__':
    tk = listner()
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        tk.listner()
        rate.sleep()

#does it work 
print("hello")
