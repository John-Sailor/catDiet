import time
import pigpio


def main():
	calVal
	try:
		with open('/root/catDiet/cal.cfg', 'r') as calFile:
			calVal = float(calFile.read().trim)
	except FileNotFoundError:
		calVal = calibrateFood()
	currentAmount = quantityLogger()
	dispenseFood(currentAmount, calVal)
def dispenseFood(amount, calVal):
	pi.set_pulse_width(17,1000)
	foodConstant = 10
	time.sleep(amount * calVal *.001)
	pi.set_pulse_width(17,0)
def quantityLogger():
	nextFoodAmount = calcNextFoodAmount(foodArray[-1])
	with file.open("/root/catDiet/food.log", "w") as foodLog:
		foodArray = foodLog.readlines()
		nextFoodAmount = calcNextFoodAmount(foodArray[-1].trim)
		foodArray.insert(0, str(nextFoodAmount))
		foodLog.write(str("\n").join(foodArray))
		return nextFoodAmount
def calcNextFoodAmount(currentAmount):
	currentAmount = float(currentAmount)
	if currentAmount >= 0.33333333333333333
		return currentAmount - 0.000182648401826484‬
	return currentAmount
def calibrateFood()
	# fills the feeder wheel preventing inaccurate results
	pi.set_pulse_width(17,1000)
	time.sleep(1)
	pi.set_pulse_width(17,0)
	while true
	    time.sleep(5)
		if pi.read(23) == 1:
			start = time.time()
			stop = start
			while pi.read(23) == 1:
				pi.set_pulse_width(17,1000)
				time.sleep(.001)
				pi.set_pulse_width(17,0)
				time.sleep(.001)
				stop = time.time()
			calVal = (float(stop) - float(start))/2.0
			with file.open("/root/catDiet/cal.cfg", "w") as calFile:
				calFile.write(calVal)
			return calVal
if __name__ == '__main__':
    main()
