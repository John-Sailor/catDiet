import time
import pigpio

pi = pigpio.pi()
def main():
        #calVal = None
        #try:
          #      with open('/root/catDiet/cal.cfg', 'r') as calFile: 
         #               calVal = float(calFile.read().trim)
        #except FileNotFoundError:
         #       print("cal file not found")
          #      calVal = calibrateFood()
        currentAmount = quantityLogger()
        dispenseFood(currentAmount, calVal)
def dispenseFood(amount, calVal):
        pi.set_servo_pulsewidth(18,1000)
        foodConstant = 10
        amount = amount/4
        time.sleep(amount * calVal *.001)
        pi.set_servo_pulsewidth(18,0)
def quantityLogger():
	with open("/root/catDiet/food.log", "w") as foodLog:
		foodArray = foodLog.readlines()
		nextFoodAmount = calcNextFoodAmount(foodArray[-1].trim)
		foodArray.insert(0, str(nextFoodAmount))
		foodLog.write(str("\n").join(foodArray))
		return nextFoodAmount
def calcNextFoodAmount(currentAmount):
        currentAmount = float(currentAmount)
        if currentAmount >= 0.333333333333333:
                return currentAmount - 0.00018264840182648
        return currentAmount
def calibrateFood():
        pi = pigpio.pi()
        print("entering cal method")
        # fills the feeder wheel preventing inaccurate results
        pi.set_servo_pulsewidth(17,1000)
        print("filling wheel")
        time.sleep(1)
        pi.set_servo_pulsewidth(17,0)
        while True:
                print("waiting on input")
                time.sleep(5)
                if pi.read(23) == 1:
                        print("input recieved")
                        start = time.time()
                        while pi.read(23) == 1:
                                pi.set_servo_pulsewidth(17,1000)
                                time.sleep(.001)
                                pi.set_servo_pulsewidth(17,0)
                                time.sleep(.001)
                                stop = time.time()
                        print("input stopped")
                        calVal = (float(stop) - float(start))/2.0
                        with file.open("/root/catDiet/cal.cfg", "w") as calFile:
                                calFile.write(calVal)
                        return calVal
if __name__ == '__main__':
    main()
