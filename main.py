from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD, Font
from PIL import Image, ImageTk
from student import student


class Face_recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongition Attendance Marking System")

        # first pic
        img = Image.open(r"/Users/abidh/Desktop/FYP/bkg_images/blue.jpg")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        first_lbl = Label(self.root, image=self.photoimg)
        first_lbl.place(x=0, y=0, width=500, height=130)

        # second pic

        img1 = Image.open(r"/Users/abidh/Desktop/FYP/bkg_images/blue.jpg")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root, image=self.photoimg1)
        first_lbl.place(x=500, y=0, width=500, height=130)

        # third pic

        img2 = Image.open(r"/Users/abidh/Desktop/FYP/bkg_images/blue.jpg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_lbl = Label(self.root, image=self.photoimg2)
        first_lbl.place(x=1000, y=0, width=500, height=130)

        # bg image

        img3 = Image.open(r"/Users/abidh/Desktop/FYP/bkg_images/etc_nural.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bkg_image = Label(self.root, image=self.photoimg3)
        bkg_image.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bkg_image, text="FACIAL RECOGNITION ATTENDANCE MARKING SYSTEM", font=("Impact", 35, BOLD),  fg="Black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # std button
        img4 = Image.open(r"/Users/abidh/Desktop/FYP/bkg_images/student.png")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        button1 = Button(bkg_image, image=self.photoimg4,
                         command=self.student_details, cursor="hand2")
        button1.place(x=200, y=100, width=220, height=220)

        button1_1 = Button(bkg_image, text="Student Details", command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"),  fg="Black")
        button1_1.place(x=200, y=300, width=220, height=40)

        # detect button
        img5 = Image.open(r"/Users/abidh/Desktop/FYP/bkg_images/facereco.jpeg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        button1 = Button(bkg_image, image=self.photoimg5, cursor="hand2")
        button1.place(x=500, y=100, width=220, height=220)

        button1 = Button(bkg_image, text="Face Detector", cursor="hand2", font=(
            "times new roman", 15, "bold"),  fg="Black")
        button1.place(x=500, y=300, width=220, height=40)

 # Attendance button
        img6 = Image.open(
            r"/Users/abidh/Desktop/FYP/bkg_images/Attendance.jpeg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        button1 = Button(bkg_image, image=self.photoimg6, cursor="hand2")
        button1.place(x=800, y=100, width=220, height=220)

        button1 = Button(bkg_image, text="Attendance", cursor="hand2", font=(
            "times new roman", 15, "bold"),  fg="Black")
        button1.place(x=800, y=300, width=220, height=40)

 # Train Data button
        img7 = Image.open(
            r"/Users/abidh/Desktop/FYP/bkg_images/traindata.jpeg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        button1 = Button(bkg_image, image=self.photoimg7, cursor="hand2")
        button1.place(x=1100, y=100, width=220, height=220)

        button1 = Button(bkg_image, text="Train Data", cursor="hand2", font=(
            "times new roman", 15, "bold"),  fg="Black")
        button1.place(x=1100, y=300, width=220, height=40)

    # ======fuction======
    def student_details(self):
        self.__new__window = Toplevel(self.root)
        self.app = student(self.__new__window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_System(root)
    root.mainloop()
