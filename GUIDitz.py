from Tkinter import *


class TomsButtons:
	def __init__(self, master):
		self.frame = Frame(master)
		self.frame.pack()

		self.printButton = Button(self.frame, text="Print Message", command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(self.frame, text="Quit", command=self.frame.quit)
		self.quitButton.pack(side=LEFT)
	
	def printMessage(self):
		print "wow, this worked!"


root = Tk()

b = TomsButtons(root)

root.mainloop()
