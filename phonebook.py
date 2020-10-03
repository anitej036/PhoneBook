try:
    from Tkinter import *
except:
    from tkinter import *
import sqlite3
try:
    from tkMessageBox import *
except:
    from tkinter import messagebox

#root0 Window
root0 = Tk()
def destroy(e=1):
    root0.destroy()
root0.title("FRONT PAGE")
root0.geometry('800x300')
root0.configure(bg='orange')
Label(root0,text = 'JAYPEE UNIVERSITY OF ENGINEERING & TECHNOLOGY',font = 'Arial 20 bold',fg = 'DarkOrange4',bg='orange').pack()
Label(root0,text = 'PHONEBOOK PROJECT',font = 'Arial 20 bold underline',fg = 'DarkOrange4',bg='orange').pack()
Label(root0,text = 'DEVELOPED BY',font = 'Arial',fg = 'DarkOrange4',bg='orange').pack()
Label(root0,text = 'ANITEJ SINGH BHADAURIA',font = 'Arial 15 bold',fg = 'DarkOrange4',bg='orange').pack()
Label(root0,text = '181B036',font = 'Arial 15 bold',fg = 'DarkOrange4',bg='orange').pack()

root0.bind('<Motion>',destroy)
root0.mainloop()




#functions
def Save():
    l=[]
    l.append(e1.get())
    l.append(e2.get())
    l.append(e3.get())
    l.append(e4.get())
    l.append(e5.get())
    l.append(e6.get())
    l.append(e7.get())
    l.append(e8.get())
    l.append(e9.get())
    ll=[]
    if v1.get()==1:
        ll.append('Office')
    if v1.get()==2:
        ll.append('Home')
    if v1.get()==3:
        ll.append('Mobile')
    if v2.get()==1:
        ll.append('Office')
    if v2.get()==2:
        ll.append('Personal')    
    ll.append(e10.get())
    ll.append(e11.get())
    cur.execute('insert into phone(first_name,middle_name,last_name,company,address,city,pin,website_URL,birthdate) values(?,?,?,?,?,?,?,?,?)',(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]))
    cur.execute('select max(contact_id) from phone')
    x=cur.fetchall()
    try:
        cur.execute('insert into phone_number(contact_id,contact_type,phone_number) values(?,?,?)',(x[0][0],ll[0],ll[2]))
    except:
        messagebox.showinfo('Error','The Entered Phone Number Is Already Saved...Enter Again ')
        return
    cur.execute('insert into email_id(contact_id,email_type,email_id) values(?,?,?)',(x[0][0],ll[1],ll[3]))
    con.commit()
    
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    messagebox.showinfo('SAVED','Contact Saved Successfully')
    
    
def Search():
    root1 = Tk()
    root1.title("SEARCH")
    root1.geometry('520x700')
    v1 = Entry(root1)
    v1.grid(row=1,column=1)
    def detail(e=1):
        def sho(name):
            root2 =Tk()
            y = ['','','']
            x = name.split()
            for  i in range(len(x)):
                y[i] = x[i]
            cur.execute('select * from phone where first_name = ? or middle_name = ? or last_name = ?',tuple(y))
            xx=cur.fetchall()
            
            cur.execute('select * from phone_number where contact_id = ?',(xx[0][0],))
            
            xxx=cur.fetchall()
            
            cur.execute('select * from email_id where contact_id = ?',(xx[0][0],))
            xxxx=cur.fetchall()
            
            def Delete():
                cur.execute('delete from phone where contact_id=?',(xx[0][0],))
                con.commit()
                cur.execute('delete from phone_number where contact_id=?',(xx[0][0],))
                con.commit()
                cur.execute('delete from email_id where contact_id=?',(xx[0][0],))
                con.commit()
                messagebox.showinfo('Saved','Contact Deleted Successfully')
                root2.destroy()
                return
            def Edit():
                root3 = Tk()
                def editt():
                    data_pb=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),xx[0][0])
                
                    cur.execute('UPDATE phone set first_name=?,middle_name=?,last_name=?,company=?,address=?,city=?,pin=?,website_URL=?,birthdate=? where contact_id=?',data_pb)
                    con.commit()
                    
                    if e11.get()!='':
                        cur.execute('UPDATE phone_number set contact_type=?,phone_number=? where contact_id=?',(e10.get(),e11.get(),xx[0][0]))
                        con.commit()
                
                    if e13.get()!='':
                        cur.execute('UPDATE email_id set email_type=?,email_id=? where contact_id=?',(e12.get(),e13.get(),xx[0][0]))
                        con.commit()
                    messagebox.showinfo('UPDATE','Contact Updated Successfully')
                    root1.destroy()
                    root2.destroy()
                    root3.destroy()
                    
                def closee():
                    jk=messagebox.askokcancel('Alert','Unsaved Changes May Lost')
                    if jk==True:
                        root3.destroy()
                    
                    #GUI for update
                    
                root3.title("EDIT")
                root1.geometry('330x400')
                Label(root3,text = 'EDIT CONTACT',font = 'Arial 20 bold').grid(row=0,column=0,columnspan=2)
                Label(root3,text = 'First Name : ',font = 'Arial 12 bold').grid(row=2,column=0,sticky=E)
                Label(root3,text = 'Middle Name : ',font = 'Arial 12 bold').grid(row=3,column=0,sticky=E)
                Label(root3,text = 'Last Name : ',font = 'Arial 12 bold').grid(row=4,column=0,sticky=E)
                Label(root3,text = 'Company Name : ',font = 'Arial 12 bold').grid(row=5,column=0,sticky=E)
                Label(root3,text = 'Address : ',font = 'Arial 12 bold').grid(row=6,column=0,sticky=E)
                Label(root3,text = 'City : ',font = 'Arial 12 bold').grid(row=7,column=0,sticky=E)
                Label(root3,text = 'Pincode : ',font = 'Arial 12 bold').grid(row=8,column=0,sticky=E)
                Label(root3,text = 'Website URL : ',font = 'Arial 12 bold').grid(row=9,column=0,sticky=E)
                Label(root3,text = 'Date of Birth : ',font = 'Arial 12 bold').grid(row=10,column=0,sticky=E)
                Label(root3,text = 'Phone No type : ',font = 'Arial 12 bold').grid(row=11,column=0,sticky=E)
                Label(root3,text = 'Phone Number : ',font = 'Arial 12 bold').grid(row=12,column=0,sticky=E)
                Label(root3,text = 'Email Type : ',font = 'Arial 12 bold').grid(row=13,column=0,sticky=E)
                Label(root3,text = 'Email Id : ',font = 'Arial 12 bold').grid(row=14,column=0,sticky=E)
                e1 = Entry(root3)
                e1.insert(0, xx[0][1])
                e1.grid(row=2,column=1)
                e2 = Entry(root3)
                e2.insert(0, xx[0][2])
                e2.grid(row=3,column=1)
                e3 = Entry(root3)
                e3.insert(0, xx[0][3])
                e3.grid(row=4,column=1)
                e4 = Entry(root3)
                e4.insert(0, xx[0][4])
                e4.grid(row=5,column=1)
                e5 = Entry(root3)
                e5.insert(0, xx[0][5])
                e5.grid(row=6,column=1)
                e6 = Entry(root3)
                e6.insert(0, xx[0][6])
                e6.grid(row=7,column=1)
                e7 = Entry(root3)
                e7.insert(0, xx[0][7])
                e7.grid(row=8,column=1)
                e8 = Entry(root3)
                e8.insert(0, xx[0][8])
                e8.grid(row=9,column=1)
                e9 = Entry(root3)
                e9.insert(0, xx[0][9])
                e9.grid(row=10,column=1)
                #for number_type
                try:
                    e10=Entry(root3)
                    e10.insert(0,xxx[0][1])
                    e10.grid(row=11,column=1)
                except:
                    e10=Entry(root3)
                    e10.insert(0,'')
                    e10.grid(row=11,column=1)
                #for ph_number
                try:
                    e11=Entry(root3)
                    e11.insert(0,xxx[0][2])
                    e11.grid(row=12,column=1)
                except:
                    e11=Entry(root3)
                    e11.insert(0,'')
                    e11.grid(row=12,column=1)
                #for em_type
                try:
                    e12=Entry(root3)
                    e12.insert(0,xxxx[0][1])
                    e12.grid(row=13,column=1)
                except:
                    e12=Entry(root3)
                    e12.insert(0,'')
                    e12.grid(row=13,column=1)
                #for em
                try:
                    e13=Entry(root3)
                    e13.insert(0,xxxx[0][2])
                    e13.grid(row=14,column=1)
                except:
                    e13=Entry(root3)
                    e13.insert(0,'')
                    e13.grid(row=14,column=1)
                    
                Button(root3,text = 'Save',command=editt,bg = 'Black',fg = 'White',font = '30').grid(row=15,column=0)
                Button(root3,text = 'Exit',command=closee,bg = 'Black',fg = 'White',font = '30').grid(row=15,column=2)
                root3.mainloop()
                
            Label(root2,text="First Name").grid(row=1,column=1)
            
            Label(root2,text=xx[0][1]).grid(row=1,column=2)
            Label(root2,text="Middle Name").grid(row=2,column=1)
            
            Label(root2,text=xx[0][2]).grid(row=2,column=2)
            Label(root2,text="Last Name").grid(row=3,column=1)
            
            Label(root2,text=xx[0][3]).grid(row=3,column=2)
            Label(root2,text="Company Name").grid(row=4,column=1)
            
            Label(root2,text=xx[0][4]).grid(row=4,column=2)
            Label(root2,text="Address").grid(row=5,column=1)
            
            Label(root2,text=xx[0][5]).grid(row=5,column=2)
            Label(root2,text="City").grid(row=6,column=1)
            
            Label(root2,text=xx[0][6]).grid(row=6,column=2)
            Label(root2,text="Pin Code").grid(row=7,column=1)
            
            Label(root2,text=xx[0][7]).grid(row=7,column=2)
            Label(root2,text="Website Url").grid(row=8,column=1)
            
            Label(root2,text=xx[0][8]).grid(row=8,column=2)
            Label(root2,text="Date of Birth").grid(row=9,column=1)
            
            Label(root2,text=xx[0][9]).grid(row=9,column=2)
            Label(root2,text="Phone Number Type").grid(row=10,column=1)
            
            Label(root2,text=xxx[0][1]).grid(row=10,column=2)
            Label(root2,text="Phone Number").grid(row=11,column=1)
            
            Label(root2,text=xxx[0][2]).grid(row=11,column=2)
            Label(root2,text="Email id Type").grid(row=12,column=1)
            
            Label(root2,text=xxxx[0][1]).grid(row=12,column=2)
            Label(root2,text="Email id").grid(row=13,column=1)
            
            Label(root2,text=xxxx[0][2]).grid(row=13,column=2)
            Button(root2,text="Delete",command=Delete).grid(row=14,column=1)
            Button(root2,text="Edit",command=Edit).grid(row=14,column=2)
            
            root2.mainloop()
        data=(e1.get(e1.curselection()))
        sho(data)
        
        
    def search1(e=1):
        e1.delete(0,END)
        a=str(v1.get())
        cur.execute('select first_name,middle_name,Last_name from phone where first_name like "%'+str(a)+'%" or middle_name like "%'+str(a)+'%" or last_name like "%'+str(a)+'%"')
        data=(cur.fetchall())
        for i in range(len(data)):
            x = data[i][0]+' '+data[i][1]+' '+data[i][2]
            e1.insert(i+1,x)
        root1.bind('<Button-1>',detail)    
    
    #label for search page
    Label(root1,text = 'SEARCH CONTACT',font = 'Arial 20 bold',fg = 'Black',bg = 'sky blue').grid(row=0,column=1)
    Label(root1,text = 'Name or Number',).grid(row=1,column=0)
    
    e1=Listbox(root1,height=40,width=40,font='Arial 18',fg='Blue',bg='light yellow')
    cur.execute('select count(*) from phone')
    n = cur.fetchall()[0][0]
    cur.execute('select first_name,middle_name,last_name from phone order by first_name')
    data = cur.fetchall()
    
    e1.grid(row=2,column=0,columnspan=3)
    root1.bind("<KeyPress>",search1)
    root1.mainloop()
