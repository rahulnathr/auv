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

		self.master.arducopter_arm() 
		self.override=[0]*16
		self.last_override=[0]*16
		self.override_counter=0
		if self.sitl_output:
			self.override_period=mavutil.periodic_event(20)
		else:
			self.override_period=mavutil.periodic_event(1)
		self.channelchange()
	def idle_task(self):
		if self.override_period.trigger():
			if (self.override!=[0]*16 or self.override !=self.last_override or self.override_counter>0):
				self.last_override=self.override[:]
				self.send_rc_override()
				if self.override_counter>0:
					self.override_counter-=1

	def send_rc_override(self):
		if self.sitl_output:
			buf = struct.pack('<HHHHHHHHHHHHHHHH',*self.override)
			self.sitl_output.write(buf)
		else:
			chan8=self.override[:8]
			self.master.mav.rc_channels_override_send(self.target_system,self.target_component,*chan8)


		#arm the module1
		
	def set_override(self,newchannels):
		self.override=newchannels
		self.override_counter=10
		self.send_rc_override()

	def set_override_chan(self,channel,value):
		self.override[channel]=value
		self.override_counter=10
		self.send_rc_override()

	def get_override_chan(self,channel):
		return self.override[channel]

	def channelchange(self):
		channels=self.override
		channels[5]=1200  #fwd.back control.yet cannot change the motor direction
		self.set_override(channels)


def init(mpstate):
	'''initialise module'''
	return console1(mpstate)
