import time
import pigpio

pi = pigpio.pi()
def main():
		calVal = None
		try:
				with open('/root/catDiet/cal.cfg', 'r') as calFile:
						calVal = float(calFile.read())
		except FileNotFoundError:
				print("cal file not found")
				calVal = calibrateFood()
		while True:
				currentAmount = quantityLogger()
				dispenseFood(currentAmount, calVal)
				time.sleep(21600‬)
def dispenseFood(amount, calVal):
		pi.set_servo_pulsewidth(18,1200)
		amount = amount/4
		time.sleep(amount * calVal)
		pi.set_servo_pulsewidth(18,0)
def quantityLogger():
		nextFoodAmount = None
		try:
				with open("/root/catDiet/food.log", "w") as foodLog:
						foodArray = foodLog.read().split("\n")
						nextFoodAmount = calcNextFoodAmount(foodArray[-1]
						foodArray.insert(0, str(nextFoodAmount))
						foodLog.write(str("\n").join(foodArray))
		except FileNotFoundError:
				nextFoodAmount = 0.5
		return nextFoodAmount
def calcNextFoodAmount(currentAmount):
		currentAmount = float(currentAmount)
		if currentAmount >= 0.333333333333333:
				return currentAmount - 0.00018264840182648
		return currentAmount
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
