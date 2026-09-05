import random

while input("Do you want to play? (yes/no): ").lower() == "yes":

    playerChoice = input("Enter your choice (Rock, Paper, Scissors): ")
    playerChoice = playerChoice.capitalize()

    computerChoice = random.choice(["Rock", "Paper", "Scissors"])

    whoWins = str()

    match playerChoice:
        case "Rock":
            if computerChoice == "Rock":
                whoWins = "tie"
            elif computerChoice == "Paper":
                whoWins = "computer"
            else:
                whoWins = "player"
        case "Paper":
            if computerChoice == "Rock":
                whoWins = "player"
            elif computerChoice == "Paper":
                whoWins = "tie"
            else:
                whoWins = "computer"
        case "Scissors":
            if computerChoice == "Rock":
                whoWins = "computer"
            elif computerChoice == "Paper":
                whoWins = "player"
            else:
                whoWins = "tie"
        case _:
            whoWins = "invalid"

    print(f"Player chose: {playerChoice}")
    print(f"Computer chose: {computerChoice}")
    print(" ")

    match whoWins:
        case "player":
            print("Player wins!")
        case "computer":
            print("Computer wins!")
        case "tie":
            print("It's a tie!")
        case _:
            print("An unexpected error occurred.")

else:
    print("Thanks for playing!")