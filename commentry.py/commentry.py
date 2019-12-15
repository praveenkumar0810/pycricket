####batting
import random
for_single = ['Good cricket all round','That seems to be missing leg...and its single',
'Thats a Proper Cricket Shot.','Excellent batting conditions','Good cricket all round',]



for_boundary = ['Good cricket all round','When He Hits It, It Stays Hit.','hats placed in the gaps/vacant region',
'Thats a screamer','Excellent batting conditions','Straight down the ground','What a lovely shot!...its six',
'Only he can play that shot']


for_six = ['Good cricket all round','Just over the fielder','Thats a hugeeeee hit!','That’s a screamer',
'Excellent batting conditions','That’s massive and out of the ground','Maxxxxximumm','What a lovely shot!...its six',
'Only he can play that shot','Thats huge ','Thats a maximum']

for_wick = ['In the airrr…and taken','Good cricket all round','Excellent line and length','Thats some good short stuff','Straight Down the Fielder Throat.',
'Right Up in the Blockhole.','……..And he makes no mistake.','Edged and taken.','That’s a screamer',
'n the air..... fielder coming underneath and taken',
'Batsman tried a fancy stroke and threw his wicket',
'The break cost him his wicket as batsman tends to lose some concentration',
'Ball goes like a tracer bullet',
'What a catch!',
'From the middle of the bat and taken',
'In the airrrr.. XYZ takes it!',
'Bowled him',
'Excellent delivery']


for_batting  = ['Good cricket all round','……..And he makes no mistake.','That’s a screamer',]

for_bowling = ['It depends on how well the spinners bowl','Good cricket all round','Did it pitch in line',
'Excellent effort on the boundary','He has a go at the stumps','Direct hits are always dangerous',
'Thats sloppy work by the fielder.','Hes Bowling a Good Line and Length','……..And he makes no mistake.',
'Beautiful spell']

for_misc = ['School boy stuff (Sunil Gavaskar’s favourite when the batsman doesnt drag his bat in the crease)',
'We are up for a treat!','Cricket Is the Winner.','The Key Will Be Early Wickets.','The next few overs would be crucial.',
'They need to go for wickets now.','Stopping runs should be the topmost priority']



com_for_misc1 = ['School boy stuff (Sunil Gavaskar’s favourite when the batsman doesnt drag his bat in the crease)',
'We are up for a treat!','Cricket Is the Winner.',
'The Key Will Be Early Wickets.',
'The next few overs would be crucial.',
'They need to go for wickets now.',
'Stopping runs should be the topmost priority']
com_for_misc2 = None


def for_wickt() :

	com_for_wick = ['In the airrr…and taken','Good cricket all round','Excellent line and length',
	'Thats some good short stuff','Straight Down the Fielder Throat.',
	'Right Up in the Blockhole.','……..And he makes no mistake.','Edged and taken.',
	'That’s a screamer',
	'n the air..... fielder coming underneath and taken',
	'Batsman tried a fancy stroke and threw his wicket',
	'The break cost him his wicket as batsman tends to lose some concentration',
	'Ball goes like a tracer bullet',
	'What a catch!',
	'From the middle of the bat and taken',
	'In the airrrr.. XYZ takes it!',
	'Bowled him',
	'Excellent delivery']
	print(random.choice(com_for_wick))


count = 0
while True :
	count +=1
	for_wickt()
	if count == 1000 :
		break

