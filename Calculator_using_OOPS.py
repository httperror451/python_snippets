class Calculator():
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError as e:
            print("Can't devide by zero!")


operation = Calculator()

while True:
    try:
        choice = int(
            input("_______________\n1.add 2.sub 3.mul 4.div 5.exit\nChoose:"))
    except ValueError as e:
        print("only numbers allowed")
        continue

    if choice in (1, 2, 3, 4):
        try:
            num1 = int(input("num1:"))
            num2 = int(input("num1:"))
        except ValueError as e:
            print("only numbers allowed!")
            continue

        if choice == 1:
            print("result:", operation.add(num1, num2))

        elif choice == 2:
            print("result:", operation.sub(num1, num2))

        elif choice == 3:
            print("result:", operation.mul(num1, num2))

        elif choice == 4:
            print("result:", operation.div(num1, num2))

    elif choice == 5:
        print("program closed by user.")
        break
    else:
        print("invalid choice.")
