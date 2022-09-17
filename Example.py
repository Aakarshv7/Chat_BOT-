from tkinter import *

from pip import main


main =Tk()

def ex():
    print("a")

def bf():
    print("b")

a=IntVar()

r1=Radiobutton(main,text="Option1", variable=a,value=1, command= ex).pack()
r2=Radiobutton(main,text="Option2", variable=a,value=2, command= bf).pack()

main.mainloop()
