import random
import questionary 
import time

custom_style = questionary.Style([
        ("qmark", "fg:#5fd7ff bold"),
        ("question", "bold"),
        ("pointer", "fg:#ff5f87 bold"),
        ("highlighted", "fg:#00ff87 bold"),
        ("selected", "fg:#00ff87"),
        ("answer", "fg:#ffd75f bold"),
    ])


def choose_die_option():
    
    

    print("DICE ROLLER!")
    print("─────────────")

    return questionary.select(
        "Choose a die to roll:",
        choices=[
            "6-sided die",
            "Custom-sided die",
            "Quit",
        ],
        pointer="❯",
        style=custom_style
    ).ask()

    


def get_custom_sides():
    answer = questionary.text("Enter the number of sides for the custom die:").ask()
    try:
        sides = int(answer)
        if sides < 1:
            raise ValueError("Must be positive")
        return sides
    except (TypeError, ValueError):
        print("Invalid input. Please enter a positive integer.")
        return None


def roll_die(sides):
    result = random.randint(1, sides)
    print(f"Rolling a {sides}-sided die...")
    time.sleep(1)
    print(f"You rolled : {result}")
    input("\nPress Enter to continue...")
    return result



def dice_roller():
    while True:
        choice = choose_die_option()
        if choice == "6-sided die":
            roll_die(6)
        elif choice == "Custom-sided die":
            sides = get_custom_sides()
            if sides is not None:
                roll_die(sides)
        else:
            break

        again = questionary.select(
            "Roll again?",
            choices=[
                "Yes",
                "No",
            ],
            pointer="❯",
            style=custom_style,
        ).ask()
        if not again:
            break

    print("Thanks for using the dice roller!")


if __name__ == "__main__":
    dice_roller()
