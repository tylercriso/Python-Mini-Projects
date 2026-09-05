import random

play_index = 0

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100 (you have " + str(5 - attempts) + " attempts to get it right): "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

        if attempts >= 5:
            print(f"Sorry! You've used all 5 attempts. The number was {number_to_guess}.")
            break
    global play_index
    play_index += 1

if play_index == 0:
    play_game()

while play_index != 0:
    continue_playing = input("Do you want to play again? (y/n): ")
    if continue_playing.lower() == "y":
        play_game()
    else:
        print("Game ended.")
        break

