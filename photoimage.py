from tkinter import *

window = Tk()
window.geometry("300x200+200+100")
img1 = PhotoImage(file="png-clipart-sticker-bomb-eric-cartman-thumbnail.png")
lab0 = Label(window, image=img1, bg="blue")
lab0.pack()
window.mainloop()