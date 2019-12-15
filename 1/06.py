# def intOnlytoscore() :
#     	while True :
#             try :
#                 xinpa = int(input("on strike",))
#                 if xinpa in range(0,7) :
#                     return xinpa
                    
#                 else :
#                     print("the score range 0-6")
#                     continue
                                                    
#             except ValueError as e :
#                 print(e)
#                 continue 
		
		
		
# inpa = intOnlytoscore()
# print(inpa)






while True :
    over = input("Enter the overs u need to play = ",)
    if over.isdigit() :
        over = int(over)
        break
    else :
        print("**Please enter a valid input**")
        continue