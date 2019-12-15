while True :
    try:
        inpa = int(input("enter no = ",))
        if inpa in range(0,7) :
            return inpa

        else :
            print("Not okie")
    except ValueError as error :
        print(error)