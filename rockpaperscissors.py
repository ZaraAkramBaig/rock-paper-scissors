import tkinter as tk
import random

class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.computer_choice = random.choice(self.choices)
        self.user_choice = None
        self.user_wins = 0
        self.computer_wins = 0

    def play(self, user_choice):
        self.user_choice = user_choice
        self.computer_choice = random.choice(self.choices)  # Generate a new computer choice each round

        if self.user_choice == self.computer_choice:
            result = "It's a tie!"
        elif (self.user_choice == "rock" and self.computer_choice == "scissors") or \
             (self.user_choice == "scissors" and self.computer_choice == "paper") or \
             (self.user_choice == "paper" and self.computer_choice == "rock"):
            self.user_wins += 1
            result = f"You win! {self.user_choice.capitalize()} beats {self.computer_choice.capitalize()}."
        else:
            self.computer_wins += 1
            result = f"You lose! {self.computer_choice.capitalize()} beats {self.user_choice.capitalize()}."
        
        return result

    def score_card(self):
        return f"User wins: {self.user_wins} | Computer wins: {self.computer_wins}"

    def reset(self):
        self.computer_choice = random.choice(self.choices)
        self.user_choice = None
        self.user_wins = 0
        self.computer_wins = 0

# Initialize the game object
game = Game()

# Initialize the GUI application
root = tk.Tk()
root.title("Rock Paper Scissors")

# Functions to handle button clicks
def on_choice(choice):
    result = game.play(choice)
    result_label.config(text=result)
    score_label.config(text=game.score_card())

def reset_game():
    game.reset()  # Calls the reset method correctly
    result_label.config(text="Make your move!")
    score_label.config(text="User wins: 0 | Computer wins: 0")

# GUI components
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16)).pack(pady=10)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 12))
result_label.pack(pady=10)

# Buttons for each choice
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: on_choice("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: on_choice("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: on_choice("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Score label
score_label = tk.Label(root, text="User wins: 0 | Computer wins: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

