import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip
def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    if not character_pool:
        return "Error: No character type selected"
    return "".join(random.choice(character_pool) for _ in range(length))
def generate_and_display():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        password = generate_password(
            length, 
            use_letters_var.get(), 
            use_numbers_var.get(), 
            use_symbols_var.get()
        )
        password_display.config(state="normal")
        password_display.delete(1.0, "end")
        password_display.insert("end", password)
        password_display.config(state="disabled")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
def copy_to_clipboard():
    pyperclip.copy(password_display.get(1.0, "end").strip())
    messagebox.showinfo("Clipboard", "Password copied to clipboard!")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.configure(bg="#ffcccb")
style_options = {"bg": "#ffcccb", "fg": "#000000", "font": ("Times", 12)}
button_options = {"bg": "#add8e6", "fg": "#000000", "font": ("Times", 12), "activebackground": "#87ceeb"}
tk.Label(root, text="Password Length:", **style_options).pack(pady=5)
length_entry = tk.Entry(root, font=("Times", 12), width=10, justify="center")
length_entry.pack(pady=5)
length_entry.insert(0, "12")
use_letters_var = tk.BooleanVar(value=True)
use_numbers_var = tk.BooleanVar(value=True)
use_symbols_var = tk.BooleanVar(value=True)
for text, var in [("Include Letters", use_letters_var), ("Include Numbers", use_numbers_var), ("Include Symbols", use_symbols_var)]:
    tk.Checkbutton(root, text=text, variable=var, **style_options, selectcolor="#ffcccb").pack(anchor="center")
tk.Button(root, text="Generate Password", command=generate_and_display, **button_options).pack(pady=10)
password_display = tk.Text(root, font=("Times", 14, "bold"), height=1, width=30, state="disabled", bg="#ffffff", fg="#e74c3c")
password_display.pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, **button_options).pack(pady=5)
root.mainloop()