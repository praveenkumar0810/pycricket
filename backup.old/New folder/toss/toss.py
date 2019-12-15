#!/usr/bin/python

import random

coin = ['head','tail']
play_selection = ['batting', 'bowling']

coin_random = random.choice(coin)
usr_in =  input('Head or Tail ==' ,)
usr_in = usr_in.lower()
if usr_in == coin_random :
	print('You won the toss')
	usr_selection = input('Batting or Bowling ==')
	usr_selection = usr_selection.lower()
	if usr_selection == play_selection[0] :
		print('Your opt yo Bat')
		###Batting function
	else :
		print('Your opt to bowl')
		#####bowling function
else :
	print('Computer won the toss')
	play_random = random.choice(play_selection)
	if play_random == play_selection[0] :
		print('Computer choses the Bat') 
		#####bowling function
	else :
		print('Computer choses the Bowl')
		####batting fuction
