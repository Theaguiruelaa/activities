
GoOn = True
count = 0 
while GoOn == True:
    name = input("Please enter a name: ")

    if name.lower() == "stop":
        print("loop has now stopped")
        print("You have entered {count} number of names")
        break
        GoOn = False
    else:
        count += 1
        continue    
