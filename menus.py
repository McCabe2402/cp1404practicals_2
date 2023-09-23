
name = input("Enter name: ")

choice = 'A'

while choice != 'Q':
    print("\nMenu:")
    print("1. Say hello")
    print("2. Say goodbye")
    print("Q. Quit")

    choice = input("Enter your choice: ").upper()

    if choice == '1':
        print(f"Hello, {name}!")
    elif choice == '2':
        print(f"Goodbye, {name}!")
    elif choice == 'Q':
        print(f"End of program.")
    else:
        print("Invalid choice. Please select a valid choice that is given.")