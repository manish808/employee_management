from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox 

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')

        # Varaibles
        self.var_name=StringVar()
        self.var_number=StringVar()
        self.var_dept=StringVar()
        self.var_address=StringVar()
        self.var_salary=StringVar()
        self.var_email=StringVar()
        self.var_id=StringVar()

        lbl_title=Label(self.root,text='Employee Management System',font=('times new roman',37,BOLD),fg='black',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        img_logo=Image.open('images\logo.jpg')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        img_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        #1st
        img1=Image.open('images\logo.jpg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.logo=Label(img_frame,image=self.photo1)
        self.logo.place(x=0,y=0,width=540,height=160)

        #Main Frame 
        Main_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=800)


        #upper Frame
        upper_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE , text='Employee Management',font=('times new roman',10,BOLD),fg='red',bg='white')
        upper_frame.place(x=5,y=0,width=1500,height=350)


        #Entry Fields

        #-- Select Department
        lbl_dept=Label(upper_frame,text='Department',font=('arial',11,BOLD),bg='white')
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)

        combo_dept=ttk.Combobox(upper_frame,textvariable=self.var_dept,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dept['value']=('Select Your Department','HR','Software Engineer','Manager')
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #-- Enter Phone Number
        lbl_num=Label(upper_frame,text='Phone Number:',font=('arial',12,'bold'),bg='white')
        lbl_num.grid(row=1,column=0,padx=2,pady=10)

        txt_num=ttk.Entry(upper_frame,textvariable=self.var_number,width=22,font=('arial',11,'bold'))
        txt_num.grid(row=1,column=1,padx=2,pady=7)
        
         #-- Enter Email
        lbl_email=Label(upper_frame,text='Email:',font=('arial',12,'bold'),bg='white')
        lbl_email.grid(row=2,column=0,padx=2,pady=10)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',11,'bold'))
        txt_email.grid(row=2,column=1,padx=2,pady=7)

         #-- Enter id
        lbl_id=Label(upper_frame,text='Employee Id:',font=('arial',12,'bold'),bg='white')
        lbl_id.grid(row=2,column=2,padx=2,pady=10)

        txt_id=ttk.Entry(upper_frame,textvariable=self.var_id,width=22,font=('arial',11,'bold'))
        txt_id.grid(row=2,column=3,padx=2,pady=7)

         #-- Enter Address
        lbl_add=Label(upper_frame,text='Address:',font=('arial',12,'bold'),bg='white')
        lbl_add.grid(row=3,column=0,padx=2,pady=10)

        txt_add=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_add.grid(row=3,column=1,padx=2,pady=7)

         #-- Enter Salary
        lbl_sal=Label(upper_frame,text='Salary:',font=('arial',12,'bold'),bg='white')
        lbl_sal.grid(row=1,column=2,padx=2,pady=10)

        txt_sal=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
        txt_sal.grid(row=1,column=3,padx=2,pady=7)


        #-- Enter Name
        lbl_name=Label(upper_frame,text='Name:',font=('arial',12,'bold'),bg='white')
        lbl_name.grid(row=0,column=2,padx=2,pady=10)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #Button Frame
        button_frame = Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1290,y=10,width=170,height=250)

        btn_add=Button(button_frame,text='Save',command=self.add_data,font=('aerial',10,'bold'),width=18,height=2,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text='Update',command=self.update_data,font=('aerial',10,'bold'),width=18,height=2,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text='Delete',command=self.delete_data,font=('aerial',10,'bold'),width=18,height=2,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_refresh=Button(button_frame,text='Refresh',command=self.refresh_data,font=('aerial',10,'bold'),width=18,height=2,bg='blue',fg='white')
        btn_refresh.grid(row=3,column=0,padx=1,pady=5)


        #lower Frame
        lower_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE , text='Employee Management Table',font=('times new roman',10,BOLD),fg='red',bg='white')
        lower_frame.place(x=5,y=360,width=1500,height=200)

        #Search Frame 

        self.var_search_combo=StringVar()
        self.var_search_result=StringVar()
        search_frame = LabelFrame(lower_frame,bd=2,relief=RIDGE, bg='white')
        search_frame.place(x=0,y=2,width=1500,height=50)

        btn_search=Button(search_frame,text='Search By:',font=('aerial',8,'bold'),width=8,height=2,bg='red',fg='black')
        btn_search.grid(row=0,column=0,padx=1,pady=5)

        combo_search=ttk.Combobox(search_frame,textvariable=self.var_search_combo,font=('arial',7,'bold'),width=17,state='readonly')
        combo_search['value']=('idEmployee','Phone_number','Name','Email')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2,pady=10)

        txt_search=ttk.Entry(search_frame,textvariable=self.var_search_result,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=3,padx=2,pady=7)

        btn_search=Button(search_frame,command=self.Search,text='Search',font=('aerial',8,'bold'),width=8,height=2,bg='blue',fg='white')
        btn_search.grid(row=0,column=4,padx=1,pady=5)

        btn_showall=Button(search_frame,command=self.fetch_data,text='Show All',font=('aerial',8,'bold'),width=8,height=2,bg='blue',fg='white')
        btn_showall.grid(row=0,column=5,padx=1,pady=5)

        # Table Frame
        table_frame=Frame(lower_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=100)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee=ttk.Treeview(table_frame,column=('id','name','dep','num','email','add','sal'))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee.xview)
        scroll_y.config(command=self.employee.yview)

        self.employee.heading('id',text='Employee Id')
        self.employee.heading('name',text='Name')
        self.employee.heading('dep',text='Department')
        self.employee.heading('num',text='Number')
        self.employee.heading('sal',text='Salary ') 
        self.employee.heading('add',text='Address ')
        self.employee.heading('email',text='Email')

        self.employee['show']='headings'

        self.employee.column("id",width=50)
        self.employee.column("name",width=50)
        self.employee.column("dep",width=50)
        self.employee.column("num",width=50)
        self.employee.column("sal",width=50)
        self.employee.column("add",width=50)
        self.employee.column("email",width=50)
 
        self.employee.pack(fill=BOTH,expand=1)

        self.employee.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
    

    # *************Function Declarations********
    def add_data(self):
        if self.var_dept.get()=="" or self.var_address=="" or self.var_email=="" or self.var_id=="" or self.var_name=="" or self.var_number=="" or self.var_salary=="":
            messagebox.showerror('Error','All Details must be filled')
        else:
            try:
                conn= mysql.connector.connect(host='localhost',username='root',password='hello123',database='employee_management_system')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                self.var_id.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_dept.get(),
                                                                                                self.var_number.get(),
                                                                                                self.var_salary.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_email.get(),
                                                                                               
                                                                                               
                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been added successfully',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # fetch data
    def fetch_data(self):
        conn= mysql.connector.connect(host='localhost',username='root',password='hello123',database='employee_management_system')
        my_cursor=conn.cursor()   
        my_cursor.execute('select * from employee')
        data = my_cursor.fetchall()
        if (len(data))!= 0:
            self.employee.delete(*self.employee.get_children())
            for i in data:
                self.employee.insert("",END,values=i)
            conn.commit()
        conn.close()

    # Get Cursor

    def get_cursor(self,event=""):
        cursor_row=self.employee.focus()
        content=self.employee.item(cursor_row)
        data=content['values']

        self.var_id.set(data[0])
        self.var_name.set(data[1])
        self.var_dept.set(data[2])
        self.var_email.set(data[6])
        self.var_salary.set(data[4])
        self.var_number.set(data[3])
        self.var_address.set(data[5])


    # Update Data

    def update_data(self):
        if self.var_dept.get()=="" or self.var_address=="" or self.var_email=="" or self.var_id=="" or self.var_name=="" or self.var_number=="" or self.var_salary=="":
            messagebox.showerror('Error','All Details must be filled')
        else:
            try:
                update= messagebox.askyesno('Update','Are you sure you want to update data')
                if update> 0:
                    conn= mysql.connector.connect(host='localhost',username='root',password='hello123',database='employee_management_system')
                    my_cursor=conn.cursor()
                    my_cursor.execute('Update employee set Name=%s, Department=%s, Phone_number=%s,Salary= %s, Address=%s, Email=%s where idEmployee=%s',(     
                                                                                                                                                            self.var_name.get(),
                                                                                                                                                            self.var_dept.get(),
                                                                                                                                                            self.var_number.get(),
                                                                                                                                                            self.var_salary.get(),
                                                                                                                                                            self.var_address.get(),
                                                                                                                                                            self.var_email.get(),
                                                                                                                                                            self.var_id.get()    
                                                                                                                                                            ))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee Updated Successfully',parent =self.root)
            except Exception as es:
                 messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)


    # Delete

    def delete_data(self):
        if self.var_id=="":
            messagebox.showinfo('Error', 'All fields must not be empty')
        else:
            try:
                delete = messagebox.askyesno('Delete','Are you sure you want to delete',parent = self.root)
                if delete > 0:
                    conn= mysql.connector.connect(host='localhost',username='root',password='hello123',database='employee_management_system')
                    my_cursor=conn.cursor()
                    my_cursor.execute('delete from employee where idEmployee=%s ',(self.var_id.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.refresh_data()
                conn.close()
                messagebox.showinfo('Deleted','Employee Deleted Successfully',parent =self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)


    # Reset Data

    def refresh_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_dept.set("Select Department")
        self.var_email.set("")
        self.var_salary.set("")
        self.var_number.set("")
        self.var_address.set("")


    # Search Data

    def Search(self):
        if self.var_search_result=="" or self.var_search_combo=="":
            messagebox.showinfo('Error', 'All fields must not be empty')
        else:
            try:
                conn= mysql.connector.connect(host='localhost',username='root',password='hello123',database='employee_management_system')
                my_cursor=conn.cursor()
                my_cursor.execute('Select * from employee where ' + str(self.var_search_combo.get())+" LIKE '%" + str(self.var_search_result.get() + "%'"))
                rows= my_cursor.fetchall()
                if (len(rows))!= 0:
                    self.employee.delete(*self.employee.get_children())
                    for i in rows:
                     self.employee.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



if __name__=="__main__": 
    root=Tk()
    obj=Employee(root)
    root.mainloop() 