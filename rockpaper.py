import random

print("Welcome to Rock-Paper-Scissors Game " )


user_score = 0
computer_score = 0


while True:
    print("\nChoices: rock, paper, scissors")
    user_choice = input("Enter your choice: ").lower()
    
    # Validate input
    if user_choice not in ["rock", "paper", "scissors"]:
        print(" Invalid choice! Please choose rock, paper, or scissors.")
        continue
    
    # Computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f" You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine winner
    if user_choice == computer_choice:
        print(" It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print(" You win this round!")
        user_score += 1
    else:
        print(" Computer wins this round!")
        computer_score += 1
    
    # Display scores
    print(f" Score -> You: {user_score} | Computer: {computer_score}")
    
    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Scores:")
        print(f" You: {user_score}")
        print(f"💻 Computer: {computer_score}")
        print("Thanks for playing! Goodbye.")
        break
