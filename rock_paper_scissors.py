import random
import sys

# Game constants
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
VALID_CHOICES = [ROCK, PAPER, SCISSORS]

def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    return random.choice(VALID_CHOICES)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the round.
    
    Returns:
        str: 'user', 'computer', or 'tie'
    """
    if user_choice == computer_choice:
        return 'tie'
    
    # Rock beats scissors, scissors beat paper, paper beats rock
    if (user_choice == ROCK and computer_choice == SCISSORS) or \
       (user_choice == SCISSORS and computer_choice == PAPER) or \
       (user_choice == PAPER and computer_choice == ROCK):
        return 'user'
    
    return 'computer'

def parse_user_choice(user_input):
    """
    Parses and normalizes the user's input.
    
    Returns:
        str or None: The normalized choice (ROCK, PAPER, SCISSORS) or None if invalid.
    """
    val = user_input.strip().lower()
    if val in ('r', 'rock'):
        return ROCK
    if val in ('p', 'paper'):
        return PAPER
    if val in ('s', 'scissors'):
        return SCISSORS
    return None

def get_yes_no(prompt, default=True):
    """Prompts the user for a yes/no input, returning a boolean."""
    default_str = " [Y/n]" if default else " [y/N]"
    while True:
        choice = input(prompt + default_str + ": ").strip().lower()
        if not choice:
            return default
        if choice in ('y', 'yes'):
            return True
        if choice in ('n', 'no'):
            return False
        print("Invalid input. Please enter 'y' or 'n'.")

def main():
    print("========================================")
    print("       Rock-Paper-Scissors Game         ")
    print("========================================")
    print("Instructions:")
    print("  Enter 'rock' (or 'r'), 'paper' (or 'p'), or 'scissors' (or 's').")
    print("  Type 'q' or 'quit' to exit the game at any time.\n")
    
    user_score = 0
    computer_score = 0
    ties = 0
    round_num = 1
    
    while True:
        print(f"--- Round {round_num} ---")
        user_input = input("Choose Rock, Paper, or Scissors: ").strip()
        if user_input.lower() in ('q', 'quit'):
            break
            
        user_choice = parse_user_choice(user_input)
        if not user_choice:
            print("Invalid choice. Please choose Rock, Paper, or Scissors (or r/p/s).\n")
            continue
            
        computer_choice = get_computer_choice()
        
        # Emoji representation for clear feedback
        emojis = {
            ROCK: "🪨 (Rock)",
            PAPER: "📄 (Paper)",
            SCISSORS: "✂️ (Scissors)"
        }
        
        print(f"You chose: {emojis[user_choice]}")
        print(f"Computer chose: {emojis[computer_choice]}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == 'user':
            print("🎉 You win this round!")
            user_score += 1
        elif result == 'computer':
            print("💻 Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a tie!")
            ties += 1
            
        print(f"\nScoreboard: You {user_score} - {computer_score} Computer (Ties: {ties})")
        print("-" * 40)
        
        round_num += 1
        
        if not get_yes_no("Do you want to play another round?"):
            break
        print()
        
    # Check if any rounds were actually completed
    total_rounds = round_num - 1
    if total_rounds > 0:
        print("\n========================================")
        print("              Final Score               ")
        print("========================================")
        print(f"Total Rounds Played: {total_rounds}")
        print(f"Your Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        print(f"Ties: {ties}")
        
        if user_score > computer_score:
            print("\n🏆 Congratulations! You won the game!")
        elif computer_score > user_score:
            print("\n😢 The computer won the game. Better luck next time!")
        else:
            print("\n🤝 The game ended in a tie!")
    
    print("\nThank you for playing Rock-Paper-Scissors. Goodbye!")

if __name__ == "__main__":
    main()
