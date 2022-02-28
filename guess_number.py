#Let users guess a randomly generated number between 1 to 100, and give them tips (larger or smaller) to help them to find out the right number
import random
num = random.randint(1,100)
while True:
	num_guess = int(input('猜數字，請輸入一個1-100之間的數字：'))
	if num_guess > 100 or num_guess < 1:
		print('要猜1-100之間的數字喔')
	elif num == num_guess:
		print('猜對囉！')
		break
	elif num > num_guess:
		print('太小了，再往上猜！')
	else:
		print('太大了，請往下猜！')