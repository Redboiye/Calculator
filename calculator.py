from functions import calculate

print("Welcome to Simple Calculator")
result = None
number_1 = input("enter number_1: ")
operation = input("Choose operator: + - * /  ")
number_2 = input("enter number_2: ")

if number_1.isnumeric() and number_2.isnumeric():
    print('you enter the currect digit')
else:
    exit("incorrect format")

result = calculate(operation, number_1, number_2)

print(result)
