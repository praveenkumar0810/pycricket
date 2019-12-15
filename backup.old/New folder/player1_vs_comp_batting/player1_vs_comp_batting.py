#!/usr/bin/python

import random

usr_score = []
com_score = []
##total
wick = 10
over = int(input('enter the overs u need to play',))
ball = over*6

##count 
wick_c = 0
ball_c = 0
run_c = 0

while True :
	if wick_c > 9 :
		break
	if ball_c == ball :
		break

	usr_inp = input('on strike',)

	if  usr_inp == str() or int(usr_inp) not in range(0,7):
		print('enter 0-6 to score')
		continue 
	usr_inp = int(usr_inp)
	ball_c += 1
	ball_r = ball - ball_c

	comp_inp = random.randint(0,6)
	com_score.append(comp_inp)

	if usr_inp == comp_inp :
		wick_c += 1
		print(('wicket no {} gone,ball remaining {}').format(wick_c,ball_r))
		continue

	if usr_inp != comp_inp :
		run_c += usr_inp
		usr_score.append(usr_inp)
		print(('the score is {}-{}').format(run_c,wick_c))
print(('Player{}-{} in {}').format(run_c,wick_c,ball_c))


     




