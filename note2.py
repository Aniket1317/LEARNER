from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class note:
    current_file='no_file'
    def open(self):
        open_file=filedialog.askopenfile(initialdir='/',title='Select a file to open',filetypes=(('text files','*.txt'),('all files','*.*')))
        if(open_file != None):
            self.textpad.delete(1.0,END) 
            for line in open_file:
                self.textpad.insert(END, line)
        self.current_file = open_file.name
        open_file.close()
                
    def save_as(self):
        file=filedialog.asksaveasfile(mode= 'w', defaultextension='.txt')
        if(file != None):
            return
        text_save=self.textpad.get(1.0,END)
        self.current_file= file.name
        file.write(text_save)
        file.close()
        
    def save(self):
        if (self.current_file == 'no_file'):
            self.save_as()
        else:
            file= open(self.current_file, 'w+')
            file.write(self.textpad.get(1.0, END))
            file.close()
            
    def new(self):
        self.textpad.delete(1.0,END)
        self.current_file='no_file'
        
    def exit(self):
        if messagebox.askyesno('Do you want to exit.....','Really!!!...Dont do it'):
            self.master.destroy()
            
    def copy(self):
        self.textpad.clipboard_clear()
        self.textpad.clipboard_append(self.textpad.selection_get())
    
    def cut(self):
        self.copy()
        self.textpad.delete('sel.first','sel.last')
    
    def paste(self):
        self.textpad.insert(INSERT,self.textpad.clipboard_get())
        
        
    def __init__(self,master):
        self.master=master
        master.title('My Diary')
        self.textpad=Text(self.master, undo=True)
        self.textpad.pack(fill=BOTH,expand=1)
        
        self.menu=Menu()
        self.master.configure(menu=self.menu)
        
        self.filemenu=Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='New',command= self.new)
        self.filemenu.add_command(label='open',command= self.open)
        self.filemenu.add_command(label='Save as..',command= self.save_as)
        self.filemenu.add_command(label='Save',command= self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit',command= self.exit)
        self.filemenu.add_separator()
        
        self.editmenu=Menu(self.menu)
        self.menu.add_cascade(label='Edit',menu=self.editmenu)
        self.editmenu.add_command(label='Cut',command=self.cut)
        self.editmenu.add_command(label='Copy',command=self.copy)
        self.editmenu.add_command(label='Paste',command=self.paste)
        self.editmenu.add_separator()
        self.editmenu.add_command(label='Undo',command=self.textpad.edit_undo)
        self.editmenu.add_command(label='Redo',command=self.textpad.edit_redo)
        self.editmenu.add_separator()
        
        
        
root = Tk()
obj= note(root)
root.mainloop()
