import os 
import os.path 
import sys
from pymavlink import mavutil 
import errno
import time 

from MAVProxy.modules.lib import mp_module 
from MAVProxy.modules.lib import mp_util
from MAVProxy.modules.lib import mp_settings 

#initialising the module
class console1(mp_module.MPModule):
	def __init__(self,mpstate):
		super(console1,self).__init__(mpstate,"console1","arming the px4")

		self.master.arducopter_arm()    #arm the module 
		channels=self.override
		self.set_override(channels[4]=1450) # trying to set the yaw channel on rc channel 4 tp pwm 1450
		#i am using a simplerov ardusub firmware.
		
		
									

		
	


def init(mpstate):
	'''initialise module'''
	return console1(mpstate)
