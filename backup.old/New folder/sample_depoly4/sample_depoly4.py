#!/usr/bin/python

import random



###first batting 

def battingfirst() :
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



	##range(globa for battingfirst function)
	rran = range(0,ball)

	while True :
		if wick_c > 9 :
			break
		if ball_c == ball :
			break

		usr_inp = input('on strike',)

		if  usr_inp == ' ' and int(usr_inp) not in range(0,7):
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
		#	print(('the score is {}-{}').format(run_c,wick_c))
		if ball_c / 6 in rran :
			print(('the score is {}-{}').format(run_c,wick_c))

	player_score = run_c
	print(('Player{}-{} in {}').format(run_c,wick_c,ball_c))



	busr_score = []
	bcom_score = []
	##total
	bwick = 10
	bover = over
	#bover = int(input('enter the overs u need to play',))
	bball = bover*6

	##count 
	bwick_c = 0
	bball_c = 0
	brun_c = 0

	while True :
		if bwick_c > 9 :
			break
		if bball_c == bball :
			break
		print("error 01 not found")
		if player_score <= brun_c :
			break
		print("error 02 not found")
		busr_inpb = input('bowl',)

		if busr_inpb == '  ' or int(busr_inpb) not in range(0,7) :
			print('enter 0-6 to bowl')
			continue
		busr_inpb = int(busr_inpb)
		bball_c += 1
		bball_r = bball - bball_c

		bcomp_inp = random.randint(0,6)
		bcom_score.append(bcomp_inp)

		if busr_inpb == bcomp_inp :
			bwick_c += 1
			print(('wicket no {} gone,bball remaining {}').format(bwick_c,bball_r))
			continue

		if busr_inpb != bcomp_inp :
			brun_c += bcomp_inp
			busr_score.append(bcomp_inp)
			if bball_c / 6 in rran :
				print(('the score is {}-{}').format(brun_c,bwick_c))
		#	print(('the score is {}-{}').format(brun_c,bwick_c))
			computer_score = brun_c
	print(('{}-{} in {}balls ').format(brun_c,bwick_c,bball_c))


	#############Result
	if computer_score > player_score :
		print(('Computer won the match by {}').format(computer_score-player_score))
	if computer_score < player_score :
		print(('You won the match by {}').format(player_score - computer_score))
	if computer_score == player_score :
		print('Scores are Level -- Matchs Draw')





#####first 	bowling fucntion 

def bowlingfirst () :

	busr_score = []
	bcom_score = []
	##total
	bwick = 10
	bover = int(input('enter the overs u need to play',))
	bball = bover*6

	##count 
	bwick_c = 0
	bball_c = 0
	brun_c = 0

	##range(globa for ##bowlingfirst function)
	rran = range(0,bball)

	while True :
		if bwick_c > 9 :
			break
		if bball_c == bball :
			break

		busr_inpb = input('bowl',)

		if busr_inpb == ' ' or int(busr_inpb) not in range(0,7) :
			print('enter 0-6 to bowl')
			continue
		busr_inpb = int(busr_inpb)
		bball_c += 1
		bball_r = bball - bball_c

		bcomp_inp = random.randint(0,6)
		bcom_score.append(bcomp_inp)

		if busr_inpb == bcomp_inp :
			bwick_c += 1
			print(('wicket no {} gone,bball remaining {}').format(bwick_c,bball_r))
			continue

		if busr_inpb != bcomp_inp :
			brun_c += busr_inpb
			busr_score.append(busr_inpb)
			if bball_c / 6 in rran :
				print(('the score is {}-{}').format(brun_c,bwick_c))
		#	print(('the score is {}-{}').format(brun_c,bwick_c))
	computer_score = brun_c
	print(('{}-{} in {}balls ').format(brun_c,bwick_c,bball_c))

	###bat2

	usr_score = []
	com_score = []
	##total
	wick = 10
	#over = int(input('enter the overs u need to play',))
	over = bover
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
		if computer_score >= run_c :
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
			if ball_c / 6 in rran :
				print(('the score is {}-{}').format(run_c,wick_c))

		#	print(('the score is {}-{}').format(run_c,wick_c))
	player_score = run_c
	print(('Player{}-{} in {}').format(run_c,wick_c,ball_c))

	if computer_score > player_score :
		print(('Computer won the match by {}').format(computer_score-player_score))
	if computer_score < player_score :
		print(('You won the match by {}').format(player_score - computer_score))


###############toss###########

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
		battingfirst()
	else :
		print('Your opt to bowl')
		#####bowling function
		bowlingfirst()

else :
	print('Computer won the toss')
	play_random = random.choice(play_selection)
	if play_random == play_selection[0] :
		print('Computer choses the Bat') 
		#####bowling function
		bowlingfirst()

	else :
		print('Computer choses the Bowl')
		####batting fuction
		battingfirst()

