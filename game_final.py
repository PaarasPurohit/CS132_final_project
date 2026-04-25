import random
import tkinter as tk

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

        self.secret_number = random.randint(1, 100)
        self.history_stack = Stack()

        self.label_title = tk.Label(root, text="Guess a number (1–100)", font=("Arial", 14))
        self.label_title.pack(pady=10)

        self.entry_guess = tk.Entry(root)
        self.entry_guess.pack(pady=5)

        self.button_guess = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button_guess.pack(pady=5)

        self.label_feedback = tk.Label(root, text="")
        self.label_feedback.pack(pady=5)

        self.label_history = tk.Label(root, text="History: No guesses yet.")
        self.label_history.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.history_stack.push(guess)

            if guess < self.secret_number:
                self.label_feedback.config(text="Too low!")
            elif guess > self.secret_number:
                self.label_feedback.config(text="Too high!")
            else:
                self.label_feedback.config(
                    text=f"Correct! {self.history_stack.size} attempts."
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