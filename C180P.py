from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Translator")
root.geometry("800x800")
root.configure(bg= "#F2CCC3")

l1 = Label(root, text = "LANGUAGE TRANSLATOR")
l1.place(relx= 0.5, rely= 0.1, anchor = CENTER)

l2 = Label(root, text = "Enter Text")
l2.place(relx= 0.2, rely= 0.3, anchor = CENTER)

ta = Text(root,height= 400, wrap= WORD, width=500, padx = 5, pady= 5, bd = 0)
ta.place(relx = 0.2, rely= 0.4, anchor = CENTER)

root.mainloop()