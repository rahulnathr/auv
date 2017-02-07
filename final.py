import os 
import os.path 
import sys	
from pymavlink import mavutil 
import errno
import time 
import threading


from MAVProxy.modules.lib import mp_module 
from MAVProxy.modules.lib import mp_util
from MAVProxy.modules.lib import mp_settings 

#initialising the module
class console1(mp_module.MPModule):
	def __init__(self,mpstate):
		super(console1,self).__init__(mpstate,"console1","arming the px4")
		self.master.arducopter_arm() 
		self.auv()
	def auv(self):
		#first get the sensor data from the external pressure sensor
		threading.Timer(3,self.auv).start()
		pressure=self.master.field('SCALED_PRESSURE','press_abs',0)
		scaledpressure=	self.master.field('SCALED_PRESSURE2','press_abs',0)
		print ("Scaled pressure is %f"%scaledpressure)
		if scaledpressure<1015.60:
			print ("the pressure is less so going down")
			#initiate rc commands to go down
			self.master.mav.rc_channels_override_send(self.target_system,self.target_component,1500,1500,1800,1500,1100,1500,1500,1500)
		if scaledpressure>1015.65:
			#setting the mode to depth -hold 
			self.master.mav.rc_channels_override_send(self.target_system,self.target_component,1500,1500,1800,1500,1100,1700,1500,1500)
			self.master.set_mode(2)

def init(mpstate):
	'''initialise module'''
	return console1(mpstate)