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
		self.pressure_record()
		self.down_thrust()
	def pressure_record(self):
		pressure=self.master.field('SCALED_PRESSURE','press_abs',0)
		scaledpressure=self.master.field('SCALED_PRESSURE1','press_abs',0)
		f=open("pressure_record.txt","w")
		f.write("This is pressure:%f and scaled_pressure is %f"%(pressure,scaledpressure))
		f.close()
		print (pressure)
		print (scaledpressure)
	def down_thrust(self):
		pressure=self.master.field('SCALED_PRESSURE','press_abs',0)
		if pressure<1013:
			print ("Pressure is too low,I am going to go down")

def init(mpstate):
	'''initialise module'''
	return console1(mpstate)