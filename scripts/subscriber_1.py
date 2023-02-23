#!/usr/bin/env
import rospy
from std_msgs.msg import String

# def callback(data):
#     rospy.loginfo("Recieved data: %s", data.data)
#     # print("received")

# def listener():
#     rospy.init_node("Subscriber_1", anonymous=True)
#     rospy.Subscriber("/talking_topic",String, callback)
#     rospy.spin()


# if __name__ == "__main__":
#     try:
#         listener()

#     except rospy.ROSInterruptException:
#         pass


class listner():
    def __init__(self):
        rospy.init_node("subscriber_1", anonymous=True)
        self.message = ""
    def subscribe(self):
        rospy.Subscriber("/talking_topic", String, self.callback)
    def callback(self,msg):
        self.message = msg.data
        rospy.loginfo("Recieved data: %s", self.message)

if __name__ == '__main__':
    lst = listner()
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        lst.subscribe()
        rate.sleep()

    

