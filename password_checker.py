while True:
    password = input("Enter a password to check (or type 'quit' to exit): ")

    if password.lower() == "quit":
        print("Goodbye!")
        break

    length_ok = len(password) >= 8
    has_number = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_symbol = any(char in "!@#$%^&*()_+-=" for char in password)

    if length_ok and has_number and has_upper and has_symbol:
        print("Strong password!\n")
    else:
        print("Password needs improvement. Missing:")
        if not length_ok:
            print("- At least 8 characters")
        if not has_number:
            print("- A number")
        if not has_upper:
            print("- An uppercase letter")
        if not has_symbol:
            print("- A symbol (like ! @ # $)")
        print()