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
		time.sleep(5)
		self.master.arducopter_arm() #arm the copter
		time.sleep(5) #sleep the system
		self.master.mav.command_long_send(self.target_system,0,mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,0,0,0,0,0,0,0,0)
									#need of rc values to overide the motors

		
	


def init(mpstate):
	'''initialise module'''
	return console1(mpstate)
