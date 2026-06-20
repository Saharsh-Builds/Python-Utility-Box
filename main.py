import questionary
import sys


def main_menu():

    def show_banner():
        print("\n")
        print("╭───────────────────────────────────────────╮")
        print("│ Utility Box v1.0                          │")
        print("│                                           │")
        print("│ made by Saharsh-Builds <3                 │")
        print("│                                           │")
        print("│ For learning Python, and a few tools      │")
        print("╰───────────────────────────────────────────╯")
        print()

    show_banner()

    custom_style = questionary.Style([
        ('qmark', 'fg:#00d7ff bold'),          
        ('question', 'fg:#00d7ff bold'),       
        ('pointer', 'fg:#ff5f87 bold'),        
        ('highlighted', 'fg:#5fff87 bold'),    
        ('selected', 'fg:#5fff87'),           
        ('answer', 'fg:#ffd700 bold'),         
    ])

    choice = questionary.select(
        "Select a utility:",
        choices=[
            "🧮 Calculator",
            "🎲 Dice Roller",
            "🔐 Password Generator",
            "🚪 Exit"
        ],
        pointer="➜",
        style=custom_style
    ).ask()

    return choice


def main():

    while True:

        UserChoice = main_menu()

        if UserChoice == "🧮 Calculator":
            from calculator import calculator
            calculator()

        elif UserChoice == "🎲 Dice Roller":
            from diceroller import dice_roller
            dice_roller()

        elif UserChoice == "🔐 Password Generator":
            from pw_gen import password_generator
            password_generator()

        elif UserChoice == "🚪 Exit":
            print("\nThanks for using Utility Box!")
            sys.exit()

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()