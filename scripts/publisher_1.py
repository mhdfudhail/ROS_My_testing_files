#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# def talk_to_me():
#     pub = rospy.Publisher('talking_topic', String, queue_size=10)
#     rospy.init_node('publisher_1', anonymous=True)
#     rate = rospy.Rate(1)
#     rospy.loginfo("publisher_started_publishing")

#     while not rospy.is_shutdown():
#         msg = "Hello_friend !"
#         # print(msg)
#         pub.publish(msg)
#         rate.sleep()
 

# if __name__ == "__main__":
#     try:
#         talk_to_me()
#     except rospy.ROSInterruptException:
#         pass




class talker():
    def __init__(self):
        rospy.init_node("publisher_1", anonymous=True)
        self.pub = rospy.Publisher("talking_topic", String, queue_size=10)
        self.message = "Hello_my_friend !"
        rospy.loginfo("publisher_started_publishing_at_node_talking_topic")
        print(self.message)
    def publish(self):
        self.pub.publish(self.message)

if __name__ == '__main__':
    tk = talker()
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        tk.publish()
        rate.sleep()
        # print(tk.message)