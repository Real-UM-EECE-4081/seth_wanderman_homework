

print("Question 6")
factorial = 1
Prefactored_num = int(input("please input a non-negative integer to get its factorial "))
if Prefactored_num < 0:
   print("Does not exist for negative numbers")
elif Prefactored_num == 0:
   print("1")
else:
   for X in range(1, Prefactored_num + 1):
       factorial = factorial *X
   print(factorial)