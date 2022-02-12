"""
A Simple Calculator Built with Pure Python
Change the code and practice yourself
"""
choose_operation = input("""
+--------------------+
|   Choose Option    |
| 1 - Addition       |
| 2 - Subtraction    |
| 3 - Multiplication |
| 4 - Division       |
+--------------------+
""")
def sum(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

if choose_operation == '1':
    num_1 = int(input('Enter First Number : '))
    num_2 = int(input('Enter Second Number : '))
    print('The Answer Is : ->')
    print(sum(num_1, num_2))
    
    
elif choose_operation == "2":
    num_1 = int(input('Enter First Number : '))
    num_2 = int(input('Enter Second Number : '))
    print('The Answer Is : ->')
    print(subtract(num_1, num_2))

elif choose_operation == '3':
    num_1 = int(input('Enter First Number : '))
    num_2 = int(input('Enter Second Number : '))
    print('The Answer Is : ->')
    print(multiply(num_1, num_2))
    

elif choose_operation == '4':
    num_1 = int(input('Enter First Number : '))
    num_2 = int(input('Enter Second Number : '))
    print('The Answer Is : ->')
    print(divide(num_1, num_2))
  

else:
    print("I'm Sorry! I can't Help")