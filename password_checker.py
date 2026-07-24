common_passwords = ["password", "123456", "qwerty", "letmein", "admin", "welcome", "monkey", "dragon"]

while True:
    password = input("Enter a password to check (or type 'quit' to exit): ")

    if password.lower() == "quit":
        print("Goodbye!")
        break

    if password.lower() in common_passwords:
        print("This is one of the most common passwords in the world. Extremely weak!\n")
        continue

    length_ok = len(password) >= 8
    has_number = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_symbol = any(char in "!@#$%^&*()_+-=" for char in password)

    score = sum([length_ok, has_number, has_upper, has_symbol])

    print(f"Strength score: {score}/4")

    if score == 4:
        print("Strong password!\n")
    elif score >= 2:
        print("Medium password - could be stronger.")
        if not length_ok:
            print("- Add more characters (8+ recommended)")
        if not has_number:
            print("- Add a number")
        if not has_upper:
            print("- Add an uppercase letter")
        if not has_symbol:
            print("- Add a symbol (like ! @ # $)")
        print()
    else:
        print("Weak password. Missing:")
        if not length_ok:
            print("- At least 8 characters")
        if not has_number:
            print("- A number")
        if not has_upper:
            print("- An uppercase letter")
        if not has_symbol:
            print("- A symbol (like ! @ # $)")
        print()