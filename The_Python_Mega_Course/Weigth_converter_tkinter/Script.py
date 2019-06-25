from tkinter import *

window = Tk()

def clear_all():
    textbox1.delete(1.0, END)
    textbox2.delete(1.0, END)
    textbox3.delete(1.0, END)

def convert_value():
    clear_all()
    
    grams = float(input_value.get()) * 1000
    textbox1.insert(END, grams)
    
    pounds = float(input_value.get()) * 2.2046
    textbox2.insert(END, pounds)
    
    ounces = float(input_value.get()) * 35.274
    textbox3.insert(END, ounces)

label1 = Label(window, text="Enter kilograms")
label1.grid(row=0, column=0)

input_value = StringVar()
inputbox1 = Entry(window, textvariable=input_value)
inputbox1.grid(row=0, column=1)

button1 = Button(window, text="Convert", command=convert_value)
button1.grid(row=0, column=2)

label2 = Label(window, text="Grams")
label2.grid(row=1, column=0)

textbox1 = Text(window, height=1, width=20)
textbox1.grid(row=1, column=1)

label3 = Label(window, text="Pounds")
label3.grid(row=2, column=0)

textbox2 = Text(window, height=1, width=20)
textbox2.grid(row=2, column=1)

label4 = Label(window, text="Ounces")
label4.grid(row=3, column=0)

textbox3 = Text(window, height=1, width=20)
textbox3.grid(row=3, column=1)

window.mainloop()