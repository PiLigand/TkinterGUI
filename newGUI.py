from tkinter import *
import tkinter.messagebox

def doNothing():
	print ("Nothing Done.")

root = Tk()

# ============= Main Menu ==================

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="Edit butts", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# ============= Toolbar ==================

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ============= Status Bar ==================

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W) #west anchor
status.pack(side=BOTTOM, fill=X)

# ============= Message Boxes ==================

tkinter.messagebox.showinfo("Window Title", "My window message")

root.mainloop()
