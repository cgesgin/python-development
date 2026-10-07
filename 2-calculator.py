
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
choice = input("Choose an operation (+, -, *, /): ")

if choice == "+":
    result = number1 + number2
    print(result)
elif choice == "-":
    result = number1 - number2
    print(result)
elif choice == "*":
    result = number1 * number2
    print(result)
elif choice == "/":
    result = number1 / number2
    print(result)