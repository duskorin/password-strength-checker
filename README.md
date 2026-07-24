# Password Strength Checker

A simple command-line tool built in Python that checks whether a password is strong enough, and tells you exactly what's missing if it's not.

## What it checks
- Minimum length (8+ characters)
- At least one number
- At least one uppercase letter
- At least one symbol
- Whether it's a commonly used/leaked password

## Scoring
Gives a score out of 4 based on the criteria above, plus a special warning if the password is found in a list of common weak passwords.

## How to run it
1. Make sure you have Python installed
2. Run the script:
3. Enter a password when prompted. Type `quit` to exit.

## What I learned
This was my first Python project. I learned about:
- Variables and user input
- If/else conditionals
- Generator expressions (`any()`)
- Loops (`while True`)
- Basic string methods
- Lists and the `in` operator
- f-strings

## Future improvements
- Load a much larger common-password list from a file instead of hardcoding it
- Add a GUI version
- Estimate time-to-crack based on password complexity