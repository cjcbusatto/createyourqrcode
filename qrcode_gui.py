#!/usr/bin/python
from Tkinter import *
from tkFileDialog import askopenfilename
import qrgenerator
def openfile():
 	filename = askopenfilename(parent=root)
 	text = entry.get()
 	readabilityPriority = checkButtonValue.get()
	qrgenerator.create_qrcode(text, filename, readabilityPriority).show()

root = Tk()
root.wm_title("Create Your Own QRCode!")
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(300, 80))

entry = Entry(root, width=50)
entry.insert(0,"Insert the URL that you want to encode here!")
entry.pack()

checkButtonValue = IntVar()
c = Checkbutton(root, text="Readability Priority", variable=checkButtonValue)
c.pack()

b = Button(root, text="Create QRCode!", width=12, command=openfile)
b.pack()


root.mainloop()