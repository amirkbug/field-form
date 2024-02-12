from tkinter import *
from tkinter import messagebox
from infooo import *
# main tk 
main = Tk()

# functions
def exit_func():
    main.destroy()

def insert_func():
    global x1
    s1 = info(lbl_firstname_entry.get(),lbl_lastname_entry.get(),int(lbl_score_entry.get()))
    x1 = s1.state(int(lbl_score_entry.get()))
    lstbx.insert(END,f"{s1.fname} {s1.lname} {s1.score} {x1}",)

def status():
    s2 = info(lbl_firstname_entry.get(),lbl_lastname_entry.get(),int(lbl_score_entry.get()))
    x2 = s2.state(int(lbl_score_entry.get()))
    messagebox.showinfo('your score !!!!' , x2)


# geometry
screen_width = main.winfo_screenwidth() 
screen_height = main.winfo_screenheight() 
window_width = 400
window_height = 400
x = (screen_width - window_width) / 2
y = (screen_height - window_height) / 2
main.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
# title and icon
main.title('form')

# labels 
lbl_firstname = Label(main,text='firstname :')
lbl_firstname.place(x=50,y=20)

lbl_lastname = Label(main,text='lastname :')
lbl_lastname.place(x=50,y=50)

lbl_score = Label(main,text='score :')
lbl_score.place(x=70,y=80)

# entris 
lbl_firstname_entry = Entry(main)
lbl_firstname_entry.place(x=130,y=20)

lbl_lastname_entry = Entry(main)
lbl_lastname_entry.place(x=130,y=50)

lbl_score_entry = Entry(main)
lbl_score_entry.place(x=130,y=80)

# button
exit_bu = Button(main,text='exit',width=7,height=1,command=exit_func)
exit_bu.place(x=80,y=300)

status_bu = Button(main,text='status',width=7,height=1,command=status)
status_bu.place(x=160,y=300)

insert_bu = Button(main,text='insert',width=7,height=1,command=insert_func)
insert_bu.place(x=240,y=300)


# listbox
lstbx = Listbox(main,width=50,height=9)
lstbx.place(x=0,y=100)




# main loop
main.mainloop()