import menu
K=[True]*10
N=3
menu._Menu(K,N)

#level
from tkinter import *
from tkinter import ttk
from random import randint
import tkinter.font as tkFont
n=3

Bt=[0]*n
Btn=[0]*n
x0=50
y0=50
w=500
h=500
for i in range(n):
  Btn[i]=[0]*n
  Bt[i]=[0]*n
root = Tk()
root.title("METANIT.COM")
root.geometry("600x600")
canvas = Canvas(bg="white", width=600, height=600)
canvas.focus_set()
#canvas.pack()

pixelVirtual = PhotoImage(width=1, height=1)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)

labelExample = Label(root, text="20", font=fontStyle)
pixelVirtual = PhotoImage(width=1, height=1)
def clicked(i,j):
    print("Clic",i,j)

index=1
for i in range(n):    
    for j in range(n):
        Bt[i][j] = index
        Btn[i][j]=Button(root, text = str(index),
                         image=pixelVirtual, width = w//3.5, height = h//3.5,
                         command=lambda k=i,m=j:clicked(k,m),compound="c")
        Btn[i][j].place(y=x0+w//n*i,x=y0+h//n*j,)
        index+=1
Btn[n-1][n-1]["text"] =""      
root.mainloop()