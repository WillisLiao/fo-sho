from tkinter import *

window = Tk()
window.title("Label demo")
window.geometry("350x440+300+100")
lab = Label(window,
            text="The THE report announced AU is ranked among th list of high-impact universities in the world, No. 11 in Taiwan.",
            anchor="nw",
            width=25,
            height=20,
            wraplength=120,
            justify=RIGHT,
            font="Helvetica 20 bold",
            background="#ccffdd",
            foreground="#0000ff")
lab.pack()
window.mainloop()