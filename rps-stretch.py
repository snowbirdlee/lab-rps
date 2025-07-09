from dataclasses import dataclass, field
import random
import yaml
import os
from rich import print

player_stats_yaml = "player_stats.yml"

@dataclass
class GameEngine:
    moves: list[str] = field(default_factory=lambda: ["rock", "paper", "scissors"])
    
    def user_move(self):
        while True:
            user_input = input("\nWhat is your move? ").lower().strip()
            if user_input in self.moves:
                return user_input
            else:
                print("Please enter rock, paper, or scissors.")
    
    def computer_move(self):
        return random.choice(self.moves) # ChatGPT. more concise
    
    def decide_winner(self, player_move: str, computer_move: str):
        player_data = self.load_stats()
        
        if player_move == computer_move:
            print("Tie!")
            player_data["ties"] += 1
            result = "tie"
        elif player_move == "rock" and computer_move == "scissors":
            print("Player wins!")
            player_data["wins"] += 1
            result = "player"
        elif player_move == "paper" and computer_move == "rock":
            print("Player wins!")
            player_data["wins"] += 1
            result = "player"
        elif player_move == "scissors" and computer_move == "paper":
            print("Player wins!")
            player_data["wins"] += 1
            result = "player"
        else:
            print("Computer wins!")
            player_data["losses"] += 1
            result = "computer"
        
        self.save_stats(player_data)
        return result
    
    def load_stats(self):
        if os.path.exists(player_stats_yaml): #autofill
            with open(player_stats_yaml, "r") as file:
                player_data = yaml.safe_load(file) or {"wins": 0, "losses": 0, "ties": 0}
        else:
            player_data = {"wins": 0, "losses": 0, "ties": 0}
        return player_data
    
    def save_stats(self, player_data):
        with open(player_stats_yaml, "w") as file:
            yaml.dump(player_data, file)
    
    def display_stats(self):
        player_data = self.load_stats()
        print(
            f"\nFinal Stats:\n"
            f"Wins: {player_data['wins']}\n"
            f"Losses: {player_data['losses']}\n"
            f"Ties: {player_data['ties']}"
        )

def clear_data():
    open(player_stats_yaml, "w").close()
    print("Stats cleared.")

def main():
    print("\nLet's do a best of 5 match!")
    player_wins = 0
    computer_wins = 0
    while True:
        game = GameEngine()
        player_move = game.user_move()
        computer_move = game.computer_move()
        print(f"Computer chose: {computer_move}")
        result = game.decide_winner(player_move, computer_move)
        if result == "player":
            player_wins += 1
        elif result == "computer":
            computer_wins += 1
            
        if player_wins == 3:
            print("[bold green]Player won this match![/bold green]")
            break
        elif computer_wins == 3:
            print("[bold magenta]Computer won this match![/bold magenta]")
            break

    game.display_stats()

    while True:
        player_wants_clear = input("Would you like to clear your stats? (y/n) ").strip().lower()
        if player_wants_clear in ["yes", "y"]:
            clear_data()
            break  
        elif player_wants_clear in ["no", "n"]:
            print("Ok. Data kept.")
            break
        else:
            print("Please enter yes or no.")

if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors!")
    while True:
        main()
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again in ["yes", "y"]:
            continue
        elif play_again in ["no", "n"]:
            print("Thanks for playing!")
            break    
        else:
            print("Please enter yes or no.")
