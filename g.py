import tkinter as tk
from PIL import Image, ImageTk
import random

# Determine the correct resampling filter depending on Pillow version
try:
    resample_filter = Image.Resampling.LANCZOS
except AttributeError:
    resample_filter = Image.LANCZOS

# Set the path to your background image
image_path = "photo.jpg"

# Initialize the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
small_geometry = "350x400"
root.geometry(small_geometry)
root.resizable(True, True)

# Track fullscreen state
is_fullscreen = False

# Function to resize and apply the background image
def update_background():
    if root.attributes("-fullscreen"):
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    else:
        w, h = 350, 400

    try:
        bg_img = Image.open(image_path).resize((w, h), resample_filter)
        bg_photo = ImageTk.PhotoImage(bg_img)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo
    except Exception as e:
        print("Error loading background image:", e)

# Load initial background
try:
    bg_img = Image.open(image_path).resize((350, 400), resample_filter)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print("Error loading background image:", e)
    root.configure(bg="darkslateblue")

# UI elements
heading = tk.Label(root, text="PLAY", font=("Arial", 32, "bold"), fg="white", bg="black")
heading.place(relx=0.5, rely=0.03, anchor="n")

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="yellow", bg="black")
result_label.place(relx=0.5, rely=0.75, anchor="center")

score_label = tk.Label(root, text="You: 0  Computer: 0", font=("Arial", 12, "bold"), fg="yellow", bg="black")
score_label.place(relx=0.5, rely=0.85, anchor="center")

# Game logic
user_score = 0
computer_score = 0
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

def play(user_choice):
    global user_score, computer_score
    comp_choice = random.randint(1, 3)
    user_str = choices[user_choice]
    comp_str = choices[comp_choice]

    if user_str == comp_str:
        outcome = "Tie!"
    elif (user_str == "Rock" and comp_str == "Scissors") or \
         (user_str == "Paper" and comp_str == "Rock") or \
         (user_str == "Scissors" and comp_str == "Paper"):
        outcome = "You Win!"
        user_score += 1
    else:
        outcome = "Computer Wins!"
        computer_score += 1

    result_label.config(text=f"You: {user_str}\nComputer: {comp_str}\n{outcome}")
    score_label.config(text=f"You: {user_score}  Computer: {computer_score}")

# Game buttons
btn_frame = tk.Frame(root, bg="black")
btn_frame.place(relx=0.5, rely=0.4, anchor="center")

tk.Button(btn_frame, text="Rock (1)", command=lambda: play(1), width=10).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Paper (2)", command=lambda: play(2), width=10).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Scissors (3)", command=lambda: play(3), width=10).grid(row=0, column=2, padx=5, pady=5)

# Fullscreen toggle
def toggle_fullscreen():
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    root.attributes("-fullscreen", is_fullscreen)
    if not is_fullscreen:
        root.geometry(small_geometry)
    update_background()

tk.Button(root, text="Toggle Fullscreen", command=toggle_fullscreen, bg="gray", fg="white").place(relx=0.95, rely=0.03, anchor="ne")

root.mainloop()