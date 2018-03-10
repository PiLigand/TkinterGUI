import tkinter

def doNothing():
    print ("Nothing done")

def updateText(TextWidget, TextToBe):
    TextWidget.delete(index1="0.0", index2=tkinter.END)
    TextWidget.insert(tkinter.END, TextToBe)

def textAtoB():
    dmp = textBox2.get(index1="0.0", index2=tkinter.END)
    updateText(TextWidget=textBox1, TextToBe=dmp)


root = tkinter.Tk()

#============== Base Frame ================
baseFrame = tkinter.Frame(root, height=500, width=600)
baseFrame.pack()

#============== TextBoxes =================
textBox1 = tkinter.Text(baseFrame, height=10, width=50)
textBox1.insert(index=tkinter.END ,chars="butts")
updateText(TextWidget=textBox1, TextToBe="Other Message")
textBox1.pack()

textBox2 = tkinter.Text(baseFrame, height=10, width=50)
textBox2.pack()

#============== Buttons ===================
button1 = tkinter.Button(baseFrame, text="Button", command=doNothing)
button1.pack()
button2 = tkinter.Button(baseFrame, text="Text A to B", command=textAtoB)
button2.pack()

root.mainloop()
