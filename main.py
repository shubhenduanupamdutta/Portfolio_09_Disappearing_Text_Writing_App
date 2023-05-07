from tkinter import Tk
import time


# -------------- CONSTANTS ------------------#

WIDTH: int = 1000
HEIGHT: int = 500

# -------------- FUNCTIONALITY --------------#

start_time = time.time()


# -------------- UI SETUP -------------------#

window = Tk()
window.title("Disappearing Text")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=20, pady=20)




window.mainloop()
