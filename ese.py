# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:55:24 2018

@author: SaHiL
"""

from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    
    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Insert Status","All Fields are required");
    else:
       con = mysql.connect(host="localhost",user="root",password="",database="stud1")
       cursor = con.cursor();
       cursor.execute("insert into student values('"+id+"','"+name+"','"+phone+"')");
       cursor.execute("commit");
       
       e_id.delete(0,'end')
       e_name.delete(0,'end')
       e_phone.delete(0,'end')
       show()
       MessageBox.showinfo("Insert Status","Done");
       con.close()
       
def delete():
    if(e_id.get()==""):
        MessageBox.showinfo("Delete Function","Id is compolsary for delete")
    else:
        con = mysql.connect(host="localhost",user="root",password="",database="stud1")
        cursor = con.cursor()
        cursor.execute("delete from student where id='"+e_id.get()+"'")
        cursor.execute("commit")
        
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        show()
        MessageBox.showinfo("Deleted","done");
        con.close()
        

def update():
     if(e_id.get()==""):
         MessageBox.showinfo("Update Info","give id")
     else:
         con = mysql.connect(host="localhost",user="root",password="",database="stud1")
         cursor = con.cursor()
         cursor.execute("update student set name='"+e_name.get()+"',phone='"+e_phone.get()+"' where id='"+e_id.get()+"'")
         cursor.execute("commit")
         
         e_id.delete(0,'end')
         e_name.delete(0,'end')
         e_phone.delete(0,'end')
         show()
         MessageBox.showinfo("Update Info","done")
         con.close()
         
def show():
    con = mysql.connect(host="localhost",user="root",password="",database="stud1")
    cursor = con.cursor()
    cursor.execute("select * from student")
    
    rows = cursor.fetchall()
    list.delete(0,list.size())
    
    for row in rows:
        s = row[0]+'        '+row[1]
        list.insert(list.size()+1,s)
        
def get():
    con = mysql.connect(host="localhost",user="root",password="",database="stud1")
    cursor = con.cursor()
    cursor.execute("select *  from student where id='"+e_id.get()+"'")
    
    rows = cursor.fetchall()
    e_name.delete(0,'end')
    e_phone.delete(0,'end')
    
    for row in rows:
        e_name.insert(0,row[1])
        e_phone.insert(0,row[2])
    
root = Tk()
root.geometry("600x300")
root.title("Python CRUD")

id = Label(root,text="Enter ID",font=("bold",10))
id.place(x=20,y=30)

name = Label(root,text="Enter Name",font=("bold",10))
name.place(x=20,y=60)

phone = Label(root,text="Enter Phone",font=("bold",10))
phone.place(x=20,y=90);

e_id = Entry()
e_id.place(x=150,y=30); 

e_name = Entry()
e_name.place(x=150,y=60); 

e_phone = Entry()
e_phone.place(x=150,y=90); 

insert = Button(root,text="Insert",font=("italic",10),bg="white",command=insert)
insert.place(x=20,y=140)

delete = Button(root,text="Delete",font=("italic",10),bg="white",command=delete)
delete.place(x=70,y=140);

update= Button(root,text="Update",font=("italic",10),bg="white",command=update)
update.place(x=130,y=140)

get = Button(root,text="Get",font=("italic",10),bg="white",command=get)
get.place(x=190,y=140)

list = Listbox(root)
list.place(x=290,y=30)
show()

root.mainloop()