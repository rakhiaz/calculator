from tkinter import *

class Calculator:

    def __init__(self,master):

        master.title('Calculator')

        self.entry1 = Entry(master)
        self.entry1.grid(row=0)
        
        self.label1 = Label(master,text="+")
        self.label1.grid(row=0,column=1)
        
        self.entry2 = Entry(master)
        self.entry2.grid(row=0,column=2)

        self.btn1 = Button(master, text="=",command=self.tambah)
        self.btn1.grid(row=0,column=3,padx=15)
        
        self.entry3 = Entry(master)
        self.entry3.grid(row=0,column=4)


        self.entry4 = Entry(master)
        self.entry4.grid(row=1)
        
        self.label2 = Label(master,text="-")
        self.label2.grid(row=1,column=1)
        
        self.entry5 = Entry(master)
        self.entry5.grid(row=1,column=2)

        self.btn2 = Button(master, text="=",command=self.kurang)
        self.btn2.grid(row=1,column=3,padx=15)
        
        self.entry6 = Entry(master)
        self.entry6.grid(row=1,column=4)


        self.entry7 = Entry(master)
        self.entry7.grid(row=2)
        
        self.label3 = Label(master,text="/")
        self.label3.grid(row=2,column=1)
        
        self.entry8 = Entry(master)
        self.entry8.grid(row=2,column=2)

        self.btn3 = Button(master, text="=",command=self.bagi)
        self.btn3.grid(row=2,column=3,padx=15)
        
        self.entry9 = Entry(master)
        self.entry9.grid(row=2,column=4)


        self.entry10 = Entry(master)
        self.entry10.grid(row=3)
        
        self.label4 = Label(master,text="x")
        self.label4.grid(row=3,column=1)
        
        self.entry11 = Entry(master)
        self.entry11.grid(row=3,column=2)

        self.btn4 = Button(master, text="=",command=self.kali)
        self.btn4.grid(row=3,column=3,padx=15)
        
        self.entry12 = Entry(master)
        self.entry12.grid(row=3,column=4)


        self.btn_clear = Button(master,text="Clear All",width=20,command=self.clear)
        self.btn_clear.grid(row=4,column=2,pady=10)
        

    def tambah(self):
        x = int(self.entry1.get())
        y = int(self.entry2.get())

        hasil = x + y

        self.entry3.delete(0, END)
        self.entry3.insert(0, hasil)

    def kurang(self):
        x = int(self.entry4.get())
        y = int(self.entry5.get())

        hasil = x - y

        self.entry6.delete(0, END)
        self.entry6.insert(0, hasil)

    def bagi(self):
        x = int(self.entry7.get())
        y = int(self.entry8.get())

        hasil = x / y

        self.entry9.delete(0, END)
        self.entry9.insert(0, hasil)

    def kali(self):
        x = int(self.entry10.get())
        y = int(self.entry11.get())

        hasil = x * y

        self.entry12.delete(0, END)
        self.entry12.insert(0, hasil)

    def clear(self):
        self.entry1.delete(0, END)
        self.entry1.insert(0, "")

        self.entry2.delete(0, END)
        self.entry2.insert(0, "")

        self.entry3.delete(0, END)
        self.entry3.insert(0, "")

        self.entry4.delete(0, END)
        self.entry4.insert(0, "")

        self.entry5.delete(0, END)
        self.entry5.insert(0, "")

        self.entry6.delete(0, END)
        self.entry6.insert(0, "")

        self.entry7.delete(0, END)
        self.entry7.insert(0, "")

        self.entry8.delete(0, END)
        self.entry8.insert(0, "")

        self.entry9.delete(0, END)
        self.entry9.insert(0, "")

        self.entry10.delete(0, END)
        self.entry10.insert(0, "")

        self.entry11.delete(0, END)
        self.entry11.insert(0, "")

        self.entry12.delete(0, END)
        self.entry12.insert(0, "")

        

if __name__ == '__main__':
    root = Tk()
    cal = Calculator(root)
    root.mainloop()
