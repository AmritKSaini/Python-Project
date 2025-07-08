import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
# print(operations["*"](4,8))

def calc():
    print(art.logo)
    continue_calc = True
    num1 = float(input("What's the first number?: "))

    while continue_calc:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            num1 = answer

        elif choice == "n":
            continue_calc = False
            print(" \n" * 20)
            calc()
        else:
            continue_calc = False
            print("Please type a valid response!")
            calc()

calc()


