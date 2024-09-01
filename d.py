from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Criminal:
    def __init__(self, root):
        self.root = root
        # defining the dimensions of the window
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        # creation of the label of the software and aedding the required modifications
        lbl_title = Label(self.root, text='CRIMINAL MANAGEMENT SYSTEM', font=('Lucida Console', 40, 'bold'),
                          bg='#51B4E6', fg='black')
        # placing the title on the window
        lbl_title.place(x=0, y=0, width=1530, height=70)

        # LOGO for the page
        img_logo = Image.open('heredity.jfif')
        img_logo = img_logo.resize((60, 60), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=150, y=5, width=50, height=60)

        # Frame for the crime data input
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=10, y=200, width=150, height=560)

        upper_frame = Frame(main_frame, bd=2, relief=RIDGE, bg='white')
        upper_frame.place(x=10, y=200, width=1480, height=270)


if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()