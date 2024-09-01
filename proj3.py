from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2130x1190+0+0")
        self.root.title('CRIMINAL MANAGENET SYSTEM SOFTWARE')

        # Variables
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthMark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()

        lbl_title = Label(self.root, text="CRIMINAL MANAGENET SYSTEM SOFTWARE", font=("times new roman", 40, "bold"),
                          bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1530, height=70)

        # logo
        img_logo = Image.open('heredity.jfif')
        img_logo = img_logo.resize((60, 60), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=100, y=5, width=60, height=60)

        # Image Frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=65, width=1530, height=130)

        # 1st
        img1 = Image.open('heredity.jfif')
        img1 = img1.resize((540, 160), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=160)

        # # 2st
        img_2 = Image.open('heredity.jfif')
        img_2 = img_2.resize((540, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img_2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=540, y=0, width=540, height=160)

        # # 3st
        img_3 = Image.open('heredity.jfif')
        img_3 = img_3.resize((540, 160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img_3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1000, y=0, width=540, height=160)

        # Main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=200, width=1500, height=560)

        # upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Criminal Information',
                                 font=('times new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1480, height=270)

        # Labels and Entry fields
        caseid = Label(upper_frame, text='Case ID:', font=('arial', 11, 'bold'), bg='white')
        caseid.grid(row=0, column=0, padx=2, sticky=W)

        caseentry = ttk.Entry(upper_frame, textvariable=self.var_case_id, width=22, font=("arial", 11, "bold"))
        caseentry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Criminal NO
        lbl_criminal_no = Label(upper_frame, font=("arial", 12, "bold"), text="Criminal NO:", bg="white")
        lbl_criminal_no.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_criminal_no = ttk.Entry(upper_frame, textvariable=self.var_criminal_no, width=22,
                                    font=("arial", 11, "bold"))
        txt_criminal_no.grid(row=0, column=3, padx=2, pady=7)

        # Criminal Name
        lbl_Name = Label(upper_frame, font=("arial", 12, "bold"), text="Criminal Name:", bg="white")
        lbl_Name.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_Name = ttk.Entry(upper_frame, textvariable=self.var_name, width=22, font=("arial", 11, "bold"))
        txt_Name.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # NickName
        lbl_nickname = Label(upper_frame, font=("arial", 12, "bold"), text="NickName:", bg="white")
        lbl_nickname.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_nickname = ttk.Entry(upper_frame, textvariable=self.var_nickname, width=22, font=("arial", 11, "bold"))
        txt_nickname.grid(row=1, column=3, padx=2, pady=7)

        # Arrest Date
        lbl_arrestDate = Label(upper_frame, font=("arial", 12, "bold"), text="Arrest Date:", bg="white")
        lbl_arrestDate.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_arrestDate = ttk.Entry(upper_frame, textvariable=self.var_arrest_date, width=22, font=("arial", 11, "bold"))
        txt_arrestDate.grid(row=2, column=1, padx=2, pady=7)

        # Date of Crime
        lbl_dateOfCrime = Label(upper_frame, font=("arial", 12, "bold"), text="Date of Crime:", bg="white")
        lbl_dateOfCrime.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        txt_dateOfCrime = ttk.Entry(upper_frame, textvariable=self.var_date_of_crime, width=22,
                                    font=("arial", 11, "bold"))
        txt_dateOfCrime.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # Address
        lbl_address = Label(upper_frame, font=("arial", 12, "bold"), text="Address:", bg="white")
        lbl_address.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=22, font=("arial", 11, "bold"))
        txt_address.grid(row=3, column=1, padx=2, pady=7)

        # Age
        lbl_age = Label(upper_frame, font=("arial", 12, "bold"), text="Age:", bg="white")
        lbl_age.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_age = ttk.Entry(upper_frame, textvariable=self.var_age, width=22, font=("arial", 11, "bold"))
        txt_age.grid(row=3, column=3, padx=2, pady=7)

        # occupution
        lbl_occupution = Label(upper_frame, font=("arial", 12, "bold"), text="Occupation:", bg="white")
        lbl_occupution.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_occupution = ttk.Entry(upper_frame, textvariable=self.var_occupation, width=22, font=("arial", 11, "bold"))
        txt_occupution.grid(row=4, column=1, padx=2, pady=7)

        # birthMark
        lbl_birthMark = Label(upper_frame, font=("arial", 12, "bold"), text="Birth Mark:", bg="white")
        lbl_birthMark.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        txt_birthmark = ttk.Entry(upper_frame, textvariable=self.var_birthMark, width=22, font=("arial", 11, "bold"))
        txt_birthmark.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        # Crime Type
        lbl_crimeType = Label(upper_frame, font=("arial", 12, "bold"), text="Crime Type:", bg="white")
        lbl_crimeType.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_crimeType = ttk.Entry(upper_frame, textvariable=self.var_crime_type, width=22, font=("arial", 11, "bold"))
        txt_crimeType.grid(row=0, column=5, padx=2, pady=7)

        # # Father Name
        lbl_fatherName = Label(upper_frame, font=("arial", 12, "bold"), text="Father Name:", bg="white")
        lbl_fatherName.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_fatherName = ttk.Entry(upper_frame, textvariable=self.var_father_name, width=22, font=("arial", 11, "bold"))
        txt_fatherName.grid(row=1, column=5, padx=2, pady=7)

        # Radio Frame
        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=730, y=90, width=190, height=30)

        lbl_gender = Label(upper_frame, font=("arial", 12, "bold"), text="Gender:", bg="white")
        lbl_gender.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        male = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Male', value='male',
                           font=('arial', 9, 'bold'), bg='white')
        male.grid(row=2, column=5, pady=2, padx=5, sticky=W)
        self.var_gender.set('male')

        female = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Female', value='female',
                             font=('arial', 9, 'bold'), bg='white')
        female.grid(row=2, column=6, pady=2, padx=5, sticky=W)

        # Most wantes

        lbl_wanted = Label(upper_frame, font=("arial", 12, "bold"), text="Most Wanted:", bg="white")
        lbl_wanted.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        radio_frame_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_wanted.place(x=730, y=130, width=190, height=30)

        yes = Radiobutton(radio_frame_wanted, variable=self.var_wanted, text='Yes', value='yes',
                          font=('arial', 9, 'bold'), bg='white')
        yes.grid(row=2, column=5, pady=2, padx=5, sticky=W)
        self.var_wanted.set('yes')

        no = Radiobutton(radio_frame_wanted, variable=self.var_wanted, text='No', value='no', font=('arial', 9, 'bold'),
                         bg='white')
        no.grid(row=2, column=6, pady=2, padx=5, sticky=W)

        # backgound image
        img_crime = Image.open('heredity.jfif')
        img_crime = img_crime.resize((470, 245), Image.ANTIALIAS)
        self.photocrime = ImageTk.PhotoImage(img_crime)

        self.img_crime = Label(upper_frame, image=self.photocrime)
        self.img_crime.place(x=1000, y=0, width=470, height=245)

        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)

        #btn_add = Button(button_frame, text="Record Save", command=self.add_data, font=("arial", 13, "bold"), width=14,
                         #bg='blue', fg='white')
        #btn_add.grid(row=0, column=0, padx=3, pady=5)

        #btn_update = Button(button_frame, text="Update", command=self.update_data, font=("arial", 13, "bold"), width=14,
                            #bg='blue', fg='white')
        #btn_update.grid(row=0, column=1, padx=1, pady=5)

        #btn_delete = Button(button_frame, text="Delete", command=self.delete_data, font=("arial", 13, "bold"), width=14,
                            #bg='blue', fg='white')
        #btn_delete.grid(row=0, column=2, padx=1, pady=5)

        #btn_clear = Button(button_frame, text="Clear", command=self.reset_data, font=("arial", 13, "bold"), width=14,
                           #bg='blue', fg='white')
        #btn_clear.grid(row=0, column=3, padx=1, pady=5)

        # down Frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Criminal Information Table',
                                font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=10, y=280, width=1480, height=270)

        # Search Frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white', text='Search Criminal Record',
                                  font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_by = Label(search_frame, font=("arial", 11, "bold"), text="Search By:", fg="white", bg="red")
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        # search
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame, textvariable=self.var_com_search, state="readonly",
                                      font=("arial", 12, "bold"), width=18)
        com_txt_search['value'] = ("Select Option", "Case_id", "Criminal_no")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame, textvariable=self.var_search, width=22, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        #btn__search = Button(search_frame, text="Search", command=self.serach_data, font=("arial", 11, "bold"),
                             #width=14, bg="blue", fg="white")
        #btn__search.grid(row=0, column=3, padx=5)

        #btn_ShowAll = Button(search_frame, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"),
                             #width=14, bg="blue", fg="white")
        #btn_ShowAll.grid(row=0, column=4, padx=5)

        stayhome = Label(search_frame, text="NATIONAL CRIME AGENCY", font=("times new roman", 30, "bold"), fg="crimson",
                         bg="white")
        stayhome.place(x=780, y=0, width=600, height=30)


if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()