import time
import pigpio


amountFood
weight
prevWeight= []
def main():
	start time
	dispense food
	get weight
	adjust amount
	sleep
	dispense food
def getWeight():
	global weight
	//placeholder
def dispenseFood():
	pi.set_pulse_width(17,1000)
	time.sleep(amount*.001)
	pi.set_pulse_width(17,0)
def adjustAmount():
	day = getDay
	global amountFood
	global prevWeight[day] = weight
	# if target weight
	if prevWeight[day] <  targetWeight*1.02 && prevWeight[day] > targetWeight*.98:
		
	# if overweight
	if prevWeight[day] > prevWeight[day-7]*.98:
		amountFood = amountFood -5;
	#if on track
	else if  prevWeight[day] > prevWeight[day-7]*.95 && prevWeight[day] < prevWeight[day-7]*.99:
		amountFood = amountFood -1
	#underweight
	else:
		amount = amount +5
