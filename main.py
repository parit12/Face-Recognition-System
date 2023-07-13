from tkinter import*
from tkinter import ttk
import tkinter
from tkinter.messagebox import askyesno
from PIL import Image,ImageTk
import os
from student import Student
from training import Train
from face_recognize import Face_Detection

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1330x710+0+0")
        self.root.title("Face_Recognition_System")

        #image1
        img=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-Recognition-System\image1.jpg")
        img=img.resize((510,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)

        #image2
        img1=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-Recognition-System\image4.jfif")
        img1=img1.resize((510,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=515,y=0,width=510,height=130)


        #image3
        img2=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-Recognition-System\image1.jpg")
        img2=img2.resize((510,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1030,y=0,width=510,height=130)
        

        #background_Image
        img3=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-Recognition-System\image5.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        

        title_lbl=Label(bg_img,text="...FACE RECOGNITION SYSTEM...", font=("Bahnschrift Condensed",35,"bold"),bg="white", fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=45)
         

        #Student Button
        img4=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-Recognition-System\student.jfif")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        #Student_Details(Image)
        b1=Button(bg_img,image=self.photoimg4,command=self.details,cursor="hand2")
        b1.place(x=200,y=50,width=220,height=220)

        #Student_Details(Text)
        b1_1=Button(bg_img,text="STUDENT'S INFORMATION",command=self.details,cursor="hand2",font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red")
        b1_1.place(x=200,y=250,width=220,height=40)


        #Face Detection Button
        img5=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-Recognition-System\face.jfif")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        #Face Detection(Image)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=50,width=220,height=220)

        #Face Detection(Text)
        b1_1=Button(bg_img,text="FACE DETECTION",cursor="hand2",font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red",command=self.face_data)
        b1_1.place(x=500,y=250,width=220,height=40)

       
        #Model Training
        img9=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-Recognition-System\model.jfif")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        #Model Training(Image)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=800,y=50,width=220,height=220)

        #Model Training(Text)
        b1_1=Button(bg_img,text="MODEL TRAINING",cursor="hand2",command=self.train_data,font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red")
        b1_1.place(x=800,y=250,width=220,height=40)


    def open_img(self):
        os.startfile("data")


    #==============Function Buttons=============
    def details(self):
     self.details=Toplevel(self.root)
     self.app=Student(self.details)

    def train_data(self):
     self.details=Toplevel(self.root)
     self.app=Train(self.details)

    def face_data(self):
     self.details=Toplevel(self.root)
     self.app=Face_Detection(self.details)



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
