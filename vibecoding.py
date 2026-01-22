import tkinter as tk
import random
import pyperclip
from datetime import date

# ---------------- CATEGORY WISE QUOTES ---------------- #

categories = [
    "Study",
    "Positivity",
    "Success",
    "Self-Love",
    "Happy"
]

quotes_by_category = {
    "Study": [
        "Study hard today for a better tomorrow.",
        "Learning never exhausts the mind.",
        "Focus now, shine later."
    ],
    "Positivity": [
        "Choose positivity every day.",
        "Good things are coming.",
        "Positive mind, positive life."
    ],
    "Success": [
        "Success comes with consistency.",
        "Hard work creates success.",
        "Failure is part of success."
    ],
    "Self-Love": [
        "You are enough just as you are.",
        "Be kind to yourself.",
        "Love yourself first."
    ],
    "Happy": [
        "Celebrate the small joys.",
        "Happiness grows with gratitude.",
        "Joy is found in little things."
    ]
}

# ---------------- TRACKING VARIABLES ---------------- #

used_quotes = {cat: [] for cat in categories}
current_category_index = 0
last_shown_date = None

# ---------------- FUNCTIONS ---------------- #

def get_next_daily_quote():
    global current_category_index

    category = categories[current_category_index]
    remaining_quotes = [
        q for q in quotes_by_category[category]
        if q not in used_quotes[category]
    ]

    # If all quotes in this category are used, move to next category
    if not remaining_quotes:
        used_quotes[category] = []
        current_category_index = (current_category_index + 1) % len(categories)
        return get_next_daily_quote()

    quote = random.choice(remaining_quotes)
    used_quotes[category].append(quote)

    return f"📌 {category} Quote:\n\n{quote}"

def show_daily_quote():
    global last_shown_date, current_category_index

    today = date.today()

    # Show quote only once per day
    if last_shown_date != today:
        daily_quote = get_next_daily_quote()
        quote_label.config(text=daily_quote)
        status_label.config(text="🌞 Today's Motivation")
        last_shown_date = today

        # Prepare next category for next day
        current_category_index = (current_category_index + 1) % len(categories)

def next_quote():
    # Optional manual browsing (does not affect daily rule)
    quote_label.config(text=get_next_daily_quote())
    status_label.config(text="Manual Quote View")

def share_quote():
    pyperclip.copy(quote_label.cget("text"))
    status_label.config(text="Quote copied! Share it 📤")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Daily Motivation App")
root.geometry("520x360")
root.configure(bg="#F5F5F5")

quote_label = tk.Label(
    root,
    text="🌅 Welcome!\nYour daily quote will appear here.",
    wraplength=460,
    font=("Helvetica", 14),
    bg="#F5F5F5",
    fg="#333",
    justify="center"
)
quote_label.pack(pady=40)

button_frame = tk.Frame(root, bg="#F5F5F5")
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Next ➡️",
    font=("Arial", 11),
    command=next_quote
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Share 📤",
    font=("Arial", 11),
    command=share_quote
).grid(row=0, column=1, padx=10)

status_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    bg="#F5F5F5",
    fg="green"
)
status_label.pack()

# Show quote ONCE per day when app opens
show_daily_quote()

root.mainloop()