class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error! Divide by zero."

    def pow(self, a, b):
        return a ** b


obj = Calculator()
while True:
    print(f"{50 * '*'}\n\t\t\t\tBasic Claculator\t\t\t\t\n{50 * '*'}")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n6.Exit\n")
    ch = int(input("Enter the Choice: "))
    if ch == 1:
        num1 = eval(input("enter the number1: "))
        num2 = eval(input("enter the number2: "))
        print(obj.add(num1, num2))
    elif ch == 2:
        num1 = eval(input("enter the number1: "))
        num2 = eval(input("enter the number2: "))
        print(obj.sub(num1, num2))
    elif ch == 3:
        num1 = eval(input("enter the number1: "))
        num2 = eval(input("enter the number2: "))
        print(obj.mul(num1, num2))
    elif ch == 4:
        num1 = eval(input("enter the number1: "))
        num2 = eval(input("enter the number2: "))
        print(obj.div(num1, num2))
    elif ch == 5:
        num1 = eval(input("enter the number1: "))
        num2 = eval(input("enter the number2 to power: "))
        print(obj.pow(num1, num2))
    elif ch == 6:
        exit()
