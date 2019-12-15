# while True :
    
#     if wick_c > 9 :
#         break
#     if ball_c == ball :
#         break

#     usr_inp = input("on strike",)

#     if  usr_inp == " " :
#         print("enter 0-6 to score")
#         continue
#     if int(usr_inp) not in range(0,7):
#         print("enter 0-6 to score")
#         continue

# while True : 
#     try:
#         usr_inp = input("on strike",)
#         if inpa.isdigit() or inpa in range(0,7):
#             break
#     except ValueError as e:
#         print("enter 0-6 to score")
#         continue



while True :
    inpa = input("enter nos pls===",)

    if inpa.isdigit() or inpa in range(0,7):
        print("inpa",inpa)
        break
    else :
        print("pls enter 0-6")
        continue 
    break









# case (1):   ############### (1)  #####################
#     while True :
#         inpa = input("enter nos pls===",)

#         if inpa.isdigit() or inpa in range(0,7):
#             print("inpa",inpa)
#             break
#         else :
#             print("pls enter 0-6")
#             continue 
#         break
# ################### func#################
# inpa = None
# def int_only1() :
#     while True :
#         inpa = input("enter nos pls===",)
#         if inpa.isdigit() or inpa in range(0,7):
#             break
#         else :
#             print("pls enter 0-6")
#             continue 
#         break
#     return inpa

    

# inpa =  int_only1()
# inpa = int(inpa)
# # print(inpa)




















# while True :
#     inpa = input("enter nos pls===",)
#     if int(inpa) in range(0,7):
#         print(inpa)
#     else :
#         print("break")
#         break


# while True :
#     try :
#         inpa = input("enter nos pls===",)

#     except :


# def int_only():
#     try:
#             inpa = int(input("no pls == ",))
#         except :
#             print("**Please enter a valid input**")
#             int_only()
#         return inpa
# print(int_only())






# import random

# import os 
# cwd =  os.getcwd()
# cdir =  os.chdir(b"F:\py_ex\project_cricket\1\")
# print("path",cwd)
# with open('test02.txt','a') as fopen :
#     while True :

#         com_for_bowling = ["It depends on how well the spinners bowl",
#         "Good cricket all round","Did it pitch in line",
#         "Excellent effort on the boundary","He has a go at the stumps",
#         "Direct hits are always dangerous",
#         "Thats sloppy work by the fielder.",
#         "Hes Bowling a Good Line and Length","......And he makes no mistake.",
#         "Beautiful spell"]
#         res =  (random.choice(com_for_bowling))
#        # print(res)
#         fopen.write(res)

    