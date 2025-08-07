def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

def mul(n1, n2):
    return n1 * n2

calculation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def print_symbols():
    for key in calculation:
        print(key)
    
print("Welcome to the calculator program! \n")

n1 = int(input("Enter the first number "))
n2 = int(input("Enter the second number "))

print_symbols()

operation = input("choose an operation to perform ")

result = calculation[operation](n1,n2)

while True:
    choice = input(f"The result is: {result} do you want to perform another operation? (yes/no) \n")
    if choice.lower() == "yes":
        n1 = result
        n2 = int(input("Enter the next number "))
        print_symbols()
        operation = input("choose an operation to perform ")
        result = calculation[operation](n1, n2)
    else:
        print("Thank you for using the calculator program! ")
        break