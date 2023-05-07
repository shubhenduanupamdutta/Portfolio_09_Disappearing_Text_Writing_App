from tkinter import *
import time

# -------------- CONSTANTS ------------------#

WIDTH: int = 1000
HEIGHT: int = 500

# -------------- FUNCTIONALITY --------------#

start_time = time.time()
last_typed_time = 0
current_typed = ""


def start_typing():
    start_button.destroy()
    global start_time
    start_time = time.time()
    typing_entry.grid()
    time_left.grid()
    typing_time.grid()
    typing_entry.focus()


def check_inactivity():
    global last_typed_time, current_typed, start_time
    inactivity_time = window.after_idle(check_inactivity)
    # print(f"current: {inactivity_time}, last: {last_typed_time}")
    time_inactive = int(inactivity_time[6:]) - int(last_typed_time[6:])
    if time_inactive < 100000:
        time_left.config(text=f" Time Left: {10.0 - time_inactive / 10000:0.2f} ")
    if time_inactive > 100000:
        current_typed = ""
        typing_entry.config(text=current_typed)
        start_time = time.time()


def key_pressed(event):
    key = event.char
    global current_typed, last_typed_time
    last_typed_time = window.after_idle(check_inactivity)
    # update typing entry
    current_typed += key
    typing_entry.config(text=current_typed)
    time_typed = time.time() - start_time

    # update typing time
    typing_time.config(text=f" Typing Time: {time_typed:.2f} ")


# -------------- UI SETUP -------------------#

window = Tk()
window.title("Disappearing Text")
window.minsize(width=WIDTH, height=HEIGHT)
window.maxsize(width=WIDTH, height=HEIGHT)
window.config(padx=20, pady=20)

# LOGO
canvas = Canvas(width=(WIDTH - 100), height=150)
logo_img = PhotoImage(file="title.png")
canvas.create_image((WIDTH - 100) / 2, 75, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

# Start Writing Button
start_button = Button(text="Start Writing", font=("Arial", 18, "bold"), background="lightgreen", command=start_typing)
start_button.grid(row=1, column=0, columnspan=2, pady=50)

# Stats
time_left = Label(text="  Time Left: 10  ", font=("DejaVu Sans Mono", 18, "bold"), foreground="red")
time_left.grid(row=1, column=0, pady=20)

typing_time = Label(text="  Typing Time: 0  ", font=("DejaVu Sans Mono", 18, "bold"), foreground="green")
typing_time.grid(row=1, column=1, pady=20)
# Writing Entry
typing_entry = Label(width=50, height=7, background='white', font=("Arial", 18, "bold"))
typing_entry.grid(row=2, column=0, columnspan=2, pady=15)

# hiding the entry and stats
typing_entry.grid_remove()
time_left.grid_remove()
typing_time.grid_remove()

# binding all the keys to a command
window.bind("<Key>", key_pressed)

window.mainloop()
