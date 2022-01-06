class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def add(self):
        return num1 + num2

    def sub(self):
        return num1 - num2

    def mul(self):
        return num1 * num2

    def div(self):
        try:
            return num1 / num2
        except ZeroDivisionError as e:
            print("Can't devide by zero!")


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
            operation = Calculator(num1, num2)

        except ValueError as e:
            print("only numbers allowed!")
            continue

        if choice == 1:
            print("result:", operation.add())

        elif choice == 2:
            print("result:", operation.sub())

        elif choice == 3:
            print("result:", operation.mul())

        elif choice == 4:
            print("result:", operation.div())

    elif choice == 5:
        print("program closed by user.")
        break
    else:
        print("invalid choice.")
