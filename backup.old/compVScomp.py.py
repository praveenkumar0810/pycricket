import random
import time

##runs_lis
runs_lis1 = [] 

#total
total_ovr = 50
total_balls = total_ovr * 6
total_wick = 10

##count 
ovr_count = 0       
ball_count = 0
run_count = 0
wick_count = 0

#left
ball_left = total_balls - ball_count
wick_left = total_wick - wick_count

while wick_count < 10 :

    comp1_inpa = random.randint(0,6)
    comp2_inpa = random.randint(0,6)

    ##ball_counting
    ball_count = ball_count + 1
    print('ball_count',ball_count)
    if ball_count == total_balls :
        break

    if comp1_inpa == comp2_inpa :
        wick_count = wick_count + 1
        print(('wicket {} gone').format(wick_count))

    if comp1_inpa != comp2_inpa :
        run_count = comp1_inpa + run_count
        runs_lis1.append(comp1_inpa)
        time.sleep(0.2)
        print(('The score is {}').format(run_count))
        comp1_score = run_count
print(("the total score of comp1_inpa is {}").format(run_count))
#print('runs_lis',runs_lis)


##runs_lis
runs_lis2 = [] 

#total
#total_ovr = 5
total_balls = total_ovr * 6
total_wick = 10

##count 
ovr_count = 0       
ball_count = 0
run_count = 0
wick_count = 0

#left
ball_left = total_balls - ball_count
wick_left = total_wick - wick_count

while wick_count < 10 :

    comp1_inpa = random.randint(0,6)
    comp2_inpa = random.randint(0,6)

    ##ball_counting
    ball_count = ball_count + 1
    print('ball_count',ball_count)
    if ball_count == total_balls :
        break

    if comp1_inpa == comp2_inpa :
        wick_count = wick_count + 1
        print(('wicket {} gone').format(wick_count))

    if comp1_inpa != comp2_inpa :
        run_count = comp2_inpa + run_count
        runs_lis2.append(comp2_inpa)
        time.sleep(0.2)
        comp2_score = run_count
        print(('The score is {}').format(run_count))
        
print(("the total score of comp2_inpa is {}").format(run_count))

max_run = max(comp1_score,comp2_score)
min_run = min(comp1_score,comp2_score)
won_by = max_run - min_run

if comp1_score == max_run :
	print(('<<comp1>> won by {}').format(won_by))
elif comp2_score == max_run :
	print(('<<comp2>> won by {}').format(won_by))





