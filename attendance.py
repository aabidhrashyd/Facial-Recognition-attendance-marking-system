# create a function in FR import data to csv.
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD, Font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np

# globle var
mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongition Attendance Marking System")

        # =====Variable========
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

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
            bkg_image, text="ATTENDANCE VIEW", font=("Impact", 35, BOLD),  fg="Black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bkg_image, bd=2)
        main_frame.place(x=0, y=46, width=1500, height=660)
#########################################################################
        # left lable frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=580)

        # label entering
        # Attendance ID
        attendance_id = Label(Left_frame, text='attendance_id', font=(
            "times new roman", 12, "bold"))
        attendance_id.grid(row=0, column=0, padx=10, sticky=W)

        attendance_id = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_id,
                                  font=("times new roman", 13, "bold"))
        attendance_id.grid(row=0, column=1, padx=2, pady=10)

        # Name
        name_lable = Label(Left_frame, text='Name', font=(
            "times new roman", 12, "bold"))
        name_lable.grid(row=0, column=2, padx=4, sticky=W)

        name_dis = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_name,
                             font=("times new roman", 13, "bold"))
        name_dis.grid(row=0, column=3, pady=8)

        # DEPARTMENT
        dep_lable = Label(Left_frame, text='Department', font=(
            "times new roman", 12, "bold"))
        dep_lable.grid(row=1, column=0, padx=4, sticky=W)

        dep_name = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_name,
                             font=("times new roman", 13, "bold"))
        dep_name.grid(row=1, column=1, pady=8)

        # Date
        date_label = Label(Left_frame, text='Date', font=(
            "times new roman", 12, "bold"))
        date_label.grid(row=1, column=2, padx=4, sticky=W)

        attn_date = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_date,
                              font=("times new roman", 13, "bold"))
        attn_date.grid(row=1, column=3, pady=8)

        # TIME
        time_lable = Label(Left_frame, text='Time', font=(
            "times new roman", 12, "bold"))
        time_lable.grid(row=2, column=0, padx=4, sticky=W)

        atten_time = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_time,
                               font=("times new roman", 13, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

        # attendance
        attn_lable = Label(Left_frame, text='Attendance', font=(
            "times new roman", 12, "bold"))
        attn_lable.grid(row=2, column=2)

        attn_combo = ttk.Combobox(Left_frame, textvariable=self.var_atten_attendance, font=(
            "times new roman", 12), state="readonly", width=19)
        attn_combo["values"] = ("Present", "Absent")
        attn_combo.current(0)
        attn_combo.grid(row=2, column=3,  pady=8)

        # buttons frame
        btn_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="White")
        btn_frame.place(x=0, y=200, width=715, height=70)

        import_btn = Button(btn_frame, command=self.importcsv, text="Import CSV", width=24, font=(
            "times new roman", 13, "bold"), bg="#A877BA", fg="Blue")
        import_btn.grid(row=0, column=0)

        Export_btn = Button(btn_frame,  text="Export CSV", command=self.exportCsv, width=24, font=(
            "times new roman", 13, "bold"), bg="#A877BA", fg="Blue")
        Export_btn.grid(row=0, column=1)

        Delete_btn = Button(btn_frame,  text="Delete", width=24, font=(
            "times new roman", 13, "bold"), bg="#A877BA", fg="Blue")
        Delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", bg="Black", fg="Blue", width=17, font=(
            "times new roman", 13, "bold"))
        reset_btn.grid(row=0, column=3)

        # right lable frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Datas", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=710, y=10, width=720, height=580)

        table_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, bg='white')
        table_frame.place(x=5, y=5, width=700, height=455)

        # scrollbar de
        scrollbar_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scrollbar_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendaceReportTable = ttk.Treeview(table_frame, column=(
            "id", "name", "department", "date", "time", "Status"), xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        scrollbar_x.config(command=self.AttendaceReportTable.xview)
        scrollbar_y.config(command=self.AttendaceReportTable.xview)

        self.AttendaceReportTable.heading("id", text="STD ID")
        self.AttendaceReportTable.heading("name", text="Student Name")
        self.AttendaceReportTable.heading("department", text="Department")
        self.AttendaceReportTable.heading("date", text="Date")
        self.AttendaceReportTable.heading("time", text="Time")
        self.AttendaceReportTable.heading("Status", text="Status")

        self.AttendaceReportTable["show"] = "headings"

        self.AttendaceReportTable.column("id", width=90)
        self.AttendaceReportTable.column("name", width=90)
        self.AttendaceReportTable.column("department", width=90)
        self.AttendaceReportTable.column("date", width=90)
        self.AttendaceReportTable.column("time", width=90)
        self.AttendaceReportTable.column("Status", width=90)

        self.AttendaceReportTable.pack(fill=BOTH, expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>", self.get_cursor)

        # ===========fetch data
    def fetch_data(self, rows):
        self.AttendaceReportTable.delete(
            *self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("", END, values=i)

    #import CSV
    def importcsv(self):
        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open Excel", filetypes=(
            ("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
        with open(file_name) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "NO DATA FOND :", parent=self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open Excel", filetypes=(
                ("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
            with open(file_name, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile)
                csvread = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your Data Exported")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due To:{str(es)}", parent=self.root)

    def get_cursor(self, i=""):
        cursor_row = self.AttendaceReportTable.focus()
        content = self.AttendaceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_time.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
