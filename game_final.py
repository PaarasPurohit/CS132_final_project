import random
import tkinter as tk

MAX_ATTEMPTS = 10

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def display_history(self):
        current = self.top
        history = []
        while current:
            history.append(str(current.data))
            current = current.next
        return " -> ".join(history) if history else "No guesses yet."


class GuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.difficulty_levels = {
            "Easy (1-50)": 50,
            "Medium (1-100)": 100,
            "Hard (1-500)": 500,
            "Insane (1-1000)": 1000
        }

        self.selected_difficulty = tk.StringVar(value="Medium (1-100)")
        self.max_number = self.difficulty_levels[self.selected_difficulty.get()]

        self.secret_number = random.randint(1, self.max_number)
        self.history_stack = Stack()

        tk.Label(root, text="Number Guessing Game", font=("Arial", 16)).pack(pady=10)

        tk.OptionMenu(
            root,
            self.selected_difficulty,
            *self.difficulty_levels.keys(),
            command=self.change_difficulty
        ).pack(pady=5)

        self.label_instruction = tk.Label(root, text=f"Guess a number (1–{self.max_number})")
        self.label_instruction.pack(pady=5)

        self.entry_guess = tk.Entry(root)
        self.entry_guess.pack(pady=5)

        self.button_guess = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button_guess.pack(pady=5)

        tk.Button(root, text="Restart Game", command=self.restart_game).pack(pady=5)

        self.label_feedback = tk.Label(root, text="")
        self.label_feedback.pack(pady=5)

        self.label_attempts = tk.Label(root, text=f"Attempts left: {MAX_ATTEMPTS}")
        self.label_attempts.pack(pady=5)

        self.label_history = tk.Label(root, text="History: No guesses yet.")
        self.label_history.pack(pady=10)

    def change_difficulty(self, value):
        self.max_number = self.difficulty_levels[value]
        self.restart_game()

    def restart_game(self):
        self.secret_number = random.randint(1, self.max_number)
        self.history_stack = Stack()

        self.label_feedback.config(text="")
        self.label_history.config(text="History: No guesses yet.")
        self.label_instruction.config(text=f"Guess a number (1–{self.max_number})")
        self.label_attempts.config(text=f"Attempts left: {MAX_ATTEMPTS}")

        self.button_guess.config(state=tk.NORMAL)
        self.entry_guess.delete(0, tk.END)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())

            if guess < 1 or guess > self.max_number:
                self.label_feedback.config(
                    text=f"Enter a number between 1 and {self.max_number}!"
                )
                return

            self.history_stack.push(guess)

            attempts_used = self.history_stack.size
            attempts_left = MAX_ATTEMPTS - attempts_used

            if guess < self.secret_number:
                self.label_feedback.config(text="Too low!")
            elif guess > self.secret_number:
                self.label_feedback.config(text="Too high!")
            else:
                self.label_feedback.config(
                    text=f"Correct! You won in {attempts_used} attempts."
                )
                self.button_guess.config(state=tk.DISABLED)

            self.label_attempts.config(text=f"Attempts left: {attempts_left}")

            if attempts_left == 0 and guess != self.secret_number:
                self.label_feedback.config(
                    text=f"You lost! The number was {self.secret_number}."
                )
                self.button_guess.config(state=tk.DISABLED)

            history_text = self.history_stack.display_history()
            self.label_history.config(text=f"History: {history_text}")

            self.entry_guess.delete(0, tk.END)

        except ValueError:
            self.label_feedback.config(text="Enter a valid integer!")


if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameGUI(root)
    root.mainloop()