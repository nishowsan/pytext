#start of python text editor
'''
            welcome to my very own and first python text editor
          at december i am releasing v2.0 (advanced and better)
'''
# starting coding
# importing packages
import sys
import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
root = Tk() # the main window
text = Text(root)# the main text box for tkinter
# packing variables
text.pack(fill=X)
filename = NONE
# new file
def new(): # the function to save the file
    global filename
    filename = "Untitled"
    text.delete(0.0 ,END)
# save file
def save(): # the function to save the file
    global filename
    t = text.get(0.0 ,END)
    f = open(filename ,'w')
    f.write(t)
    f.close()
# save as file
def saveas(): # the function to save the file
    f = tkinter.filedialog.asksaveasfile(mode='w' ,defaultextension='.txt')
    t =text.get(0.0 ,END)
    try:
        f.write(t.rstrip())
    except:
        print("something went wrong .")
# open file
def open_file(): # the function to save the file
    f =tkinter.filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0 ,END)
    text.insert(0.0 ,t)
# to exit
def exit_sys(): # the function to save the file
    sys.exit(0)

# going graphical
label = Label(root ,text="welcome to python text editor" ,bg='green' ,fg='black' ,bd=1)
label.pack(fill=X ,side=TOP)

# message to the users
def about():
    tkinter.messagebox.showinfo('the pytext editor', "thanks for using the python text editor beta by nishow")

def help():
    tkinter.messagebox.showinfo('the pytext editor' , "you fool , can't even use a text editor , just type on it")

# main functions of menu
menu = Menu(root) # making the menu
root.config(menu=menu) # configuring the menu for the main windows
submenu1 = Menu(menu) # sub menu
submenu2 = Menu(menu) # sub  menu
# adding the sub menu
menu.add_cascade(label='file' ,menu=submenu1)
menu.add_cascade(label='about' ,menu=submenu2)
# adding the sub menu commands
# sub menu 1
submenu1.add_command(label='new file' ,command=new)
submenu1.add_command(label='save' ,command=save)
submenu1.add_command(label='save as' ,command=saveas)
submenu1.add_command(label='open' ,command=open_file)
submenu1.add_separator()
submenu1.add_command(label='exit' ,command=exit_sys)
# sub menu 2
submenu2.add_command(label='about' ,command=about)
submenu2.add_command(label='help' ,command=help)
#final comment
'''
     the code is complete , please do not change the coder name ,
        that will not make you the coder of this program
'''
# executing the final program before launching
root.mainloop()

