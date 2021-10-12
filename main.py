from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=525)
padlock_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=padlock_img)
canvas.grid(column=0, row=0, columnspan=2)

window.mainloop()