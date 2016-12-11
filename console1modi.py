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
		self.add_command('yaw',self.cmd_yaw,"change_yaw")
		self.add_command('fwd',self.fwd,"change_fwd_rev")
		self.add_command('thrust',self.thrust,"change_thrust")
		self.add_command('stop',self.stop,"revert_changes")
		
	channels=[1500,1500,1500,1500,1100,1500,1500,1500]


	phrase="2000 is max ,1000 is min,1500 is neutral"


	def sendcommand(self,args):
		self.master.mav.rc_channels_override_send(self.target_system,self.target_component,*args)

	def stop(self,args):
		self.channels[3]=1505
		self.sendcommand(self.channels)
		return	

	def thrust(self,args):
		self.master.arducopter_arm()
		print (self.phrase)
		self.channels[2]=int(args[0])
		self.sendcommand(self.channels)
		return


	def fwd(self,args):
		self.master.arducopter_arm()
		print (self.phrase)
		self.channels[5]=int(args[0])
		self.sendcommand(self.channels)
		return

	def cmd_yaw(self,args):
		self.master.arducopter_arm()
		print (self.phrase)
		self.channels[3]=int(args[0])
		print "sending newchannels",self.channels
		self.sendcommand(self.channels)
		return

	
def init(mpstate):
	'''initialise module'''
	return console1(mpstate)