def show_menu():
    print("\n===== Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")
    print("======================")

def cal():
    show_menu()
    while True:
        choice = int(input("\nEnter Choice (0/1/2/3/4): "))

        if choice == 0:
            print("Exit!")
            break

        print()
        n1 = int(input("Enter first number: "))
        print()
        n2 = int(input("Enter second number: "))
        print()

        if choice == 1:   print(n1, "+", n2, "=", n1 + n2)
        elif choice == 2: print(n1, "-", n2, "=", n1 - n2)
        elif choice == 3: print(n1, "x", n2, "=", n1 * n2)
        elif choice == 4: print(n1, "÷", n2, "=", n1 / n2)
        else: print("Invalid choice, try again.")

cal()