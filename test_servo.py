import time
import pigpio

pi = pigpio.pi()
pi.wait_for_edge(13)
start = time.time()
pi.set_servo_pulsewidth(18,0)
pi.wait_for_edge(13, pigpio.FALLING_EDGE)
diff = time.time() - start
pi.set_servo_pulsewidth(18,0)
with open("/root/catDiet/cal.cfg",'w') as file:
    file.write(diff)

