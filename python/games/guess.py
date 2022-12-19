import tkinter as tk
import random

class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create the label to display the game instructions
        self.instructions = tk.Label(self, text="Guess a number between 1 and 10:")
        self.instructions.pack()

        # Create the entry field for the player's guess
        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack()

        # Create the submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack()

        # Create the label to display the game result
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def check_guess(self):
        # Get the player's guess
        guess = int(self.guess_entry.get())

        # Check if the guess is correct
        if guess == self.secret_num:
            self.result_label.config(text="You win!")
        else:
            self.result_label.config(text="Your guess is incorrect. Try again.")

def play_game():
    # Set up the game
    root = tk.Tk()
    app = Game(master=root)
    app.secret_num = random.randint(1, 10)  # Generate a secret number between 1 and 10
    app.mainloop()

# Start the game
play_game()
