# Number Guessing Game by Paaras Purohit

This README is both the report and the instructions on how to run the game.

### Preface: How to Run the Game

The game can be run on any machine that has Python installed. Here are the steps to download this repo and play the game:

1. Clone the repository or download the file called ```game_final.py```
2. Run the file, either through the terminal or through an IDE (e.g. VS Code)
3. Have fun!

### Getting Started

A number-guessing game has very simple logic. There's a range of numbers that a host can choose a random number from. When it does, the user has to try to guess that number, to which they will receive feedback on whether they guessed too high or low. Once they guess the number, they win. Simple logic like that can be made by the following:

```python
import random

num = random.randint(1, 100)

guess = int(input("Guess the number >>"))
while guess != num:
    if guess > num:
        print("Too high")
        guess = int(input("Guess the number >>"))
    elif guess < num:
        print("Too low")
        guess = int(input("Guess the number >>"))
```

### Implementing In-Class Concepts

While the code above technically is a number-guessing game, it can be made better. Not necessarily by optimizing it, but through implementing core concepts learned in CMPSC 132, we can use the game to show our understanding and grasp of data structures and object-oriented programming.

Three concepts we can use in our number guessing game are:

1. Classes (object-oriented programming)
2. Linked lists
3. The stack

To start, the first class we'll make is the Node class, which is essential for the linked list (and also is a class):

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

From there, we can make a LinkedList class:

```python
class LinkedList:
    def __init__(self):
        self.top = None
        self.size = 0
```

But since the linked list is supposed to be used for the stack, let's rename the class to Stack. We also need to add a push() method as follows to add guesses to the top of the stack:

```python
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
```

I was going to add the peek() and pop() methods, but we never need to delete anything from the stack, so the pop() method wouldn't make sense here. Also, the peek() method is good, but it would be better to see the entire list of all of the user's guesses. We can do this by looping through the linked list and displaying every element through this Stack method:

```python
def display_history(self):
        current = self.top
        history = []
        while current:
            history.append(str(current.data))
            current = current.next
        return " -> ".join(history) if history else "No guesses yet."
```

Once we have a valid Stack class, we can modify our original game logic:

```python
secret_number = random.randint(1, 100)
history_stack = Stack()
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while playing:
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
```

Similar to how we tested our code with docstrings using a main method, we can also wrap our game into a function and call it in a main method. Also, we should handle cases where the user enters something other than an integer. So, now it looks like this:

```python
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
```

### Making a GUI

I wanted this game to be played beyond just a console, as most games are played with graphical UI. GUI was then the next step for this game, but I didn't know where to start.

After doing some research, I learned that Python has a library called TKinter, which is Python's GUI library. I played around with the library and documentation, and was able to first make a simple desktop app, where the user clicks a button and sees the text change:

```python
import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()
```

Now that I had an understanding of how to use TKinter on a basic level, it was time to implement it into the game.

The elements needed for the GUI are:
- Title
- Subtitle
- Input box
- Submit button
- Feedback text (too high or too low)
- Guess history (text)

We can create a class called ```GuessingGameUI``` for this:

```python
class GuessingGameGUI:
    def __init__(self, root):

        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("600x400")

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
```

Next, the elements need to change based on user input. The feedback needs to reflect the most recent guess, and the guess history needs to be updated accordingly. I created a ```check_guess()``` method, which uses previously coded game logic to update each element accordingly:

```python
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
```

Now, our main method looks like this:

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameGUI(root)
    root.mainloop()
```

### Adding Difficulty

Adding difficulty for the game meant increasing or decreasing the range. The instructions were that there were three levels of difficulty.  As for the UI, I was unsure how to do this. I ended up settling on a dropdown menu. First, we added a difficulty dictionary to the ```GuessingGameUI``` class, along with a dropdown for the user:

```python
self.difficulty_levels = {
    "Easy (1-50)": 50,
    "Medium (1-100)": 100,
    "Hard (1-500)": 500,
    "Insane (1-1000)": 1000
}

self.selected_difficulty = tk.StringVar(value="Medium (1-100)")
self.max_number = self.difficulty_levels[self.selected_difficulty.get()]

self.dropdown = tk.OptionMenu(
    root, 
    self.selected_difficulty, 
    *self.difficulty_levels.keys(),
    command=self.change_difficulty
)
self.dropdown.pack(pady=5)

def change_difficulty(self, value):
    self.max_number = self.difficulty_levels[value]
    self.restart_game()
```

### Limiting Attempts (Attempts Remaining & Replay)

This meant creating a ```restart()``` method, which reset all of the game pieces:

```python
def restart_game(self):
    self.secret_number = random.randint(1, self.max_number)
    self.history_stack = Stack()
    self.label_feedback.config(text="")
    self.label_history.config(text="History: No guesses yet.")
    self.label_instruction.config(text=f"Guess a number (1–{self.max_number})")
    self.button_guess.config(state=tk.NORMAL)
    self.entry_guess.delete(0, tk.END)
```

The rest of the attempt logic included creating a ```MAX_ATTEMPTS``` constant (set to 10), creating a new label for the attempts that remain, and revealing the number when the attempts are done.

### Conclusion & Testing

![demonstration](<Screenshot 2026-04-26 at 17.51.24.png>)

Any simple project can be enhanced not for the sake of optimzation always, but sometimes to demonstrate a skill that someone might have learned. Classes and stacks aren't a required feature for a number-guessing game, but to show my understanding of those concepts learned in CS 132, we can be challenged to implement them, which was my goal with this project.

I chose the number-guessing game because it was a blank canvas to me, something that I could easily fill with different things about computer science principles that I learned throughout the course. It also gave me a chance to go above and beyond. Although we never covered GUI's in this course, it was still something extra I could do for the game that made it more fun, and also something that I could use to learn both the topic itself and how to do independent research on something I didn't know about before.