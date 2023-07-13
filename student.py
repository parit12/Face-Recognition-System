from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student's Informtion")


        #==========Variables==========
        self.var_name=StringVar()
    

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
        

        title_lbl=Label(bg_img,text="...STUDENT'S INFORMATION...", font=("Bahnschrift Condensed",35,"bold"),bg="white", fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame( bg_img, bd=2)
        main_frame.place(x=20,y=55,width=1485,height=710)

        #Left LabelFrame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Details",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="purple")
        Left_frame.place(x=10,y=10,width=600,height=580)

        #Current Course label
        Currentcourse_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        Currentcourse_frame.place(x=5,y=10,width=575,height=550)



        #Student's Name
        name_label=Label(Currentcourse_frame,text="Student's Name", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        name_label.grid(row=0,column=0,padx=15,sticky=W)
        name_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_name,font=("Bahnschrift Condensed",10,"bold"))
        name_text.grid(row=0,column=1,padx=1,pady=10,sticky=W)


        #Radio Buttons
        self.var_radio1=StringVar()
        radio1=ttk.Radiobutton(Currentcourse_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio1.grid(row=7,column=0,padx=10,pady=10,sticky=W)
        
        radio2=ttk.Radiobutton(Currentcourse_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio2.grid(row=7,column=1,padx=10,pady=10,sticky=W)


        #Button Frame
        btn_frame=Frame(Currentcourse_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=330,width=570,height=165)

        #extra
        save_btn=Button(btn_frame,text="Save",command=self.addf,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        save_btn.grid(row=0,column=0,padx=5,pady=5)

        #extra2
        delete_btn=Button(btn_frame,text="Delete",command=self.dele,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        delete_btn.grid(row=0,column=2,padx=10,pady=15)


        upload_btn=Button(btn_frame,text="Upload Sample",command=self.generate_dataset,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        upload_btn.grid(row=0,column=1,padx=10,pady=15)

       
        #============Function Declaration(ADD Data)==========
    def addf(self): 
        f = open ('parit.txt','r+')
        f.write(self.var_name.get())
        f.close()
        messagebox.showinfo("data " ,"Data is Saved",parent=self.root)
   
      

     #=============Delete Function================
    def dele(self):
        messagebox.showinfo("Delete" ,"Data Has been deleted" )

    #===============Generate Dataset/Take Photos==============
    def generate_dataset(self):
            try:
                #=====Load Predefined Data On Face Frontals from Open CV=====
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_crop(myframe) is not None:
                           img_id+=1
                           face=cv2.resize(face_crop(myframe),(450,450))
                           face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                           file_name='data/user.'+"0" "."+str(img_id)+".jpg"
                           cv2.imwrite(file_name,face)
                           cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                           cv2.imshow("Cropped Image",face)

                    if cv2.waitKey(1)==13 or int (img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset Completed!!",parent=self.root)    
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root) 

     

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()