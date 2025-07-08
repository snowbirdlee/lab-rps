from dataclasses import dataclass, field
import random


@dataclass
class GameEngine:
    user_input: str = field(default="", init=False)  # we don’t want it to be passed into __init__
    moves: list[str] = field(default_factory=lambda: ["rock", "paper", "scissors"])

    
    def user_move(self):
        while True:
            user_input = input("What is your move? ").lower().strip()
            if user_input in self.moves:
                return user_input
            else:
                print("Please enter rock, paper, or scissors.")
    
    def computer_move(self):
        move = random.randint(0, 2)
        return self.moves[move]
    
    def decide_winner(self, player_move: str, computer_move: str):
        if player_move == computer_move:
            print("Tie!")
        elif player_move == "rock" and computer_move == "scissors":
            print("Player wins!")
        elif player_move == "paper" and computer_move == "rock":
            print("Player wins!")
        elif player_move == "scissors" and computer_move == "paper":
            print("Player wins!")
        else:
            print("Computer wins!")
    
    

def main():
    print("Welcome to Rock Paper Scissors!")
    while True:
        game = GameEngine()
        player_move = game.user_move()
        computer_move = game.computer_move()
        print(f"Computer chose: {computer_move}")
        game.decide_winner(player_move, computer_move)
        
        while True:
            play_again = input("Play again? (yes/no): ").strip().lower()

            if play_again == "yes" or play_again == "y":
                break
            elif play_again == "no" or play_again == "n":
                print("Thanks for playing!")
                return
            else:
                print("Please enter yes or no.")

if __name__ == "__main__":
    main()
