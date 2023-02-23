#!/usr/bin/env

import rospy
import time
from std_msgs.msg import String

class talker():
    def __init__(self):
        rospy.init_node("talker")
        rospy.loginfo("started the Publisher_2 node")
        self.message = "Hello i'm new talker node !"
        self.msg_to_pub = rospy.Publisher("talker_topic", String, queue_size=10)
    def talk(self):
        self.msg_to_pub.publish(self.message)

if __name__== '__main__':
    tk = talker()
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        tk.talk()
        rate.sleep()
