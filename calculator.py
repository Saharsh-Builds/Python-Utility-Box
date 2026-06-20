import questionary

#this is the main fuction used to get the numbers for each operation..
def get_numbers():
    # loop if the user enters a invaild input!
    while True: 
        try:
            user_input = input("\nEnter numbers separated by spaces: ")

            numbers = [] # creation of an array
            
            # i learnt about arrays, ".split" and len() func
            # the code just splits and runs then number of time the user enter's ' ' and the number before it it stores in the numbers array
            for num in user_input.split():
                numbers.append(float(num))

            if len(numbers) < 2:
                print("Enter at least 2 numbers!")
                continue

            return numbers

        except ValueError:
            print("Invalid input! Please enter only numbers.")

# addition if it's not obvious!
def addition():
    numbers = get_numbers()

    result = sum(numbers)

    print(f"\nResult: {result}")
    input("\nPress Enter to continue...")

# subtraction if it's not obvious!
def subtraction():
    numbers = get_numbers()

    result = numbers[0] # first number

    for num in numbers[1:]:
        result -= num

    print(f"\nResult: {result}")
    input("\nPress Enter to continue...")

# multiplication if it's not obvious!
def multiplication():
    numbers = get_numbers()

    result = 1

    for num in numbers:
        result *= num

    print(f"\nResult: {result}")
    input("\nPress Enter to continue...")

# division if it's not obvious!
def division():
    numbers = get_numbers()

    result = numbers[0]

    for num in numbers[1:]:

        if num == 0:
            print("\nError: Cannot divide by zero.")
            input("\nPress Enter to continue...")
            return

        result /= num

    print(f"\nResult: {result}")
    input("\nPress Enter to continue...")

# The main Function of the program.. Its uses all the func stated before
def calculator():

    custom_style = questionary.Style([
        ("qmark", "fg:#5fd7ff bold"),
        ("question", "bold"),
        ("pointer", "fg:#ff5f87 bold"),
        ("highlighted", "fg:#00ff87 bold"),
        ("selected", "fg:#00ff87"),
        ("answer", "fg:#ffd75f bold"),
    ])

    while True:

        print("\n⚒ Calculator")
        print("────────────")

        choice = questionary.select(
            "Select an operation:",
            choices=[
                "+ Addition",
                "- Subtraction",
                "* Multiplication",
                "/ Division",
                "⬅ Back"
            ],
            pointer="❯",
            style=custom_style
        ).ask()

        if choice == "+ Addition":
            addition()

        elif choice == "- Subtraction":
            subtraction()

        elif choice == "* Multiplication":
            multiplication()

        elif choice == "/ Division":
            division()

        elif choice == "⬅ Back":
            break







if __name__ == "__main__":
    calculator()