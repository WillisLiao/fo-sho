from tkinter import *
window = Tk()
window.geometry("225x100+570+375")
lab0 = Label(window, width=15, height=3,
             bg="#ccddef", anchor=W,
             text = "cursor:\nbased_arrow_down",
             justify="left",
             font="Arial 20 bold",
             cursor="based_arrow_down")
lab0.pack()
window.mainloop()