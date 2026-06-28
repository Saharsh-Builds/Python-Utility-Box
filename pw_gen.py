import random
import secrets
import string
import questionary


custom_style = questionary.Style([
    ("qmark", "fg:#5fd7ff bold"),
    ("question", "bold"),
    ("pointer", "fg:#ff5f87 bold"),
    ("highlighted", "fg:#00ff87 bold"),
    ("selected", "fg:#00ff87"),
    ("answer", "fg:#ffd75f bold"),
])


def generate_random_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def generate_personalized_password(user_details, word_count=4, separator="-", use_numbers=True, use_symbols=True):
    cleaned_details = []
    for detail in user_details:
        if detail:
            cleaned = "".join(char for char in detail.lower() if char.isalnum())
            if cleaned:
                cleaned_details.append(cleaned)

    if not cleaned_details:
        cleaned_details = ["secret", "user", "safe"]

    selected_words = cleaned_details[:word_count]

    while len(selected_words) < word_count:
        selected_words.append("secure")

    password = separator.join(selected_words)

    if use_numbers:
        password = f"{password}{separator}{random.randint(10, 99)}"

    if use_symbols:
        symbols = ["!", "@", "#", "$", "%", "&", "*"]
        password = f"{password}{separator}{random.choice(symbols)}"

    if len(password) > 80:
        password = password[:80]

    return password


def get_password_length():
    while True:
        answer = questionary.text(
            "How many characters should the password have? (8-80)",
            style=custom_style
        ).ask()

        try:
            length = int(answer)
            if 8 <= length <= 80:
                return length
            print("Password length must be between 8 and 80 characters.")
        except ValueError:
            print("Please enter a valid number!")


def get_word_count():
    while True:
        answer = questionary.text(
            "How many words should it have? (2-10)",
            style=custom_style
        ).ask()

        try:
            word_count = int(answer)
            if 2 <= word_count <= 10:
                return word_count
            print("Word count must be between 2 and 10.")
        except ValueError:
            print("Please enter a valid number!")


def password_generator():
    while True:
        print("\n🔐 Password Generator")
        print("────────────────────")

        choice = questionary.select(
            "Choose a password style:",
            choices=[
                "Random Encrypted Password",
                "Personalized Password",
                "⬅ Back"
            ],
            pointer="❯",
            style=custom_style
        ).ask()

        if choice == "Random Encrypted Password":
            length = get_password_length()
            use_symbols = questionary.confirm(
                "Include symbols?",
                default=True,
                style=custom_style
            ).ask()

            password = generate_random_password(length=length, use_symbols=use_symbols)
            print(f"\nGenerated Password: {password}")
            input("\nPress Enter to continue...")

        elif choice == "Personalized Password":
            name = questionary.text("What is your name?", style=custom_style).ask()
            color = questionary.text("What is your favorite color?", style=custom_style).ask()
            pet_name = questionary.text("What is your pet's name? (optional)", style=custom_style).ask()
            hobby = questionary.text("What is a hobby you enjoy? (optional)", style=custom_style).ask()
            birth_year = questionary.text("What year were you born? (optional)", style=custom_style).ask()

            word_count = get_word_count()
            separator = questionary.select(
                "Choose a separator:",
                choices=["-", "_", ".", "$","#","@","%"],
                pointer="❯",
                style=custom_style
            ).ask()

            use_numbers = questionary.confirm(
                "Add random numbers?",
                default=True,
                style=custom_style
            ).ask()

            use_symbols = questionary.confirm(
                "Add symbols?",
                default=True,
                style=custom_style
            ).ask()

            password = generate_personalized_password(
                user_details=[name, color, pet_name, hobby, birth_year],
                word_count=word_count,
                separator=separator,
                use_numbers=use_numbers,
                use_symbols=use_symbols
            )
            print(f"\nGenerated Password: {password}")
            input("\nPress Enter to continue...")

        elif choice == "⬅ Back":
            break


if __name__ == "__main__":
    password_generator()
