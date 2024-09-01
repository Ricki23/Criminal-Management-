from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


def main():
    win = Tk()
    app = Login(win)
    win.mainloop()


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")

        self.username = StringVar()
        self.password = StringVar()

        lbl_title = Label(self.root, text="Login", font=("times new roman", 20, "bold")).pack()

        lbl_username = Label(self.root, text="Username", font=("times new roman", 15)).place(x=50, y=100)
        self.txt_username = Entry(self.root, textvariable=self.username, font=("times new roman", 15))
        self.txt_username.place(x=150, y=100)

        lbl_password = Label(self.root, text="Password", font=("times new roman", 15)).place(x=50, y=150)
        self.txt_password = Entry(self.root, textvariable=self.password, show="*", font=("times new roman", 15))
        self.txt_password.place(x=150, y=150)

        btn_login = Button(self.root, text="Login", command=self.login, font=("times new roman", 15)).place(x=150, y=200)





    def login(self):
        if self.username.get() == "admin" and self.password.get() == "admin":
            self.new_window = Toplevel(self.root)
            self.app = Crime(self.new_window)
        elif self.username.get() == "Police" and self.password.get() == "Orrisa":
            self.new_window = Toplevel(self.root)
            self.app = Crime(self.new_window)
        else:
            messagebox.showerror("Error", "Invalid username or password")




