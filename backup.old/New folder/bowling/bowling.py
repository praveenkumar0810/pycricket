#!/usr/bin/python
import random

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

while True :
	if bwick_c > 9 :
		break
	if bball_c == bball :
		break

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
		brun_c += busr_inpb
		busr_score.append(busr_inpb)
		print(('the score is {}-{}').format(brun_c,bwick_c))
print(('{}-{} in {}balls ').format(brun_c,bwick_c,bball_c))

