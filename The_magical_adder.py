# For this exercise, you have to write a python program which prompts the user to enter three integers separated by ",".
# The user input is of the form: a,b,c, where a, b and c are numbers.
# Your program should calculate and display the result of the calculation:
# a + b - c
# Examples:
# 1. > Please enter three numbers: 10,11,10
# 11
#
# 2. > Please enter three numbers: 7,5,-1
# 13

print("Please enter three numbers separated by coma: ")
numbers_list = input().split(",")

for index in range(len(numbers_list)):
    numbers_list[index] = int(numbers_list[index])

result = numbers_list[0] + numbers_list[1] - numbers_list[2]
print(result)

