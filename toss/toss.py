#!/usr/bin/python

import random
	
while True :

	coin = ['head','tail']
	random_coin = random.choices(coin)

	play_selection = ['batting', 'bowling']
	random_selection = random.choice(play_selection)


	usr_inpa = input('head or tail == ',)
	usr_inpa = usr_inpa.lower()

	if usr_inpa == coin[0] :
		# print(coin[0])
		break 

	if usr_inpa == coin[1] :
		# print(coin[1])
		break 
	print("Please enter Head or Tail")

if usr_inpa == random_coin :
	print("You won the Toss")
	print("Choose 'batting', 'bowling' ")
	usr_inpb = input("Batting or Bowling  == ")
	if usr_inpb == random_selection :
		####execute the batting function####

else :
	print("Computer won the Toss")
	usr_inpb =  random.choices(play_selection)
	if 
	




