from tkinter import *

window = Tk()
window.title("Label demo")
window.geometry("350x440+300+100")
lab1 = Label(window, bitmap="hourglass", bg="#ccddee",
            text="FengChia University", compound=LEFT)
lab2 = Label(window, bitmap="hourglass", bg="#ccddee",
            text="FengChia University", compound="right")
lab3 = Label(window, bitmap="hourglass", bg="#ccddee",
            text="FengChia University", compound=TOP)

lab4 = Label(window, bitmap="hourglass", bg="#ccddee",
            text="FengChia University", compound="bottom")
lab5 = Label(window, bitmap="hourglass", bg="#ccddee",
            text="FengChia University", compound="center")

lab1.pack()
lab2.pack()
lab3.pack()
lab4.pack()
lab5.pack()
window.mainloop()