from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD, Font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongition Attendance Marking System")

        title_lbl = Label(self.root, text="Train Data set", font=(
            "Impact", 35, BOLD),  bg="Black", fg="White")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        b1_btn = Button(self.root, text="Train", command=self.train_classifier, width="14", font=(
            "time new roman", 13, "bold"), bg="black", fg="blue")
        b1_btn.place(x=0, y=380, width=1530, height=60)
        # very much okey up to here

    def train_classifier(self):
        data_dir = ("data")  # store in folder
        path = [os.path.join(data_dir, file)
                for file in os.listdir(data_dir)]  # path joined
        # print(path)

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # grayscal
            # print(img)
            imageNp = np.array(img, 'uint8')
           # print("Numpy")
            # print(imageNp)
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
           # print("this is ID")
           # print(id)
        #print(faces, ids)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        #classifier is clf
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        # stor after class
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training data completed")


"""

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongition Attendance Marking System")

        title_lbl = Label(self.root, text="Train Data set", font=(
            "Impact", 35, BOLD),  bg="Black", fg="White")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        b1_btn = Button(self.root, text="Train", command=self.train_classifier, width="14", font=(
            "time new roman", 13, "bold"), bg="black", fg="blue")
        b1_btn.place(x=0, y=380, width=1530, height=60)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file)
                for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # GrayScale Image
            print(img)
            imageNp = np.array(img, 'uint8')  # unit8 is datatype in array
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)  # converting to np

        # ======train classifers

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed")
"""

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
