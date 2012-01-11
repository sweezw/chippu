#!/usr/bin/env python
# -*- coding: utf-8 -*-
#part of voice recognition based control of chippu,
#subscribes to topic speech (the detected string of speech)
#and makes decisions based on the recognised speech
#publishes to topic drive to control the chippu


#written by achuwilson
#achu_wilson@rediffmail.com
#achuwilson.wordpress.com

import roslib; roslib.load_manifest('chippu')
import rospy
from std_msgs.msg import String

def controller(data):
    pub = rospy.Publisher('drive', String)
   
    if(data.data>0):
     str = data.data
     if(str =="CHIPPU STOP NOW"):
       cmd= "x"
     elif(str =="CHIPPU MOVE FORWARD"):
       cmd= "f"
     elif(str =="CHIPPU MOVE BACKWARDS"):  
       cmd = "b"
     elif(str =="CHIPPU MOVE LEFT"):
       cmd ="l"
     elif(str =="CHIPPU MOVE RIGHT"):
       cmd ="r"
     elif(str =="CHIPPU LOOK UP"):
       cmd= "w"
     elif(str =="CHIPPU LOOK DOWN"):
       cmd= "s"
     elif(str =="CHIPPU LOOK RIGHT-SIDE"):
       cmd= "d"
     elif(str =="CHIPPU LOOK LEFT-SIDE"):
      cmd= "a"
     elif(str =="CHIPPU LEFT-HAND UP"):
      cmd= "g"
     elif(str =="CHIPPU LEFT-HAND DOWN"):
      cmd ="t"
     elif(str =="CHIPPU RIGHT-HAND UP"):
      cmd ="y"
     elif(str =="CHIPPU RIGHT-HAND DOWN"):
      cmd ="h"
    print str
    rospy.loginfo(str)
    pub.publish(String(cmd))
    
   
def listener():
   pub = rospy.Publisher('drive', String)
   rospy.init_node('voice_nav')
   sub = rospy.Subscriber("speech",String,controller)
   rospy.spin()
 
if __name__ == '__main__':
   listener()
   