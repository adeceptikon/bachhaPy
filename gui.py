
#Tkinter use karke 
#basic GUI ke liye 
import tkinter as tk
from tkinter.constants import *

def shout():
    

if __name__ == "__main__":
    t = tk.Tk()
    #frame banao
    frame = tk.Frame(t , relief=RIDGE , borderwidth=2 )
    frame.pack(fill=BOTH , expand=1)

    #label banao , sab frame me pack hoga
    label = tk.Label(frame , text="pehla gui program")
    label.pack(fill=BOTH , expand=1)
    #entry
    #text
    #checkbox
    #message
    #oprions menu
    #scroll bar
    #canvas
    #listbox
    #radio button
    #paned window

    #botton  , ye bhi frame me  pack hoga
    button = tk.Button(frame , text="exit" , command=t.destroy)
    button.pack(side=BOTTOM)
    t.mainloop()

