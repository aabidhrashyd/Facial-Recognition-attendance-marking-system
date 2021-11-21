from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD, Font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongition Attendance Marking System")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_faculty = StringVar()
        self.var_gender = StringVar()
        self.var_DOB = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_parmaddress = StringVar()
        self.var_island = StringVar()
        self.var_present = StringVar()

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
            bkg_image, text="STUDENT MANAGMENT", font=("Impact", 35, BOLD),  fg="Black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bkg_image, bd=2)
        main_frame.place(x=0, y=46, width=1500, height=660)
#########################################################################
        # left lable frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=580)

        # current course
        Current_course = LabelFrame(
            Left_frame, bg="white", relief=RIDGE, text="Current Course Information")
        Current_course.place(x=5, y=0, width=645, height=130)


################################
        # Department

        dep_label = Label(Current_course, text='Department', font=(
            "times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0)

        dep_combo = ttk.Combobox(Current_course, textvariable=self.var_dep, font=(
            "times new roman", 12), state="readonly", width=19)
        dep_combo["values"] = ("Select Department", "Computer Science",
                               "Civil Enginerring", "Mechanical Enginerring", "Architechter Designing")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

#################################
        # Courses

        course_label = Label(Current_course, text='Courses', font=(
            "times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(Current_course, textvariable=self.var_course, font=(
            "times new roman", 12), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "CS",
                                  "IT", "MB", "FE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
#####################################
        # Year
        year_label = Label(Current_course, text='Year', font=(
            "times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_label = ttk.Combobox(Current_course, textvariable=self.var_year, font=(
            "times new roman", 12), state="readonly", width=20)
        year_label["values"] = ("Select Year", "2019-21",
                                "2021-22", "2022-23", "2024-25")
        year_label.current(0)
        year_label.grid(row=1, column=1, padx=2, pady=10, sticky=W)

############################################
        # Semester
        sem_label = Label(Current_course, text='Semester', font=(
            "times new roman", 12, "bold"))
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_label = ttk.Combobox(Current_course, textvariable=self.var_semester, font=(
            "times new roman", 12), state="readonly", width=20)
        sem_label["values"] = ("Select Semester", "Sem 1", "Sem 2")
        sem_label.current(0)
        sem_label.grid(row=1, column=3, padx=2, pady=10, sticky=W)
############################################

        # Class Student Information
        Class_frame = LabelFrame(
            Left_frame, bg="white", relief=RIDGE, text="Class Student Information")
        Class_frame.place(x=5, y=130, width=645, height=420)


###################################################
        # std ID
        std_id = Label(Class_frame, text='Student ID', font=(
            "times new roman", 12, "bold"))
        std_id.grid(row=0, column=0, padx=10, sticky=W)

        std_id_entry = ttk.Entry(Class_frame, textvariable=self.var_std_id, width=20,
                                 font=("times new roman", 13, "bold"))
        std_id_entry.grid(row=0, column=1, padx=10, sticky=W)

#############################################################
        # std name
        std_name = Label(Class_frame, text='Student Name', font=(
            "times new roman", 12, "bold"))
        std_name.grid(row=0, column=2, padx=10, sticky=W)

        std_name_entry = ttk.Entry(Class_frame, textvariable=self.var_std_name, width=20,
                                   font=("times new roman", 13, "bold"))
        std_name_entry.grid(row=0, column=3, padx=10, pady=5,  sticky=W)

#################################################################
        # Faculty
        Faculty_name = Label(Class_frame, text='Faculty', font=(
            "times new roman", 12, "bold"))
        Faculty_name.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        Faculty_name_entry = ttk.Entry(Class_frame, textvariable=self.var_faculty, width=20,
                                       font=("times new roman", 13, "bold"))
        Faculty_name_entry.grid(row=1, column=1, padx=10, pady=5,  sticky=W)

#################################################################
        # Gender
        gender_name = Label(Class_frame, text='Gender', font=(
            "times new roman", 12, "bold"))
        gender_name.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        gender_name_entry = ttk.Entry(Class_frame, textvariable=self.var_gender, width=20,
                                      font=("times new roman", 13, "bold"))
        gender_name_entry.grid(row=1, column=3, padx=10, pady=5,  sticky=W)

####################################################################
        # DOB
        dob_name = Label(Class_frame, text='DOB', font=(
            "times new roman", 12, "bold"))
        dob_name.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        dob_name_entry = ttk.Entry(Class_frame, textvariable=self.var_DOB, width=20,
                                   font=("times new roman", 13, "bold"))
        dob_name_entry.grid(row=2, column=1, padx=10, pady=5,  sticky=W)


####################################################################
        # Email
        Email_name = Label(Class_frame, text='Email', font=(
            "times new roman", 12, "bold"))
        Email_name.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        Email_name_entry = ttk.Entry(Class_frame, textvariable=self.var_email, width=20,
                                     font=("times new roman", 13, "bold"))
        Email_name_entry.grid(row=2, column=3, padx=10, pady=5,  sticky=W)

####################################################################
        # Phone
        Phone_name = Label(Class_frame, text='Phone Number', font=(
            "times new roman", 12, "bold"))
        Phone_name.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Phone_name_entry = ttk.Entry(Class_frame, textvariable=self.var_phone, width=20,
                                     font=("times new roman", 13, "bold"))
        Phone_name_entry.grid(row=3, column=1, padx=10, pady=5,  sticky=W)


####################################################################
        # Parment address
        Paddress_name = Label(Class_frame, text='Parmenent Address', font=(
            "times new roman", 12, "bold"))
        Paddress_name.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Paddress_name_entry = ttk.Entry(Class_frame, textvariable=self.var_parmaddress, width=20,
                                        font=("times new roman", 13, "bold"))
        Paddress_name_entry.grid(row=3, column=3, padx=10, pady=5,  sticky=W)

####################################################################
        # Island/City
        location_name = Label(Class_frame, text='Island/City', font=(
            "times new roman", 12, "bold"))
        location_name.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        location_name_entry = ttk.Entry(Class_frame, textvariable=self.var_island, width=20,
                                        font=("times new roman", 13, "bold"))
        location_name_entry.grid(row=4, column=1, padx=10, pady=5,  sticky=W)

####################################################################
        # Present address
        Present_address_name = Label(Class_frame, text='Present Address', font=(
            "times new roman", 12, "bold"))
        Present_address_name.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Present_address_name_entry = ttk.Entry(Class_frame, textvariable=self.var_present, width=20,
                                               font=("times new roman", 13, "bold"))
        Present_address_name_entry.grid(
            row=4, column=3, padx=10, pady=5,  sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        controlbtn1 = ttk.Radiobutton(
            Class_frame, variable=self.var_radio1, text='Take a Photo', value="Yes")
        controlbtn1.grid(row=6, column=0)

        self.var_radio2 = StringVar()
        controlbtn2 = ttk.Radiobutton(
            Class_frame, variable=self.var_radio2, text='No Photo Sample', value="No")
        controlbtn2.grid(row=6, column=1)

        # buttons frame
        btn_frame = Frame(Class_frame, bd=2, relief=RIDGE, bg="White")
        btn_frame.place(x=0, y=200, width=715, height=70)

        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=24, font=(
            "times new roman", 13, "bold"), bg="#A877BA", fg="Blue")
        save_btn.grid(row=0, column=0)

        Update_btn = Button(btn_frame, text="Update", width=24, font=(
            "times new roman", 13, "bold"), bg="#A877BA", fg="Blue")
        Update_btn.grid(row=0, column=1)

        Delete_btn = Button(btn_frame, text="Delete", width=24, font=(
            "times new roman", 13, "bold"), bg="#A877BA", fg="Blue")
        Delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", bg="Black", fg="Blue", width=17, font=(
            "times new roman", 13, "bold"))
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(Class_frame, bd=2, relief=RIDGE, bg="White")
        btn_frame1.place(x=0, y=235, width=715, height=30)

        take_photo_btn = Button(btn_frame1, text="Take a photo sample", bg="Black", fg="BLUE", width=35, font=(
            "IMPACT", 13))
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="update a photo sample", bg="Black", fg="BLUE", width=35, font=(
            "IMPACT", 13))
        update_photo_btn.grid(row=1, column=2)

