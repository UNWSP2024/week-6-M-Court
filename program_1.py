#this program chooses two random numbers between 1 and 6 and finds the sum. It repeats 100 times and averages the sums. 

#start total at zero
total = 0

#import module
import random

#roll two dice function
def randDice():
		#roll first dice
		dice1 = random.randint(1, 6)
		#roll second dice
		dice2 = random.randint(1, 6)
		#add sum of two dice
		dice_sum = dice1 + dice2
		return dice_sum

#repeat rolling and adding 100 times
for dice_sum in range(1,101):
	#runs random number generator
	dice_sum = randDice()
	
	#add sums together each loop
	total += dice_sum

#finds average
average = total / 100

#prints average
print(f"the average of 100 random rolls is {average:.3}")