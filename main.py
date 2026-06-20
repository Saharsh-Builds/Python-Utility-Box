import questionary
import sys




def main_menu():
    while True:
        
        custom_style = questionary.Style([
        ('highlighted', 'bold'),
        ])

        Choice = questionary.select(
            "Please select an Utility tool and press Enter to continue: ",
            choices=[
                "1. Calculator",
                "2. Dice Roller",
                "3. Password Generator",
                "4. Exit"
            ],
            pointer= ">",
            style=custom_style
        ).ask()

        return Choice

        
def main():
    while True:
        
        
        UserChoice = main_menu()


        if UserChoice == "1. Calculator":
            from calculator import calculator
            calculator()

        elif UserChoice == "2. Dice Roller":
            from diceroller import dice_roller
            dice_roller()
        
        elif UserChoice == "3. Password Generator":
            from pw_gen import password_generator          
            password_generator()

        elif UserChoice == "4. Exit":
            print("Exiting the program. Goodbye!")
            sys.exit()

        else:
            print("How did you get here? Please select a valid option from the menu.")
            main()









if __name__ == "__main__":
    main()