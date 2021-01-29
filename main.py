#!/usr/bin/python3
import time
import pigpio

pi = pigpio.pi()
def main():
                calVal = None
                try:
                                with open('/root/catDiet/cal.cfg', 'r') as calFile:
                                                calVal = float(calFile.read())
                                dispenseFood(float(0.2), calVal)
                except FileNotFoundError:
                                print("cal file not found")
                                calibrateFood()
def dispenseFood(amount, calVal):
		pi.set_servo_pulsewidth(18,1200)
		time.sleep(amount * calVal)
		pi.set_servo_pulsewidth(18,0)
def calibrateFood():
	pi = pigpio.pi()
	pi.wait_for_edge(13)
	start = time.time()
	pi.set_servo_pulsewidth(18,1200)
	pi.wait_for_edge(13,pigpio.FALLING_EDGE)
	diff = time.time() - start
	pi.set_servo_pulsewidth(18,0)
	with open("/root/catDiet/cal.cfg",'w') as file:
		file.write(str(diff))
if __name__ == '__main__':
	main()
