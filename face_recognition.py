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
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongition Attendance Marking System")

        title_lbl = Label(self.root, text="Face Recognition", font=(
            "Impact", 35, BOLD),  bg="Black", fg="White")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        b1_btn = Button(self.root, text="Face Recognition", command=self.face_recog, width="14", font=(
            "time new roman", 13, "bold"), bg="black", fg="blue")
        b1_btn.place(x=0, y=380, width=1530, height=60)

        # ==============attendance==================
    def mark_attendance(self, s, i, c, d):
        with open("attendance_marking.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((s not in name_list) and (i not in name_list) and (c not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{i},{c},{d},{dtString},{d1},Present")

        # ==== face recognition

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for(x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Aabidh@apple", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select student_name from student where student_id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute(
                    "select department from student where student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute(
                    "select course from student where student_id="+str(id))
                c = my_cursor.fetchone()
                c = "+".join(c)

                my_cursor.execute(
                    "select student_id from student where student_id="+str(id))
                s = my_cursor.fetchone()
                # print(s)
                s = "+".join(s)

                # % of match
                if confidence > 89:
                    cv2.putText(
                        img, f"STD ID:{s}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"STD Name:{i}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Course:{c}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(s, i, c, d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h),
                                  (0, 0, 255), 3)  # red box
                    cv2.putText(img, "UnKnown Face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1,
                                  10, (255, 25, 255), "Face", clf)
            return img
        # read
        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
