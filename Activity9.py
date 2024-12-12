age = eval(input("Enter age: "))

if age >= 1 and age <=7:
	print(f"Toddler")
elif age >= 8 and age <= 13:
	print(f"Pre Teen")
elif age >= 14 and age <= 18:
	print(f"Teenager")
elif age >= 19 and age <= 31:	
	print(f"Early Adult")
elif age >= 32 and age <= 45:
	print(f"Mid Adult")
elif age >= 46 and age <= 59:
	print(f"Post Adult")
elif age >= 60 and age <= 100:
	print(f"Senior")
else:
	print("Invalid Age")