'''
from tkinter import *
root = Tk()

root.title('MY BOX GUI')
root.iconbitmap('plane.ico')
root.geometry("500x500")

my_label = Label(root, text = 'konichiwa').pack()
my_label2 = Label(root, text = 'how are u today?').pack()

root.mainloop()
'''
'''
from tkinter import *
root = Tk()

root.title("Co cai con cac")
root.iconbitmap('plane.ico')
root.geometry("500x200")

my_label = Label(root, text = 'toi chinh la')
my_label2 = Label(root, text = 'trung chim to')

my_label.grid(row=0, column=1)
my_label2.grid(row=0, column=2)

root.mainloop()
'''

from tkinter import *
root = Tk()

root.title("Konichiwa minasan")
root.iconbitmap('plane.ico')
root.geometry("500x300")

my_label.grid(row=0, column=1)
my_label2.grid(row=1, column=2)

root.mainloop()

