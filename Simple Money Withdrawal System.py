
# Week 7: Simple Money Withdrawal System


def display_menu():
    """Error recovery options menu."""
    print("\nWhat would you like to do?")
    print("  [1] Re-enter a withdrawal amount")
    print("  [2] Check current balance")
    print("  [3] Exit the program")


def get_option():
    """Prompt user to choose an option and validate input."""
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")


def withdraw(balance):
    print("\n" + "=" * 45)
    print("        MONEY WITHDRAWAL SYSTEM")
    print("=" * 45)
    print(f"  Starting Balance: ₱{balance:,.2f}")
    print("=" * 45)

    while True:
        print(f"\n  Current Balance: ₱{balance:,.2f}")
        amount_input = input("  Enter withdrawal amount (or 'exit' to quit): ").strip()

        if amount_input.lower() == "exit":
            print("\nThank you for using the withdrawal system.!")
            break

        try:
            amount = float(amount_input)

            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")

            if amount > balance:
                raise Exception("Insufficient funds.")

            balance -= amount
            print(f"\n   Successfully withdraw ₱{amount:,.2f}")
            print(f"  Remaining Balance: ₱{balance:,.2f}")

        except ValueError as ve:
            print(f"\n   Invalid input: {ve}")
            display_menu()
            choice = get_option()
            if choice == "1":
                continue
            elif choice == "2":
                print(f"\n  Current Balance: ₱{balance:,.2f}")
                continue
            else:
                print("\nThank you for using the withdrawal system.!")
                break

        except Exception as e:
            print(f"\n  ✘ Error: {e}")
            display_menu()
            choice = get_option()
            if choice == "1":
                continue
            elif choice == "2":
                print(f"\n  Current Balance: ₱{balance:,.2f}")
                continue
            else:
                print("\nThank you for using the withdrawal system!")
                break

        finally:
            print("  -----------------------------------------")

    return balance


if __name__ == "__main__":
    starting_balance = 5000.00
    final_balance = withdraw(starting_balance)
    print(f"\n  Final Balance on Exit: ₱{final_balance:,.2f}\n")