###################################################

        # right lable frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=710, y=10, width=720, height=580)

        # search course
        search_frame = LabelFrame(
            Right_frame, bg="white", relief=RIDGE, text="Search")
        search_frame.place(x=5, y=0, width=700, height=70)

        search_label = Label(search_frame, text="Search By: ", font=(
            "times new roman", 15, "bold"), bg="red", fg="White")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12), state="readonly", width=20)
        search_combo["values"] = ("Select", "student Id", "Phone Number",
                                  "Student Name", "Island/City", "Email", "Faculty")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20,
                                 font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5,  sticky=W)

        search_btn = Button(search_frame, text="Search", width="14", font=(
            "time new roman", 13, "bold"), bg="black", fg="blue")
        search_btn.grid(row=0, column=3)

        showall_btn = Button(search_frame, text="Show All", width="14", font=(
            "time new roman", 13, "bold"), bg="black", fg="blue")
        showall_btn.grid(row=0, column=4)

        # Table Frame
        table_frame = Frame(
            Right_frame, bg="white", bd=2, relief=RIDGE)
        table_frame.place(x=5, y=70, width=700, height=440)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "island/city",
                                                               "dob", "email", "phone", "address", "gender"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Courses")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")  # done
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("island/city", text="Island/City")  # done
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="phone")
        self.student_table.heading("address", text="Present Address")
        self.student_table.heading("gender", text="Gender")
        self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)

        # ===functions error showing here $$$$$$$$$$$$$$$$$$$$$
    def add_data(self):
        if self.var_dep.get() == "Select Department" == "":
            # or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "ERROR!!", "ALL FIELDS ARE REQUIRED", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Aabidh@apple", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_std_id.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_dep.get(),
                    self.var_std_name.get(),
                    self.var_faculty.get(),
                    self.var_gender.get(),
                    self.var_DOB.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_parmaddress.get(),
                    self.var_island.get(),
                    self.var_present.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
