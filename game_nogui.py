import random

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
    
def start_game():
    secret_number = random.randint(1, 100)
    history_stack = Stack()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    playing = True

    while playing:
        try:
            guess = int(input("\nEnter your guess: "))
            history_stack.push(guess)
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {history_stack.size} attempts.")
                print(f"Your guess path (newest first): {history_stack.display_history()}")
                playing = False
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    start_game()