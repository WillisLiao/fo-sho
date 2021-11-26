from tkinter import *
x=0
def count(lab):
    global x
    x+=1
    lab.config( text=str(x))

def reset(lab):
    global x
    x=x-x
    lab.config(text=str(x))
window = Tk()
window.title('Demo 02')
window.geometry("500x400+100+50")
lab0 = Label(window, width=15, height=3,
            bg="#ccddef",
            text=str(x),
            justify="center",
            font = "Arial 20 bold",
            cursor="bottom_left_corner")
lab0.pack()

btnPush = Button(window, width=15, height=2,
                text = "Push",
                foreground="#ff2233",
                font = "Arial 20 bold",
                command=lambda:count(lab0))
btnPush.pack(pady=10)


btnPush2 = Button(window, width=15, height=2,
                text = "reset",
                foreground="#ff2233",
                font = "Arial 20 bold",
                command=lambda:reset(lab0))
btnPush2.pack(pady=20)

window.mainloop()