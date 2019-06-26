from tkinter import *


window = Tk()

label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

title_text = StringVar()
inputbox1 = Entry(window, textvariable=title_text)
inputbox1.grid(row=0, column=1)

label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

author_text = StringVar()
inputbox2 = Entry(window, textvariable=author_text)
inputbox2.grid(row=0, column=3)

label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

year_text = StringVar()
inputbox3 = Entry(window, textvariable=year_text)
inputbox3.grid(row=1, column=1)

label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

ISBN_text = StringVar()
inputbox4 = Entry(window, textvariable=ISBN_text)
inputbox4.grid(row=1, column=3)

listbox = Listbox(window, height=6, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview())

button1 = Button(window, text="View all", width=12)
button1.grid(row=2, column=3)

button2 = Button(window, text="Search entry", width=12)
button2.grid(row=3, column=3)

button3 = Button(window, text="Add entry", width=12)
button3.grid(row=4, column=3)

button4 = Button(window, text="Update", width=12)
button4.grid(row=5, column=3)

button5 = Button(window, text="Delete", width=12)
button5.grid(row=6, column=3)

button6 = Button(window, text="Close", width=12)
button6.grid(row=7, column=3)



window.mainloop()