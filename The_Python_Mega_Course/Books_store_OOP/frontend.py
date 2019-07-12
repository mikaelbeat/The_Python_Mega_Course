from tkinter import *

from backend import Database


database = Database("books.db")


def get_selected_row(event):
    try:
        global selection
        index = listbox.curselection()[0]
        selection = listbox.get(index)
        inputbox1.delete(0, END)
        inputbox1.insert(END, selection[1])
        inputbox2.delete(0, END)
        inputbox2.insert(END, selection[2])
        inputbox3.delete(0, END)
        inputbox3.insert(END, selection[3])
        inputbox4.delete(0, END)
        inputbox4.insert(END, selection[4])
    except IndexError:
        pass

def view_command():
    listbox.delete(0, END)
    for row in database.view():
        listbox.insert(END, row)
        
def search_command():
    listbox.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(),ISBN_text.get()):
        listbox.insert(END, row)
        
def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    listbox.delete(0, END)
    listbox.insert(END,(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()))

def delete_command():
    database.delete(selection[0])
    
def update_command():
    database.update(selection[0], selection[1], selection[2], selection[3], selection[4])


window = Tk()
window.wm_title("BookStore")


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

listbox.bind('<<ListboxSelect>>', get_selected_row)

button1 = Button(window, text="View all", width=12, command=view_command)
button1.grid(row=2, column=3)

button2 = Button(window, text="Search entry", width=12, command=search_command)
button2.grid(row=3, column=3)

button3 = Button(window, text="Add entry", width=12, command=add_command)
button3.grid(row=4, column=3)

button4 = Button(window, text="Update", width=12, command=update_command)
button4.grid(row=5, column=3)

button5 = Button(window, text="Delete", width=12, command=delete_command)
button5.grid(row=6, column=3)

button6 = Button(window, text="Close", width=12, command=window.destroy)
button6.grid(row=7, column=3)



window.mainloop()