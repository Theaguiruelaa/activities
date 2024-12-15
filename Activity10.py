name = input("Enter Your Name: ")

isStudent = input("Are you a student of DLL (Yes / No): ")

if isStudent.lower() == "yes":
	yearlevel = input ("What year are you currently enrolled? \n F - Freshmen \n S - Sophomore \n J - Junior \n SN - Senior \n Please input your answer here: ")
 
	if yearlevel.lower() == "F":
		print (f"Hi {name}, Freshmen, Welcome to DLL ")

	elif yearlevel.lower() == "S":
		print (f"Hi {name}, Sophomore, Welcome to DLL ")



else: 
	print("Thank You for using the system")
