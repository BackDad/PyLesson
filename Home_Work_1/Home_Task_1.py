import tkinter as TK
import random
from tkinter import ttk
from tkinter import messagebox
import this
#import sys

def random_color():
    return ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
# ---------------------------


clicks = 0
 
def click_button():
    global clicks
    clicks += 1


def c_C_l():
    c_l = random_color()
    lable.configure(bg=c_l)
    lable.configure(text=c_l)
    P_B.step(1)
    click_button()
    print(clicks)
    if(clicks % 5 == 0):
        messagebox.showinfo('предупреждение','палец от кликов не отсох?')
        #quit()



def state_ch():
    if state01.get() == 1:
        c_B['state'] = TK.DISABLED
    else:
        c_B['state'] = TK.NORMAL

# ----------------------------
window = TK.Tk()
title = "change color"
window.title(title)
window.geometry("900x500+670+250")
#bg = TK.PhotoImage(file="bg.jpg")
state01 = TK.IntVar()
state01.set(0)
# lable
lable = TK.Label(window, bg="#333", height=10,
                 width=70, text="какой-нибудь текст")
# ---------Label--------------

lable.grid(row=0, column=0, rowspan=4, columnspan=4, stick="se")
c_B = TK.Button(window, height=1, width=15, bg="#fbf099",
                text="change color", command=c_C_l)
c_B.grid(row=4, column=1, rowspan=4, columnspan=4, stick="nw")
# ---------------------------
Check_Box = TK.Checkbutton(window, text="запрет изминения цвета",
                           variable=state01, onvalue=1, offvalue=0, command=state_ch)
Check_Box.grid(row=4, column=2, rowspan=4, columnspan=4, stick="nw")
# ---------------------------

P_B = ttk.Progressbar(window, mode='determinate', length=200)
P_B.grid(row=5, column=3, rowspan=4, columnspan=4, stick="nw")


window.mainloop()