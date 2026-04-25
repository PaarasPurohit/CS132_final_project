import tkinter as tk

def on_button_click():
    # Update the label text when button is clicked
    label.config(text="Button Clicked!")

# 1. Create the main application window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200") # Set width x height

# 2. Add a Label widget
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20) # 'pack' adds the widget to the window

# 3. Add a Button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# 4. Start the main event loop
root.mainloop()
