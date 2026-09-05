import random

index = 0

def generate_password():
    length = int(input("Enter the desired password length: "))

    isNumeric = str.lower(input("Should the password include numbers? (y/n): "))
    isSpecial = str.lower(input("Should the password include special characters? (y/n): "))
    isCapital = str.lower(input("Should the password include capital letters? (y/n): "))

    global index

    characters = "abcdefghijklmnopqrstuvwxyz"

    if isNumeric == "y":
        characters += "0123456789"
    if isSpecial == "y":
        characters += "!@#$%^&*()"
    if isCapital == "y":
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    password = "".join(random.choice(characters) for _ in range(length))

    print(password)

    index += 1

if index == 0:
    generate_password()

while index != 0:
    continue_generation = input("Do you want to generate another password? (y/n): ")
    if continue_generation.lower() == "y":
        generate_password()
    else:
        print("Password generation ended.")
        break