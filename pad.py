from tkinter import *

window = Tk()
window.title("Label demo")
window.geometry("350x440+300+100")
lab0 = Label(window, text="tkinter", relief="solid",
            bg="#ccddee", padx = 5, pady=10)
lab0.pack()
lab2 = Label(window, text="tkinter", relief="solid",
             bg="#ffddee")
lab2.pack(padx=0, pady=10)
window.mainloop()