class Crime:
    def __init__(abc, root):
        abc.root = root
        abc.root.geometry("1300x790+0+0")
        abc.root.title('CRIMINAL MANAGEMENT SYSTEM SOFTWARE')

        # Variables
        abc.var_date_of_crime = StringVar()
        abc.var_criminal_no = StringVar()
        abc.var_name = StringVar()
        abc.var_birthMark = StringVar()
        abc.var_nickname = StringVar()
        abc.var_arrest_date = StringVar()
        abc.var_address = StringVar()
        abc.var_father_name = StringVar()
        abc.var_wanted = StringVar()
        abc.var_occupation = StringVar()
        abc.var_case_id = StringVar()
        abc.var_age = StringVar()
        abc.var_crime_type = StringVar()
        abc.var_gender = StringVar()

        lt = Label(abc.root, text="CRIMINAL MANAGEMENT SYSTEM SOFTWARE", font=("times new roman", 40, "bold"),
                          bg="white", fg="blue")
        lt.place(x=0, y=0, width=1300, height=70)


        lmg=Frame(abc.root,bd=2,relief=RIDGE,bg='white')
        lmg.place(x=0,y=80,width=1550,height=200)

        #1st
        lm2 = Image.open('police2.jpg')
        lm2 = lm2.resize((490, 160), Image.ANTIALIAS)
        abc.photo_logo2 = ImageTk.PhotoImage(lm2)

        abc.logo2 = Label(lmg, image=abc.photo_logo2)
        abc.logo2.place(x=500, y=0, width=490, height=160)

        #2nd
        lm = Image.open('police1.jpg')
        lm = lm.resize((490, 160), Image.ANTIALIAS)
        abc.photo_logo = ImageTk.PhotoImage(lm)

        abc.logo = Label(lmg, image=abc.photo_logo)
        abc.logo.place(x=0, y=0, width=490, height=160)

        #3rd

        lm3 = Image.open('police3.jpg')
        lm3 = lm3.resize((490, 160), Image.ANTIALIAS)
        abc.photo_logo3 = ImageTk.PhotoImage(lm3)

        abc.logo3 = Label(lmg, image=abc.photo_logo3)
        abc.logo3.place(x=1000, y=0, width=280, height=160)



        # Main Frame
        mf = Frame(abc.root, bd=2, relief=RIDGE, bg='white')
        mf.place(x=10, y=200, width=1500, height=560)

        # upper Frame
        uf = LabelFrame(mf, bd=2, relief=RIDGE, bg='white', text='Criminal Information',
                                 font=('times new roman', 11, 'bold'), fg='red')
        uf.place(x=10, y=10, width=1480, height=270)

        # Labels and Entry fields
        caseid = Label(uf, text='Case ID:', font=('arial', 11, 'bold'), bg='white')
        caseid.grid(row=0, column=0, padx=2, sticky=W)

        caseentry = ttk.Entry(uf, textvariable=abc.var_case_id, width=22, font=("arial", 11, "bold"))
        caseentry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Criminal NO
        lbl_criminal_no = Label(uf, font=("arial", 12, "bold"), text="Criminal NO:", bg="white")
        lbl_criminal_no.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_criminal_no = ttk.Entry(uf, textvariable=abc.var_criminal_no, width=22,
                                    font=("arial", 11, "bold"))
        txt_criminal_no.grid(row=0, column=3, padx=2, pady=7)

        # Criminal Name
        lbl_Name = Label(uf, font=("arial", 12, "bold"), text="Criminal Name:", bg="white")
        lbl_Name.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_Name = ttk.Entry(uf, textvariable=abc.var_name, width=22, font=("arial", 11, "bold"))
        txt_Name.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # NickName
        lbl_nickname = Label(uf, font=("arial", 12, "bold"), text="NickName:", bg="white")
        lbl_nickname.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_nickname = ttk.Entry(uf, textvariable=abc.var_nickname, width=22, font=("arial", 11, "bold"))
        txt_nickname.grid(row=1, column=3, padx=2, pady=7)

        # Arrest Date
        lbl_arrestDate = Label(uf, font=("arial", 12, "bold"), text="Arrest Date:", bg="white")
        lbl_arrestDate.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_arrestDate = ttk.Entry(uf, textvariable=abc.var_arrest_date, width=22, font=("arial", 11, "bold"))
        txt_arrestDate.grid(row=2, column=1, padx=2, pady=7)

        # Date of Crime
        lbl_dateOfCrime = Label(uf, font=("arial", 12, "bold"), text="Date of Crime:", bg="white")
        lbl_dateOfCrime.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        txt_dateOfCrime = ttk.Entry(uf, textvariable=abc.var_date_of_crime, width=22,
                                    font=("arial", 11, "bold"))
        txt_dateOfCrime.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # Address
        lbl_address = Label(uf, font=("arial", 12, "bold"), text="Address:", bg="white")
        lbl_address.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_address = ttk.Entry(uf, textvariable=abc.var_address, width=22, font=("arial", 11, "bold"))
        txt_address.grid(row=3, column=1, padx=2, pady=7)

        # Age
        lbl_age = Label(uf, font=("arial", 12, "bold"), text="Age:", bg="white")
        lbl_age.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_age = ttk.Entry(uf, textvariable=abc.var_age, width=22, font=("arial", 11, "bold"))
        txt_age.grid(row=3, column=3, padx=2, pady=7)

        # occupution
        lbl_occupution = Label(uf, font=("arial", 12, "bold"), text="Occupation:", bg="white")
        lbl_occupution.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_occupution = ttk.Entry(uf, textvariable=abc.var_occupation, width=22, font=("arial", 11, "bold"))
        txt_occupution.grid(row=4, column=1, padx=2, pady=7)

        # birthMark
        lbl_birthMark = Label(uf, font=("arial", 12, "bold"), text="Birth Mark:", bg="white")
        lbl_birthMark.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        txt_birthmark = ttk.Entry(uf, textvariable=abc.var_birthMark, width=22, font=("arial", 11, "bold"))
        txt_birthmark.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        # Crime Type
        lbl_crimeType = Label(uf, font=("arial", 12, "bold"), text="Crime Type:", bg="white")
        lbl_crimeType.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_crimeType = ttk.Entry(uf, textvariable=abc.var_crime_type, width=22, font=("arial", 11, "bold"))
        txt_crimeType.grid(row=0, column=5, padx=2, pady=7)

        # # Father Name
        lbl_fatherName = Label(uf, font=("arial", 12, "bold"), text="Father Name:", bg="white")
        lbl_fatherName.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_fatherName = ttk.Entry(uf, textvariable=abc.var_father_name, width=22, font=("arial", 11, "bold"))
        txt_fatherName.grid(row=1, column=5, padx=2, pady=7)

        # Radio Frame
        radio_frame_gender = Frame(uf, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=730, y=90, width=190, height=30)

        lbl_gender = Label(uf, font=("arial", 12, "bold"), text="Gender:", bg="white")
        lbl_gender.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        male = Radiobutton(radio_frame_gender, variable=abc.var_gender, text='Male', value='male',
                           font=('arial', 9, 'bold'), bg='white')
        male.grid(row=2, column=5, pady=2, padx=5, sticky=W)
        abc.var_gender.set('male')

        female = Radiobutton(radio_frame_gender, variable=abc.var_gender, text='Female', value='female',
                             font=('arial', 9, 'bold'), bg='white')
        female.grid(row=2, column=6, pady=2, padx=5, sticky=W)

        # Most wantes

        lbl_wanted = Label(uf, font=("arial", 12, "bold"), text="Most Wanted:", bg="white")
        lbl_wanted.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        radio_frame_wanted = Frame(uf, bd=2, relief=RIDGE, bg='white')
        radio_frame_wanted.place(x=730, y=130, width=190, height=30)

        yes = Radiobutton(radio_frame_wanted, variable=abc.var_wanted, text='Yes', value='yes',
                          font=('arial', 9, 'bold'), bg='white')
        yes.grid(row=2, column=5, pady=2, padx=5, sticky=W)
        abc.var_wanted.set('yes')

        no = Radiobutton(radio_frame_wanted, variable=abc.var_wanted, text='No', value='no', font=('arial', 9, 'bold'),
                         bg='white')
        no.grid(row=2, column=6, pady=2, padx=5, sticky=W)

        # Button Frame
        button_frame = Frame(uf, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)

        btn_add = Button(button_frame, text="Record Save", command=abc.add_data, font=("arial", 13, "bold"), width=14,
                         bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)

        btn_update = Button(button_frame, text="Update", command=abc.update_data, font=("arial", 13, "bold"), width=14,
                            bg='blue', fg='white')
        btn_update.grid(row=0, column=1, padx=1, pady=5)

        btn_delete = Button(button_frame, text="Delete", command=abc.delete_data, font=("arial", 13, "bold"), width=14,
                            bg='blue', fg='white')
        btn_delete.grid(row=0, column=2, padx=1, pady=5)

        btn_clear = Button(button_frame, text="Clear", command=abc.reset_data, font=("arial", 13, "bold"), width=14,
                           bg='blue', fg='white')
        btn_clear.grid(row=0, column=3, padx=1, pady=5)

        lm4 = Image.open('criminal1.jpg')
        lm4 = lm4.resize((220, 220), Image.ANTIALIAS)
        abc.photo_logo4 = ImageTk.PhotoImage(lm4)

        abc.logo4 = Label(uf, image=abc.photo_logo4)
        abc.logo4.place(x=1000, y=0, width=220, height=220)

        # down Frame
        down_frame = LabelFrame(mf, bd=2, relief=RIDGE, bg='white', text='Criminal Information Table',
                                font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=10, y=280, width=1480, height=270)

        # Search Frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white', text='Search Criminal Record',
                                  font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_by = Label(search_frame, font=("arial", 11, "bold"), text="Search By:", fg="white", bg="red")
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        # search
        abc.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame, textvariable=abc.var_com_search, state="readonly",
                                      font=("arial", 12, "bold"), width=18)
        com_txt_search['value'] = ("Select Option", "Case_id", "Criminal_no")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        abc.var_search = StringVar()
        txt_search = ttk.Entry(search_frame, textvariable=abc.var_search, width=22, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        btn__search = Button(search_frame, text="Search", command=abc.serach_data, font=("arial", 11, "bold"),
                             width=14, bg="blue", fg="white")
        btn__search.grid(row=0, column=3, padx=5)

        btn_ShowAll = Button(search_frame, text="Show All", command=abc.fetch_data, font=("arial", 11, "bold"),
                             width=14, bg="blue", fg="white")
        btn_ShowAll.grid(row=0, column=4, padx=5)

        stayhome = Label(search_frame, text="NATIONAL CRIME AGENCY", font=("times new roman", 30, "bold"), fg="crimson",
                         bg="white")
        stayhome.place(x=10, y=280, width=600, height=30)

        # lm_mask=Image.open(r"images\backgound.jpg")
        # lm_mask=lm_mask.resize((50,50),Image.ANTIALIAS)
        # abc.photolm_mask=ImageTk.PhotoImage(lm_mask)

        # abc.logo=Label(search_frame,image=abc.photolm_mask)
        # abc.logo.place(x=900,y=0,width=50,height=30)

        # ============= Criminal table========================
        # Table Frame
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1170, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        abc.criminal_table = ttk.Treeview(table_frame, column=(
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=abc.criminal_table.xview)
        scroll_y.config(command=abc.criminal_table.yview)

        abc.criminal_table.heading('1', text='CaseId')
        abc.criminal_table.heading("2", text="CrimeNo")
        abc.criminal_table.heading("3", text="Criminal Name")
        abc.criminal_table.heading("4", text="NickName")
        abc.criminal_table.heading("5", text="ArrestDate")
        abc.criminal_table.heading("6", text="CrimeOfDate")
        abc.criminal_table.heading("7", text="Address")
        abc.criminal_table.heading("8", text="Age")
        abc.criminal_table.heading("9", text="Occupation")
        abc.criminal_table.heading("10", text="Birth Mark")
        abc.criminal_table.heading("11", text="Crime Type")
        abc.criminal_table.heading("12", text="Father Name")
        abc.criminal_table.heading("13", text="Gender")
        abc.criminal_table.heading("14", text="Wanted")

        abc.criminal_table['show'] = 'headings'

        abc.criminal_table.column("1", width=100)
        abc.criminal_table.column("2", width=100)
        abc.criminal_table.column("3", width=100)
        abc.criminal_table.column("4", width=100)
        abc.criminal_table.column("5", width=100)
        abc.criminal_table.column("6", width=100)
        abc.criminal_table.column("7", width=100)
        abc.criminal_table.column("8", width=100)
        abc.criminal_table.column("9", width=100)
        abc.criminal_table.column("10", width=100)
        abc.criminal_table.column("11", width=100)
        abc.criminal_table.column("12", width=100)
        abc.criminal_table.column("13", width=100)
        abc.criminal_table.column("14", width=100)

        abc.criminal_table.pack(fill=BOTH, expand=1)
        abc.criminal_table.bind("<ButtonRelease>", abc.get_cursor)
        abc.fetch_data()

    # *************Function Declarations*******************

    def add_data(abc):
        if abc.var_criminal_no.get() == "" or abc.var_nickname.get() == "":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='root',
                                               database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into criminal1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (

                    abc.var_case_id.get(),
                    abc.var_criminal_no.get(),
                    abc.var_name.get(),
                    abc.var_nickname.get(),
                    abc.var_arrest_date.get(),
                    abc.var_date_of_crime.get(),
                    abc.var_address.get(),
                    abc.var_age.get(),

                    abc.var_occupation.get(),
                    abc.var_birthMark.get(),
                    abc.var_crime_type.get(),
                    abc.var_father_name.get(),
                    abc.var_gender.get(),
                    abc.var_wanted.get()

                ))
                conn.commit()
                abc.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Criminal record has been added!', parent=abc.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=abc.root)

    # fetch Data
    def fetch_data(abc):
        conn = mysql.connector.connect(host='localhost', user='root', password='root', database='management')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from criminal1')
        data = my_cursor.fetchall()
        if len(data) != 0:
            abc.criminal_table.delete(*abc.criminal_table.get_children())
            for i in data:
                abc.criminal_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor

    def get_cursor(abc, event=""):
        cursor_row = abc.criminal_table.focus()
        content = abc.criminal_table.item(cursor_row)
        data = content['values']

        abc.var_case_id.set(data[0])
        abc.var_criminal_no.set(data[1])
        abc.var_name.set(data[2])
        abc.var_nickname.set(data[3])
        abc.var_arrest_date.set(data[4])
        abc.var_date_of_crime.set(data[5])
        abc.var_address.set(data[6])
        abc.var_age.set(data[7])
        abc.var_occupation.set(data[8])
        abc.var_birthMark.set(data[9])
        abc.var_crime_type.set(data[10])
        abc.var_father_name.set(data[11])
        abc.var_gender.set(data[12])
        abc.var_wanted.set(data[13])

    def update_data(abc):
        if abc.var_criminal_no.get() == "" or abc.var_nickname.get() == "":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are sure update this criminal record')
                if update > 0:
                    conn = mysql.connector.connect(host='localhost', user='root', password='root',
                                                   database='management')
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        'update criminal1 set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',
                        (

                            abc.var_criminal_no.get(),
                            abc.var_name.get(),
                            abc.var_nickname.get(),
                            abc.var_arrest_date.get(),
                            abc.var_date_of_crime.get(),
                            abc.var_address.get(),
                            abc.var_age.get(),
                            abc.var_occupation.get(),
                            abc.var_birthMark.get(),
                            abc.var_crime_type.get(),
                            abc.var_father_name.get(),
                            abc.var_gender.get(),
                            abc.var_wanted.get(),
                            abc.var_case_id.get(),

                        ))
                else:
                    if not update:
                        return
                conn.commit()
                abc.fetch_data()
                conn.close()
                messagebox.showinfo('success', 'Criminal record successfully updated', parent=abc.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=abc.root)

    # Delete
    def delete_data(abc):
        if abc.var_case_id.get() == "":
            messagebox.showerror('Error', "All fields are required")
        else:
            try:
                Delete = messagebox.askyesno('Delele', 'Are you sure delete this criminal', parent=abc.root)
                if Delete > 0:
                    conn = mysql.connector.connect(host='localhost', user='root', password='root',
                                                   database='management')
                    my_cursor = conn.cursor()
                    sql = 'delete from criminal1 where Case_id=%s'
                    value = (abc.var_case_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not Delete:
                        return
                conn.commit()
                abc.fetch_data()
                conn.close()
                messagebox.showinfo('Delete', 'Criminal record Successfully Deleted', parent=abc.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=abc.root)

    # reset

    def reset_data(abc):
        abc.var_case_id.set("")
        abc.var_criminal_no.set("")
        abc.var_name.set("")
        abc.var_nickname.set("")
        abc.var_arrest_date.set("")
        abc.var_date_of_crime.set("")
        abc.var_address.set("")
        abc.var_age.set("")
        # abc.var_occupationcomb.set("Select ID Proof")
        abc.var_occupation.set("")
        abc.var_birthMark.set("")
        abc.var_crime_type.set("")
        abc.var_father_name.set("")
        abc.var_gender.set("")
        abc.var_wanted.set("")

    # search
    def serach_data(abc):
        if abc.var_com_search.get() == '' or abc.var_search.get() == '':
            messagebox.showerror('Error', 'Please select option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='root',
                                               database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from criminal1 where ' + str(abc.var_com_search.get()) + " LIKE'%" + str(
                    abc.var_search.get() + "%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    abc.criminal_table.delete(*abc.criminal_table.get_children())
                    for i in rows:
                        abc.criminal_table.insert("", END, values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=abc.root)

############################################


if __name__ == "__main__":
    main()