def Close():
    x=messagebox.askokcancel('Alert','OK TO EXIT')
    if x==True:
        root.destroy()
def u():
    #showinfo('X','Not Allowed')
    e10=Entry(root)
    e10.grid(row=11,column=3)
    

root=Tk()
imgg=PhotoImage(file='animated-telephone-image-0023.gif')
Label(root,image=imgg).grid(row=0,column=1)
Label(root,text="First Name").grid(row=1,column=1)
e1=Entry(root)
e1.grid(row=1,column=2)
Label(root,text="Middle Name").grid(row=2,column=1)
e2=Entry(root)
e2.grid(row=2,column=2)
Label(root,text="Last Name").grid(row=3,column=1)
e3=Entry(root)
e3.grid(row=3,column=2)
Label(root,text="Company Name").grid(row=4,column=1)
e4=Entry(root)
e4.grid(row=4,column=2)
Label(root,text="Address").grid(row=5,column=1)
e5=Entry(root)
e5.grid(row=5,column=2)
Label(root,text="City").grid(row=6,column=1)
e6=Entry(root)
e6.grid(row=6,column=2)
Label(root,text="Pin Code").grid(row=7,column=1)
e7=Entry(root)
e7.grid(row=7,column=2)
Label(root,text="Website Url").grid(row=8,column=1)
e8=Entry(root)
e8.grid(row=8,column=2)
Label(root,text="Date of Birth").grid(row=9,column=1)
e9=Entry(root)
e9.grid(row=9,column=2)
Label(root,text="Select Phone Type",font = 'Arial 16 ',fg='BLUE').grid(row=10,column=0)
v1=IntVar()
Radiobutton(root,text="Office",variable=v1,value=1).grid(row=10,column=1)
Radiobutton(root,text="Home",variable=v1,value=2).grid(row=10,column=2)
Radiobutton(root,text="Mobile",variable=v1,value=3).grid(row=10,column=3)
Button(root,text="+",command=u).grid(row=10,column=4)
Label(root,text="Phone number").grid(row=11,column=1)
e10=Entry(root)
e10.grid(row=11,column=2)
Label(root,text="Select Email Type",font = 'Arial 16 ',fg='BLUE').grid(row=12,column=0)
v2=IntVar()
Radiobutton(root,text="Office",variable=v2,value=1).grid(row=12,column=1)
Radiobutton(root,text="Personal",variable=v2,value=2).grid(row=12,column=2)
Label(root,text="Email Id").grid(row=13,column=1)
e11=Entry(root)
e11.grid(row=13,column=2)
Button(root,text="Save",command=Save).grid(row=14,column=1)
Button(root,text="Search",command=Search).grid(row=14,column=2)
Button(root,text="Close",command=Close).grid(row=14,column=3)
#Button(root,text="Edit",command=edit).grid(row=14,column=3)






con=sqlite3.Connection('Phonebook_database')
cur=con.cursor()
cur.execute('create table if not exists phone(contact_id integer primary key autoincrement,first_name varchar(25),last_name varchar(25),middle_name varchar(25),company varchar(25),address varchar(50),city varchar(20),pin number(7),website_URL varchar(50),birthdate varchar(30))')
cur.execute('create table if not exists phone_number(contact_id integer,contact_type varchar(15),phone_number number(15) primary key,constraint fk foreign key(contact_id) references phone(contact_id))')
cur.execute('create table if not exists email_id(contact_id integer,email_type varchar(15),email_id varchar(25) primary key,constraint fk_1 foreign key(contact_id) references phone(contact_id))')


root.mainloop()
