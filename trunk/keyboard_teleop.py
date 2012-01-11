#!/usr/bin/env python
# -*- coding: utf-8 -*-
#this node reads data from keyboard and publishes the data to the topic drive, which controls the arduino


#written by achuwilson
#achu_wilson@rediffmail.com
#achuwilson.wordpress.com

import roslib; roslib.load_manifest('beginner_tutorials')
import rospy
from std_msgs.msg import String

import termios, sys, os
#import termios, TERMIOS, sys, os
TERMIOS = termios
def getkey():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
                c = os.read(fd, 4)
        finally:
                termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c

def controller():
    pub = rospy.Publisher('drive', String)
    rospy.init_node('controller')
    while not rospy.is_shutdown():
        c = getkey()
        if ord(c[0]) == 27:
		  print 'arrow', c[2]
		  if c[2] == 'A':
		    str='f'
		  if c[2] == 'B':  
		     str='b'
		  if c[2] == 'C':  
		     str='r'
		  if c[2] == 'D':  
		     str='l'
		  
                  rospy.loginfo(str)
                  pub.publish(String(str))  
                  
        if c[0] == 'x':
          str  = 'x'
	if c[0] == 'w':
	  str  ='w'
	if c[0] == 's':
	  str  = 's'
	if c[0] == 'a':
	  str  = 'a'
	if c[0] == 'd':
          str  = 'd'
	if c[0] == 't':
          str  = 't'
	if c[0] == 'g':
          str  = 'g'
	if c[0] == 'y':
          str  = 'y'
	if c[0] == 'h':
          str  = 'h'
	
	rospy.loginfo(str)
        pub.publish(String(str))
		  
		     
        print 'got', c[0]
        
        
	  
        rospy.sleep(.05)
 
if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException: pass
