import random


def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds: "))

    for _ in range(rounds):
        print("\nLet's play Round", _ + 1)
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result.lower():
            user_score += 1
        elif "computer" in result.lower():
            computer_score += 1

        print("Current Score:")
        print(f"You: {user_score}  Computer: {computer_score}")

    print("\nFinal Score:")
    print(f"You: {user_score}  Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations, you win!")
    elif user_score < computer_score:
        print("Computer wins! Better luck next time.")
    else:
        print("It's a tie!")


play_game()
