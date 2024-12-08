import tkinter as tk
from tkinter import messagebox
import random

num = random.randint(0, 20)

def show_name():
    name = name_entry.get()
    messagebox.showinfo("Welcome", "Well, well, well, {}, welcome to the guessing game! \nI am thinking of a number from 1 through 20.".format(name))

def show_guess():
    global num
    guess = int(guess_entry.get())
    if guess < num:
        messagebox.showinfo("Low", "Too low! \nTry again!")
    elif guess > num:
        messagebox.showinfo("High", "Too high! \nTry again!")
    else:
        messagebox.showinfo("Correct", "You got it! \nYou win!")

window = tk.Tk()
window.title("Guessing Game")
window.geometry("500x500")
window.configure(bg="azure")

name_label = tk.Label(window, text="Enter your name:", fg="black", bg="azure", font=("Helvetica", 20, "bold"))
name_label.pack(pady=30)

name_entry = tk.Entry(window, font=("Helvetica", 18), width=25)
name_entry.pack(pady=5)

ok_button = tk.Button(window, text="OK", command=show_name)
ok_button.pack(pady=30)

guess_label = tk.Label(window, text="Take a guess: ", fg="black", bg="azure", font=("Helvetica", 25, "italic"))
guess_label.pack(pady=30)

guess_entry = tk.Entry(window, font=("Helvetica", 18), width=25)
guess_entry.pack(pady=5)

guess_button = tk.Button(window, text="Guess", command=show_guess)
guess_button.pack(pady=30)

window.mainloop()