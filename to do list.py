from tkinter import *

window = Tk()
window.title("TO DO LIST APP")

toDo = ["savings","help people", "Study flutter", "learn trading", "buy food", "laundry", "Goal 1", "Goal 2", "Goal 3"]

myLabel = Label(window, 
    text = "My To Do List",
    font=("Bahnschrift", 25),
    bg = "#FFFFE0"
    )

myLabel.pack()

my_frame = Frame(window)
my_frame.pack(pady=20)

#design for list components
my_list = Listbox(my_frame,
    font = "Bahnschrift, 15",
    width = 25,
    height = 5,
    bg = "#D3D3D3",
    bd = 0,
    fg = "#464646",
    selectbackground="#73C2FB",
    activestyle="none" 
    )

#relist in my_list in reverse order
for item in toDo:
        my_list.insert(-1,item)

my_list.pack(side = LEFT, fill = BOTH)

#scrollbar function
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side = RIGHT, fill = BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)

my_entry = Entry(window, font=("Helvetica, 13"), width = 33, fg = "#1a1a1a")
#placeholder
# call function when we click on entry box
def inside_entry(*args):
    my_entry.delete(0, 'end')

  
  
# Add Placeholder
my_entry.insert(0, 'Add To Do Here: ')
my_entry.config(fg = "#C0C0C0")
  

my_entry.bind("<Button-1>", inside_entry)
my_entry.config(fg = "#1a1a1a")
my_entry.pack(pady=15)



button_frame = Frame(window, bg="#FFFFE0")
button_frame.pack(pady = 20)

#four functions: add item, delete item, prioritize item and mark item as done
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.config(text ="")
    inside_entry(my_entry)

def delete_item():
    my_list.delete(ANCHOR)

#priority item -> font is violet, make it first in list
def highlight_item():
    my_list.insert(0, my_list.get(ANCHOR))
    my_list.itemconfig(0, fg="#8A2BE2")
    my_list.delete(ANCHOR)
    
    
#set item can be marked as done or undone 
def done_item():
    if my_list.get(ANCHOR)[-1] == "*":
        my_list.insert(END, my_list.get(ANCHOR)[:-1])
        my_list.itemconfig(ANCHOR, fg="#464646")
        my_list.delete(ANCHOR)

    else:
        my_list.insert(END, my_list.get(ANCHOR)+"*")
        my_list.itemconfig(END, fg="#dbdbdb")
        my_list.delete(ANCHOR)

add_button = Button(button_frame, text="Add New Item", command= add_item)
delete_button = Button(button_frame, text="Delete Item", command= delete_item)
highlight_button = Button(button_frame, text="Priority Item", command= highlight_item)
mark_button = Button(button_frame, text="Mark Item", command= done_item)

#design for buttons
add_button.grid(row = 0, column = 0, padx = 10)
add_button.config(font = "Helvetica, 12", bg = "#75E6DA", activeforeground="#189AB4", relief = "groove")
delete_button.grid(row = 0, column = 1, padx = 10)
delete_button.config(font = "Helvetica, 12", bg = "#DC143C", activeforeground="#FF0000", relief = "groove")
highlight_button.grid(row = 0, column = 2, padx = 10)
highlight_button.config(font = "Helvetica, 12", bg = "#9370DB", activeforeground="#DDA0DD", relief = "groove")
mark_button.grid( row = 0, column = 3, padx = 10)
mark_button.config(font = "Helvetica, 12", bg = "#696969", activeforeground="#C0C0C0", relief = "groove")

window.configure(bg="#FFFFE0")
window.geometry("480x375")
window.mainloop()
