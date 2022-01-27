from art import logo

def addition(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def multiply(num1, num2):
    return num1*num2
def division(num1, num2):
    return num1/num2

operations={
    "+": addition,
    "-": sub,
    "*": multiply,
    "/": division
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start as fresh:") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()


# if operation_symbol == "+":
#     answer = addition(num1, num2)
# elif operation_symbol == "-":
#     answer = sub(num1, num2)
# elif operation_symbol == "*":
#     answer = multiply(num1,num2)
# elif operation_symbol== "/":
#     answer = division(num1, num2)
# else:
#     answer = print("you entered a wrong choice")
# print(f"{num1} {operation_pick} {num2} = {answer}")