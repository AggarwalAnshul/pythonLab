from tkinter import *

root=Tk()
root.geometry("800x800")
b1=Button(root,bg="yellow",padx=10,pady=10,text="b1").place(relx=1,rely=1,x=0,y=0,anchor=SE)
b2=Button(root,bg="green",padx=10,pady=10,text="b2").place(x=0,y=1,anchor=NW)
b1=Button(root,bg="blue",padx=10,pady=10,text="b1").place(relx=1,rely=1,x=-30,y=-30,anchor=SE)
b2=Button(root,bg="pink",padx=10,pady=10,text="b2").place(x=30,y=30,anchor=NW)





root.mainloop
