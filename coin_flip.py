from random import random

def flip_coin():
	print("If number is >0.5 returns HEAD othewise returns TAILS")
	r = random()
	if r > 0.5:
		print(r)
		return "HEADS"
	else:
		print(r)
		return "TAILS"
print(flip_coin())
