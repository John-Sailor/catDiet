import time
import pigpio


def main():
	currentAmount = quantityLogger()
	dispenseFood(currentAmount)
def dispenseFood(amount):
	pi.set_pulse_width(17,1000)
	foodConstant =
	time.sleep(amount * foodConstant *.001)
	pi.set_pulse_width(17,0)
def quantityLogger():
	foodArray = read_floats("/root/catDiet/food.log")
	nextFoodAmount = calcNextFoodAmount(foodArray[-1])
	foodLog = file.open("/root/catDiet/food.log", "w+")
	foodLog.write(str(nextFoodAmount) + '\n')
	foodLog.close
	return nextFoodAmount
def calcNextFoodAmount(currentAmount):
	if currentAmount >= 0.33333333333333333
		return currentAmount - 0.000182648401826484‬
	return currentAmount
def read_floats(filename):
    with open(filename) as f:
        return map(float, f)
