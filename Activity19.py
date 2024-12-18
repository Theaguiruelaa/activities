tig = True
while tig == True:
    name = input("Enter a name: ")
    if name.lower() == "stop":
        print("The loop has been terminated")
        break
        tig = False 