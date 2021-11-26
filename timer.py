from tkinter import *

x=0
def run_counter(lab):
    def counting():
        global x
        x+=1
        lab.config(text=str(x))
        lab.after(1000, counting)
    counting()

window = Tk()
window.title('Demo 02')
window.geometry("500x400+100+50")
lab0 = Label(window, width=15, height =3,
                bg = "#ccddef",
                text="cursor:\nbottom_left_corner",
                justify="center",
                font="Arial 20 bold",
                cursor="bottom_left_corner"
                )
lab0.pack()
run_counter(lab0)
btnExit = Button(window, width=15, height=2,
                text="Exit",
                foreground="ff2233",
                font="Arial 20 bold",
                command=window.destroy)
btnExit.pack(pady=10)

window.mainloop()