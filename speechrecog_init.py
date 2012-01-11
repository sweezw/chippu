#!/usr/bin/env python
# -*- coding: utf-8 -*-
#part of the speech recognition nodes of chippu

#runs julius using system calls, and then redirects its output to speech_recog.py
#such an approach is used because I could not find any c/python api for julius


#written by achuwilson
#achu_wilson@rediffmail.com
#achuwilson.wordpress.com

import roslib; roslib.load_manifest('chippu') 
import rospy
from std_msgs.msg import String
import os
import subprocess

def run():
  while not rospy.is_shutdown():
     a = os.system('julius -quiet -input mic -C julian.jconf 2>/dev/null | ./speech_recog.py')
     rospy.sleep(1.0)

if __name__ == '__main__':
       try:
           run()
       except rospy.ROSInterruptException: pass
       except KeyboardInterrupt:
		sys.exit(1)
   

