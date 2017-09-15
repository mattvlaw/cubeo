from maestro import Controller
import time

class Cubeo:
	def __init__(self, port='dummy'):
		self.port = port
		self.servos = [2,4,3,5]
		self.open_controller(self.port)
		
		self.SLOW = 6200
		self.MEDIUM = 6600
		self.FAST = 7000
		self.VERYFAST= 7500
		self.STOP = 0
		self.running = False
		self.speed = self.SLOW


	def open_controller(self,port):
		if port=="dummy":
			self.cubeo_controller = dummyController()
		else:
			self.cubeo_controller  = Controller(ttyStr=port)
			for servo in self.servos:
				self.cubeo_controller.setAccel(servo,1)

	def close_controller(self):
		self.cubeo_controller.close()

	def do_the_wave(self,start=0,direction="clockwise"):
		for servo in self.servos:
			self.cubeo_controller.setTarget(servo,self.FAST)
			print("servo: ",servo)
			time.sleep(1)
			self.cubeo_controller.setTarget(servo,self.STOP)
	def move_panel_duration(self, servo, speed, duration):
		self.cubeo_controller.setTarget(servo,speed)
		time.sleep(duration)
		self.cubeo_controller.setTarget(servo,self.stop)
	def start_panel(self,servo,speed):
		print("SPEED ",speed)
		self.cubeo_controller.setTarget(servo,speed)
	def stop_panel(self,servo):
		self.cubeo_controller.setTarget(servo,self.STOP)
	def expand_all(self):
		for servo in self.servos:
			self.cubeo_controller.setTarget(servo,self.SLOW)
			print("servo: ",servo)
		time.sleep(5)
		for servo in self.servos:
			self.cubeo_controller.setTarget(servo,self.STOP)
	def breathe_slow(self):
		self.set_all_speed(self.SLOW)
	
	def breathe_medium(self):
		self.set_all_speed(self.MEDIUM)

	def breathe_fast(self):
		self.set_all_speed(self.FAST)
	
	def breathe_very_fast(self):
		self.set_all_speed(self.VERYFAST)

	def stop_breathing(self):
		self.set_all_speed(0)

	
	def set_all_speed(self,speed):
		for servo in self.servos:
			self.cubeo_controller.setTarget(servo,speed)
			print("servo: ",servo)
	
	def multiple_waves(self,num_iterations = 1):
		for i in range(num_iterations):
			do_the_wave()
class dummyController:
	def __init__(self):
		print "started dummy controller"
	def setTarget(self,channel,target):
		print "setting target for channel"+str(channel)+" to "+str(target)
	def close(self):
		print "closing dummy controller"

