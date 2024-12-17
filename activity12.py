num = 0
odd = 0
even = 0

for a in range(1, 10):
    num1 = eval(input(f"Enter A Number {a}"))
    num += num1
    if num1 % 2 == 0:
        even += num1
    else:
        odd += num1

print(f"The Total of the number you entered is {num}")
print(f"The Total of the number you entered is {odd}")
print(f"The Total of the number you entered is {even}")