from tkinter import *
from tkinter import ttk    #เป็นหน้าตา
from tkinter import messagebox

GUI = Tk()#คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')#นี่คือชื่อโปรแกรม
GUI.geometry('500x400')#กำหนดหน้าจอ

def fullname():
    text = 'เตชิต  ภัทรศรีวงศ์'
    messagebox.showinfo('ชื่อ-สกุล',text)

fb1 = Frame(GUI)
fb1.place(x=200,y=100)
B1 = ttk.Button(fb1,text='ชื่อ-สกุล',command=fullname)#สร้างปุ่ม ใส่ข้อความบนปุ่ม
B1.pack(ipadx=20,ipady=20)


def money():
    text = '20,000'
    messagebox.showinfo('เงินเดือน',text)
    
fb2 = Frame(GUI)
fb2.place(x=200,y=200)
B2 = ttk.Button(fb2,text='เงินเดือน',command=money)#สร้างปุ่ม ใส่ข้อความบนปุ่ม
B2.pack(ipadx=20,ipady=20)


def education():
    text = 'ครู'
    messagebox.showinfo('อาชีพ',text)
    
fb3 = Frame(GUI)
fb3.place(x=200,y=300)
B3 = ttk.Button(fb3,text='อาชีพ',command=education)#สร้างปุ่ม ใส่ข้อความบนปุ่ม
B3.pack(ipadx=20,ipady=20)


GUI.mainloop()
