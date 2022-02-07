import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysqltor
master=Tk()

master.title("HOME - REPORT CARD OF STUDENTS")
master.configure(bg="maroon")
master.geometry('1370x700')
master.resizable(False,False)

#                                                                       INTERFACE OF PYTHON MYSQL CONNECTION USING MYSQLCONNECTOR WITH TKINTER                                                                                                         

def create_db():
    mycon=mysqltor.connect(host='localhost',user='root',password='abi@95*13&04*15')
    cursor=mycon.cursor()
    cursor.execute('DROP DATABASE IF EXISTS report_card')
    cursor.execute('CREATE DATABASE report_card')
    cursor.execute('use report_card')
    cursor.execute('''CREATE TABLE STUDENTS_MARKS (Admission_Number int primary key,
                                            Exam_Number int not null unique,
                                            Student_Name varchar(50) Not Null,
                                            English int(100),
                                            Mathematics int(100),
                                            Physics int(100),
                                            Chemistry int(100),
                                            Biology int(100),
                                            Computer_Science int(100),
                                            English_Assignment int(100),
                                            Mathematics_Record int(100),
                                            Physics_Practicals int(100),
                                            Chemistry_Practicals int(100),
                                            Biology_Record int(100),
                                            ComputerScience_Practicals int(100))''')

    cursor.execute('''CREATE TABLE STUDENTS_PERSONAL_INFO (Admission_Number int primary key,
                                            Student_Name varchar(50) Not Null,
                                            Exam_Number int not null unique,
                                            Class int(100) not null,
                                            Date_of_Birth date not null,
                                            Gender char(10) not null,
                                            Father_Name varchar(100),
                                            Mother_Name varchar(100),
                                            School_Name varchar(100),
                                            Exammination_Board varchar(100),
                                            Language_Medium varchar(100),
                                            State varchar(100),
                                            Phone varchar(100) ,
                                            Email_ID varchar(100))''')
    mycon.commit()
    mycon.close()



#                                                                        NEW TOPLEVEL WINDOW FOR INSERTION OF STUDENTS PERSONAL DETAILS                                                                                                                        

def insert_students_personal_info_window():
    root=Toplevel(master)
    root.title("STUDENTS PERSONAL DETAILS")
    root.configure(bg="lemon chiffon")
    root.geometry("1400x700")
    root.resizable(False,False)

    #Creating Frames
    title_frame=Frame(root,bd=6,relief='ridge',bg='peach puff')
    title_frame.place(x=5,y=5,width=1355,height=690)

    title_label=Label(title_frame,text='STUDENTS PERSONAL DETAILS',bg='peach puff',font=('Times New Roman',40),fg='black')
    title_label.pack(anchor='center')

    top_frame=Frame(root,bd=6,bg='crimson',relief='groove')
    top_frame.place(x=20,y=100,width=1325,height=500)

    next_frame3=Frame(root,bd=6,bg='peach puff',relief='flat')
    next_frame3.place(x=1050,y=620,width=290,height=70)

    next_frame4=Frame(root,bd=6,bg='peach puff',relief='flat')
    next_frame4.place(x=20,y=620,width=600,height=50)

    

    #Creating Lables
    name_label=Label(top_frame,text="Student Name",font=('Times New Roman',22),bg='crimson',fg='white')
    name_label.grid(row=1,column=1,pady=10,padx=10,sticky=W,columnspan=4)
    grade_label=Label(top_frame,text="Class",font=('Times New Roman',22),bg='crimson',fg='white')
    grade_label.grid(row=1,column=3,pady=10,padx=10,sticky=W)
    father_name_label=Label(top_frame,text="Father Name",font=('Times New Roman',22),bg='crimson',fg='white')
    father_name_label.grid(row=5,column=1,pady=10,padx=10,sticky=W)
    mother_name_label=Label(top_frame,text="Mother Name",font=('Times New Roman',22),bg='crimson',fg='white')
    mother_name_label.grid(row=6,column=1,pady=10,padx=10,sticky=W)
    exam_no_label=Label(top_frame,text="Exam Number",font=('Times New Roman',22),bg='crimson',fg='white')
    exam_no_label.grid(row=3,column=1,pady=10,padx=10,sticky=W)
    dob_label=Label(top_frame,text="Date of Birth",font=('Times New Roman',22),bg='crimson',fg='white')
    dob_label.grid(row=2,column=3,pady=10,padx=10,sticky=W)
    school_name_label=Label(top_frame,text="School Name",font=('Times New Roman',22),bg='crimson',fg='white')
    school_name_label.grid(row=4,column=1,pady=10,padx=10,sticky=W)
    gender_label=Label(top_frame,text="Gender",font=('Times New Roman',22),bg='crimson',fg='white')
    gender_label.grid(row=3,column=3,pady=10,padx=10,sticky=W)
    state_label=Label(top_frame,text="State",font=('Times New Roman',22),bg='crimson',fg='white')
    state_label.grid(row=6,column=3,pady=10,padx=10,sticky=W)
    exam_board_label=Label(top_frame,text="Examination Board",font=('Times New Roman',22),bg='crimson',fg='white')
    exam_board_label.grid(row=4,column=3,pady=10,padx=10,sticky=W)
    language_medium_label=Label(top_frame,text="Language of Medium",font=('Times New Roman',22),bg='crimson',fg='white')
    language_medium_label.grid(row=5,column=3,pady=10,padx=10,sticky=W)
    phone_label=Label(top_frame,text="Phone Number",font=('Times New Roman',22),bg='crimson',fg='white')
    phone_label.grid(row=7,column=1,pady=10,padx=10,sticky=W)
    admission_no_label=Label(top_frame,text="Admission Number",font=('Times New Roman',22),bg='crimson',fg='white')
    admission_no_label.grid(row=2,column=1,pady=10,padx=10,sticky=W)
    email_id_label=Label(top_frame,text="Email ID",font=('Times New Roman',22),bg='crimson',fg='white')
    email_id_label.grid(row=8,column=1,pady=10,padx=10,sticky=W)

    #Creating Label Entries
    name=Entry(top_frame,width=50,state='normal',font=('Times New Roman',15))
    name.grid(row=1,column=2,pady=10,ipady=5)
    father_name=Entry(top_frame,width=50,state='normal',font=('Times New Roman',15))
    father_name.grid(row=5,column=2,pady=10,ipady=5)
    mother_name=Entry(top_frame,width=50,font=('Times New Roman',15))
    mother_name.grid(row=6,column=2,pady=10,ipady=5)
    exam_no=Entry(top_frame,width=50,font=('Times New Roman',15))
    exam_no.grid(row=3,column=2,pady=10,ipady=5)
    school_name=Entry(top_frame,width=50,font=('Times New Roman',15))
    school_name.grid(row=4,column=2,pady=10,ipady=5)
    phone_no=Entry(top_frame,width=50,font=('Times New Roman',15))
    phone_no.grid(row=7,column=2,pady=10,ipady=5)
    admission_no=Entry(top_frame,width=50,font=('Times New Roman',15))
    admission_no.grid(row=2,column=2,pady=10,ipady=5)
    email_id=Entry(top_frame,width=50,font=('Times New Roman',15))
    email_id.grid(row=8,column=2,pady=10,ipady=5)

    #Creating Dropdown Box 
    grade_options=[1,2,3,4,5,6,7,8,9,10,11,12]
    clicked1=IntVar()
    clicked1.set(10)
    grade_box=OptionMenu(top_frame,clicked1, *grade_options)
    grade_box.grid(row=1,column=4,pady=10,sticky=W,ipadx=9)

    dob_date_options=[]
    for i in range (1,32):
        dob_date_options.append(i)
    clicked2=IntVar()
    clicked2.set(13)
    dob_date=OptionMenu(top_frame,clicked2, *dob_date_options)
    dob_date.grid(row=2,column=4,pady=10,sticky=W,ipadx=9)

    dob_month_options=[]
    for i in range (1,13):
        dob_month_options.append(i)
    clicked3=IntVar()
    clicked3.set(10)
    dob_month=OptionMenu(top_frame,clicked3, *dob_month_options)
    dob_month.grid(row=2,column=5,ipadx=6,sticky=W)    

    dob_year_options=[]
    for i in range (1990,2010):
        dob_year_options.append(i)
    clicked4=IntVar()
    clicked4.set(1995)
    dob_year=OptionMenu(top_frame,clicked4, *dob_year_options)
    dob_year.grid(row=2,column=6,sticky=W,padx=5)    

    language_options=["Tamil","Hindi","Assam",'Bengale','Gujarati','Kashmiri','Malayalam','Marathi','French','German','Spanish','Korean','Chinese','Japanese','Thai','English','Turkish','Arabic','Russian','Oriya','Kannada','Konkani','Manipuri','Nepali','Punjabi','Sanskrit','Sindhi','Telugu','Urdu','Bodo','Santhali','Maithili','Dogri']
    clicked5=StringVar()
    clicked5.set('English')
    language_box=OptionMenu(top_frame,clicked5, *language_options)
    language_box.grid(row=5,column=4,pady=10,sticky=W)

    state_options=["Kerala",'Andhra Pradesh','Arunachal Pradesh','Bihar','Busan','Seoul','Ilsan','Itaewon','Goa','Gujarat',"Tamil Nadu",'Jammu & Kashmir','Jharkhand','West Bengal','Karnataka','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Punjab','Rajasthan','Sikkim','Tripura','Uttaranchal','Uttar Pradesh','Haryana','Himachal Pradesh','Chattisgarh','Delhi','Chandigarh','Pondicherry']
    clicked6=StringVar()
    clicked6.set('Seoul')
    state_box=OptionMenu(top_frame,clicked6, *state_options)
    state_box.grid(row=6,column=4,pady=10,sticky=W)

    #Creating Radio Button
    clicked7=StringVar()
    clicked7.set("Female")
    gender_box=Radiobutton(top_frame,text="Male",variable=clicked7,value='Male')
    gender_box.grid(row=3,column=4,pady=10,sticky=W,ipadx=12)
    gender_box2=Radiobutton(top_frame,text="Female",variable=clicked7,value='Female')                
    gender_box2.grid(row=3,column=5,pady=10,sticky=W)                                                                                                                 

    clicked8=StringVar()
    clicked8.set("CBSE")
    examboard_box=Radiobutton(top_frame,text="CBSE",variable=clicked8,value='CBSE')
    examboard_box.grid(row=4,column=4,pady=10,sticky=W,ipadx=12)
    examboard_box2=Radiobutton(top_frame,text="ICSE",variable=clicked8,value='ICSE')
    examboard_box2.grid(row=4,column=5,pady=10,sticky=W,ipadx=10)
    examboard_box3=Radiobutton(top_frame,text="State Board",variable=clicked8,value='State Board')
    examboard_box3.grid(row=4,column=6,pady=10,padx=5,sticky=W)

    def inserting_details():
        add1=admission_no.get()
        add2=str(name.get())
        add3=str(exam_no.get())
        add4=str(clicked1.get())
        add5=str(clicked4.get())+'-'+str(clicked3.get())+'-'+str(clicked2.get())
        add6=str(clicked7.get())
        add7=str(father_name.get())
        add8=str(mother_name.get())
        add9=str(school_name.get())
        add10=str(clicked8.get())
        add11=str(clicked5.get())
        add12=str(clicked6.get())
        add13=str(phone_no.get())
        add14=str(email_id.get())

        #INTERFACE PYTHON MYSQL
        mycon=mysqltor.connect(host='localhost',user='root',password='abi@95*13&04*15')
        cursor=mycon.cursor()
        cursor.execute("use report_card")
        cursor.execute('insert into students_personal_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10,add11,add12,add13,add14))
        mycon.commit()
        mycon.close()
        insert_label=Label(next_frame4,text='Inserted Successfully Into The Table....',font=('Times New Roman',20),bg='peach puff',fg='black')
        insert_label.pack()

    
    submit_btn=Button(next_frame3,text='SAVE',command=inserting_details,bg='crimson',relief='groove',bd=4,font=('Baskerville Old Face',20) )
    submit_btn.grid(row=0,column=2,padx=10,ipadx=20)

    quit_btn=Button(next_frame3,text='QUIT',command=root.destroy,relief='groove',bd=4,bg='crimson',font=('Baskerville Old Face',20))
    quit_btn.grid(row=0,column=0,ipadx=20)

    root.mainloop()

#                                                                                    NEW TOPLEVEL WINDOW FOR INSERTION OF STUDENTS MARK DETAILS                                                                                                                       

def insert_students_marks_window():
    root=Toplevel(master)
    root.title("STUDENTS EXAMINATION MARKS")
    root.configure(bg="maroon")
    root.geometry("1200x700")
    root.resizable(False,False)
 
    #Creating Frames
    top_frame=Frame(root,bd=6,bg='crimson',relief='groove')
    top_frame.place(x=10,y=10,width=1170,height=100)

    next_frame=Frame(root,bd=6,bg='crimson',relief='groove')
    next_frame.place(x=10,y=120,width=560,height=510)

    next_frame2=Frame(root,bd=6,bg='crimson',relief='groove')
    next_frame2.place(x=600,y=120,width=575,height=510)

    frame_label=Label(next_frame,text='SUBJECTIVE',font=('Times New Roman',25),bg='crimson',fg='yellow')
    frame_label.grid(row=1,column=1,ipadx=10,padx=10,pady=10)

    frame_label2=Label(next_frame2,text='PRACTICALS',font=('Times New Roman',25),bg='crimson',fg='yellow')
    frame_label2.grid(row=1,column=1,ipadx=10,padx=10,pady=10,sticky='w')

    next_frame3=Frame(root,bd=6,bg='maroon',relief='flat')
    next_frame3.place(x=860,y=630,width=310,height=70)

    next_frame4=Frame(root,bd=6,bg='maroon',relief='flat')
    next_frame4.place(x=20,y=640,width=600,height=50)


    #Creating Labels widget for Details
    admission_no_label=Label(top_frame,text="Admission Number",font=('Times New Roman',19),bg='crimson',fg='white')
    admission_no_label.grid(row=1,column=1,pady=25,padx=3,sticky=W)
    exam_no_label=Label(top_frame,text="Exam Number",font=('Times New Roman',19),bg='crimson',fg='white')
    exam_no_label.grid(row=1,column=3,pady=10,padx=5,sticky=W,ipadx=12)
    name_label=Label(top_frame,text="Student Name",font=('Times New Roman',19),bg='crimson',fg='white')
    name_label.grid(row=1,column=5,pady=10,padx=5,sticky=W,ipadx=10)
    english_marks_label=Label(next_frame,text="English",font=('Times New Roman',20),bg='crimson',fg='white')
    english_marks_label.grid(row=2,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    maths_marks_label=Label(next_frame,text="Mathematics",font=('Times New Roman',20),bg='crimson',fg='white')
    maths_marks_label.grid(row=3,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    physics_marks_label=Label(next_frame,text="Physics",font=('Times New Roman',20),bg='crimson',fg='white')
    physics_marks_label.grid(row=4,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    chemistry_marks_label=Label(next_frame,text="Chemistry",font=('Times New Roman',20),bg='crimson',fg='white')
    chemistry_marks_label.grid(row=5,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    biology_marks_label=Label(next_frame,text="Biology",font=('Times New Roman',20),bg='crimson',fg='white')
    biology_marks_label.grid(row=6,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    cs_marks_label=Label(next_frame,text="Computer Science",font=('Times New Roman',20),bg='crimson',fg='white')
    cs_marks_label.grid(row=7,column=1,pady=10,padx=10,sticky=W,ipadx=15)

    
    english_assignment_marks_label=Label(next_frame2,text="English Assignment",font=('Times New Roman',20),bg='crimson',fg='white')
    english_assignment_marks_label.grid(row=2,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    maths_record_marks_label=Label(next_frame2,text="Mathematics Record",font=('Times New Roman',20),bg='crimson',fg='white')
    maths_record_marks_label.grid(row=3,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    physics_practicals_marks_label=Label(next_frame2,text="Physics Practicals",font=('Times New Roman',20),bg='crimson',fg='white')
    physics_practicals_marks_label.grid(row=4,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    chemistry_practicals_marks_label=Label(next_frame2,text="Chemistry Practicals",font=('Times New Roman',20),bg='crimson',fg='white')
    chemistry_practicals_marks_label.grid(row=5,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    biology_record_marks_label=Label(next_frame2,text="Biology Record",font=('Times New Roman',20),bg='crimson',fg='white')
    biology_record_marks_label.grid(row=6,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    cs_practicals_marks_label=Label(next_frame2,text="Computer Science Practicals",font=('Times New Roman',20),bg='crimson',fg='white')
    cs_practicals_marks_label.grid(row=7,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    
    # Creating Label Entries
    admission_no=Entry(top_frame,width=10,font=('Times New Roman',15))
    admission_no.grid(row=1,column=2,pady=10,padx=5,ipady=5)
    exam_no=Entry(top_frame,width=10,font=('Times New Roman',15))
    exam_no.grid(row=1,column=4,pady=10,padx=5,ipady=5)
    name=Entry(top_frame,width=30,font=('Times New Roman',17))
    name.grid(row=1,column=7,pady=10,padx=3,ipady=5)

    #Creating Dropdown Box
    marks_options=[]
    for i in range (0,21):
        marks_options.append(i)
    clicked1=IntVar()
    clicked1.set(20)
    english_marks_box=OptionMenu(next_frame,clicked1, *marks_options)
    english_marks_box.grid(row=2,column=2,pady=10,sticky=W)
    clicked2=IntVar()
    clicked2.set(20)
    maths_marks_box=OptionMenu(next_frame,clicked2, *marks_options)
    maths_marks_box.grid(row=3,column=2,pady=10,sticky=W)
    clicked3=IntVar()
    clicked3.set(19)
    physics_marks_box=OptionMenu(next_frame,clicked3, *marks_options)
    physics_marks_box.grid(row=4,column=2,pady=10,sticky=W)
    clicked4=IntVar()
    clicked4.set(18)
    chemistry_marks_box=OptionMenu(next_frame,clicked4, *marks_options)
    chemistry_marks_box.grid(row=5,column=2,pady=10,sticky=W)
    clicked5=IntVar()
    clicked5.set(15)
    biology_marks_box=OptionMenu(next_frame,clicked5, *marks_options)
    biology_marks_box.grid(row=6,column=2,pady=10,sticky=W)
    clicked6=IntVar()
    clicked6.set(20)
    cs_marks_box=OptionMenu(next_frame,clicked6, *marks_options)
    cs_marks_box.grid(row=7,column=2,pady=10,sticky=W)
    clicked7=IntVar()
    clicked7.set(20)
    english_assignment_box=OptionMenu(next_frame2,clicked7, *marks_options)
    english_assignment_box.grid(row=2,column=2,pady=10,sticky=W)
    clicked8=IntVar()
    clicked8.set(20)
    maths_record_box=OptionMenu(next_frame2,clicked8, *marks_options)
    maths_record_box.grid(row=3,column=2,pady=10,sticky=W)
    clicked9=IntVar()
    clicked9.set(20)
    physics_practicals_box=OptionMenu(next_frame2,clicked9, *marks_options)
    physics_practicals_box.grid(row=4,column=2,pady=10,sticky=W)
    clicked10=IntVar()
    clicked10.set(20)
    chemistry_practicals_box=OptionMenu(next_frame2,clicked10, *marks_options)
    chemistry_practicals_box.grid(row=5,column=2,pady=10,sticky=W)
    clicked11=IntVar()
    clicked11.set(20)
    biology_record_box=OptionMenu(next_frame2,clicked11, *marks_options)
    biology_record_box.grid(row=6,column=2,pady=10,sticky=W)
    clicked12=IntVar()
    clicked12.set(20)
    cs_practicals_box=OptionMenu(next_frame2,clicked12, *marks_options)
    cs_practicals_box.grid(row=7,column=2,pady=10,sticky=W)

    def inserting_marks():
        add1=admission_no.get()
        add2=exam_no.get()
        add3=name.get()
        add4=clicked1.get()
        add5=clicked2.get()
        add6=clicked3.get()
        add7=clicked4.get()
        add8=clicked5.get()
        add9=clicked6.get()
        add10=clicked7.get()
        add11=clicked8.get()
        add12=clicked9.get()
        add13=clicked10.get()
        add14=clicked11.get()
        add15=clicked12.get()
        #INTERFACE PYTHON MYSQL
        mycon=mysqltor.connect(host='localhost',user='root',password='abi@95*13&04*15')
        cursor=mycon.cursor()
        cursor.execute('use report_card')
        cursor.execute('insert into students_marks values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10,add11,add12,add13,add14,add15))
        mycon.commit()
        mycon.close()
        insert_label=Label(next_frame4,text='Inserted Successfully Into The Table.....',font=('Times New Roman',20),bg='maroon',fg='white')
        insert_label.pack()

    submit_btn=Button(next_frame3,text='SAVE',command=inserting_marks,relief='groove',bd=4,bg='crimson',font=('Baskerville Old Face',20) )
    submit_btn.grid(row=1,column=4,padx=5,ipadx=25,sticky='e')
            
    quit_btn=Button(next_frame3,text='QUIT',command=root.destroy,relief='groove',bd=4,bg='crimson',font=('Baskerville Old Face',20) )
    quit_btn.grid(row=1,column=5,padx=5,ipadx=25,sticky='e')

    root.mainloop()
    
#                                                                                                                          UPDATING  QUERY                                                                                                                                                                                 

def update():
    mycon=mysqltor.connect(host='localhost',user='root',password='abi@95*13&04*15',db='report_card')
    cursor=mycon.cursor()
    cursor.execute('use report_card')
    add1=admission_no.get()
    add2=exam_no.get()
    add4=english_marks_box.get()
    add5=maths_marks_box.get()
    add6=physics_marks_box.get()
    add7=chemistry_marks_box.get()
    add8=biology_marks_box.get()
    add9=cs_marks_box.get()
    add10=english_assignment_box.get()
    add11=maths_record_box.get()
    add12=physics_practicals_box.get()
    add13=chemistry_practicals_box.get()
    add14=biology_record_box.get()
    add15=cs_practicals_box.get()
    cursor.execute('''UPDATE  students_marks SET Admission_Number='''+add1+''', Exam_Number= '''+add2+''' , English='''+add4+''' , Mathematics='''+add5+''', Physics='''+add6+''', Chemistry='''+add7+''',Biology='''+add8+''', Computer_Science='''+add9+''', English_Assignment='''+add10+''', Mathematics_Record='''+add11+''', Physics_Practicals='''+add12+''', Chemistry_Practicals='''+add13+''', Biology_Record='''+add14+''', ComputerScience_Practicals='''+add15+''' WHERE Admission_Number='''+admission_no.get())
    mycon.commit()    
    mycon.close()
    insert_label=Label(next_frame4,text='Updated Successfully Into The Table......',font=('Times New Roman',20),bg='maroon',fg='white')
    insert_label.pack()
    
    
def editor(a):
    edits.destroy
    root=Toplevel(master)
    root.title("STUDENTS EXAMINATION MARKS")
    root.configure(bg="maroon")
    root.geometry("1200x700")
    root.resizable(False,False)
    
    #Creating Frames
    global next_frame4
    top_frame=Frame(root,bd=6,bg='crimson',relief='groove')
    top_frame.place(x=10,y=10,width=1170,height=100)

    name_frame=Frame(root,bd=6,bg='crimson',relief='groove')
    name_frame.place(x=10,y=120,width=560,height=510)

    name_frame2=Frame(root,bd=6,bg='crimson',relief='groove')
    name_frame2.place(x=600,y=120,width=575,height=510)

    frame_label=Label(name_frame,text='SUBJECTIVE',font=('Times New Roman',25),bg='crimson',fg='yellow')
    frame_label.grid(row=1,column=1,ipadx=10,padx=10,pady=10)

    frame_label2=Label(name_frame2,text='PRACTICALS',font=('Times New Roman',25),bg='crimson',fg='yellow')
    frame_label2.grid(row=1,column=1,ipadx=10,padx=10,pady=10,sticky='w')

    next_frame3=Frame(root,bd=6,bg='maroon',relief='flat')
    next_frame3.place(x=860,y=630,width=310,height=70)

    next_frame4=Frame(root,bd=6,bg='maroon',relief='flat')
    next_frame4.place(x=20,y=640,width=600,height=50)


    #Creating Labels widget for Details
    admission_no_label=Label(top_frame,text="Admission Number",font=('Times New Roman',19),bg='crimson',fg='white')
    admission_no_label.grid(row=1,column=1,pady=25,padx=3,sticky=W)
    exam_no_label=Label(top_frame,text="Exam Number",font=('Times New Roman',19),bg='crimson',fg='white')
    exam_no_label.grid(row=1,column=3,pady=10,padx=5,sticky=W,ipadx=12)
    name_label=Label(top_frame,text="Student Name",font=('Times New Roman',19),bg='crimson',fg='white')
    name_label.grid(row=1,column=5,pady=10,padx=5,sticky=W,ipadx=10)
    english_marks_label=Label(name_frame,text="English",font=('Times New Roman',20),bg='crimson',fg='white')
    english_marks_label.grid(row=2,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    maths_marks_label=Label(name_frame,text="Mathematics",font=('Times New Roman',20),bg='crimson',fg='white')
    maths_marks_label.grid(row=3,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    physics_marks_label=Label(name_frame,text="Physics",font=('Times New Roman',20),bg='crimson',fg='white')
    physics_marks_label.grid(row=4,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    chemistry_marks_label=Label(name_frame,text="Chemistry",font=('Times New Roman',20),bg='crimson',fg='white')
    chemistry_marks_label.grid(row=5,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    biology_marks_label=Label(name_frame,text="Biology",font=('Times New Roman',20),bg='crimson',fg='white')
    biology_marks_label.grid(row=6,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    cs_marks_label=Label(name_frame,text="Computer Science",font=('Times New Roman',20),bg='crimson',fg='white')
    cs_marks_label.grid(row=7,column=1,pady=10,padx=10,sticky=W,ipadx=15)

    
    english_assignment_marks_label=Label(name_frame2,text="English Assignment",font=('Times New Roman',20),bg='crimson',fg='white')
    english_assignment_marks_label.grid(row=2,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    maths_record_marks_label=Label(name_frame2,text="Mathematics Record",font=('Times New Roman',20),bg='crimson',fg='white')
    maths_record_marks_label.grid(row=3,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    physics_practicals_marks_label=Label(name_frame2,text="Physics Practicals",font=('Times New Roman',20),bg='crimson',fg='white')
    physics_practicals_marks_label.grid(row=4,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    chemistry_practicals_marks_label=Label(name_frame2,text="Chemistry Practicals",font=('Times New Roman',20),bg='crimson',fg='white')
    chemistry_practicals_marks_label.grid(row=5,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    biology_record_marks_label=Label(name_frame2,text="Biology Record",font=('Times New Roman',20),bg='crimson',fg='white')
    biology_record_marks_label.grid(row=6,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    cs_practicals_marks_label=Label(name_frame2,text="Computer Science Practicals",font=('Times New Roman',20),bg='crimson',fg='white')
    cs_practicals_marks_label.grid(row=7,column=1,pady=10,padx=10,sticky=W,ipadx=15)
    
    # Creating Label Entries
    global admission_no
    global exam_no
    global name
    global english_marks_box
    global maths_marks_box
    global physics_marks_box
    global chemistry_marks_box
    global biology_marks_box
    global cs_marks_box
    global english_assignment_box
    global maths_record_box
    global physics_practicals_box
    global chemistry_practicals_box
    global biology_record_box
    global cs_practicals_box
    admission_no=Entry(top_frame,width=10,font=('Times New Roman',15))
    admission_no.grid(row=1,column=2,pady=10,padx=5,ipady=5)
    exam_no=Entry(top_frame,width=10,font=('Times New Roman',15))
    exam_no.grid(row=1,column=4,pady=10,padx=5,ipady=5)
    name=Entry(top_frame,width=30,font=('Times New Roman',17))
    name.grid(row=1,column=7,pady=10,padx=3,ipady=5)
    english_marks_box=Entry(name_frame,width=10,font=('Times New Roman',15))
    english_marks_box.grid(row=2,column=2,pady=10,padx=5,ipady=5)
    maths_marks_box=Entry(name_frame,width=10,font=('Times New Roman',15))
    maths_marks_box.grid(row=3,column=2,pady=10,padx=5,ipady=5)
    physics_marks_box=Entry(name_frame,width=10,font=('Times New Roman',15))
    physics_marks_box.grid(row=4,column=2,pady=10,padx=5,ipady=5)
    chemistry_marks_box=Entry(name_frame,width=10,font=('Times New Roman',15))
    chemistry_marks_box.grid(row=5,column=2,pady=10,padx=5,ipady=5)
    biology_marks_box=Entry(name_frame,width=10,font=('Times New Roman',15))
    biology_marks_box.grid(row=6,column=2,pady=10,padx=5,ipady=5)
    cs_marks_box=Entry(name_frame,width=10,font=('Times New Roman',15))
    cs_marks_box.grid(row=7,column=2,pady=10,padx=5,ipady=5)
    english_assignment_box=Entry(name_frame2,width=10,font=('Times New Roman',15))
    english_assignment_box.grid(row=2,column=2,pady=10,padx=5,ipady=5)
    maths_record_box=Entry(name_frame2,width=10,font=('Times New Roman',15))
    maths_record_box.grid(row=3,column=2,pady=10,padx=5,ipady=5)
    physics_practicals_box=Entry(name_frame2,width=10,font=('Times New Roman',15))
    physics_practicals_box.grid(row=4,column=2,pady=10,padx=5,ipady=5)
    chemistry_practicals_box=Entry(name_frame2,width=10,font=('Times New Roman',15))
    chemistry_practicals_box.grid(row=5,column=2,pady=10,padx=5,ipady=5)
    biology_record_box=Entry(name_frame2,width=10,font=('Times New Roman',15))
    biology_record_box.grid(row=6,column=2,pady=10,padx=5,ipady=5)
    cs_practicals_box=Entry(name_frame2,width=10,font=('Times New Roman',15))
    cs_practicals_box.grid(row=7,column=2,pady=10,padx=5,ipady=5)

    quit_btn=Button(next_frame3,text='QUIT',command=root.destroy,relief='groove',bd=4,bg='crimson',font=('Baskerville Old Face',20) )
    quit_btn.grid(row=1,column=5,padx=5,ipadx=25,sticky='e')
    submit_btn=Button(next_frame3,text='SAVE',command=update,relief='groove',bd=4,bg='crimson',font=('Baskerville Old Face',20) )
    submit_btn.grid(row=1,column=4,padx=5,ipadx=25,sticky='e')

    #interface python mysql
    mycon=mysqltor.connect(host='localhost',user='root',password='abi@95*13&04*15',db='report_card')
    cursor=mycon.cursor()
    cursor.execute('use report_card')
    cursor.execute('SELECT * from students_marks WHERE Admission_Number='+a)
    records=cursor.fetchall()

    for record in records:
        admission_no.insert(0,record[0])
        exam_no.insert(0,record[1])
        name.insert(0,record[2])
        english_marks_box.insert(0,record[3])
        maths_marks_box.insert(0,record[4])
        physics_marks_box.insert(0,record[5])
        chemistry_marks_box.insert(0,record[6])
        biology_marks_box.insert(0,record[7])
        cs_marks_box.insert(0,record[8])
        english_assignment_box.insert(0,record[9])
        maths_record_box.insert(0,record[10])
        physics_practicals_box.insert(0,record[11])
        chemistry_practicals_box.insert(0,record[12])
        biology_record_box.insert(0,record[13])
        cs_practicals_box.insert(0,record[14])
    mycon.commit()
    mycon.close()
    
def edit():
    global edits
    edits=Toplevel(master)
    edits.title("UPDATE WINDOW")
    edits.configure(bg="peach puff")
    edits.geometry("727x423")
    edits.resizable(False,False)
    txt='''Enter the Admission Number of the student's record that
you wish to edit or modify the marks from the table
students_marksYou can only edit the marks of the
student,admission number of the student and exam number
of the student.'''
    delete_frame=Frame(edits,bg='crimson',relief='groove',bd=5)
    delete_frame.place(x=10,y=10,width=700,height=400)

    delete_frame2=Frame(delete_frame,bg='crimson',relief='flat',bd=5)
    delete_frame2.place(x=0,y=0,width=690,height=200)
    delete_frame3=Frame(delete_frame,bg='crimson',relief='flat',bd=5)
    delete_frame3.place(x=50,y=200,width=560,height=150)

    select_id_label=Label(delete_frame3,text="Select Admission Number",font=('Times New Roman',19),bg='crimson',fg='black')
    select_id_label.grid(row=1,column=1,pady=25,padx=5,sticky=W)
    select_id_label1=Message(delete_frame2,width=900,text=txt,font=('Times New Roman',19),bg='crimson',fg='yellow')
    select_id_label1.pack(fill=X,side=LEFT)
    select_id=Entry(delete_frame3,width=20,font=('Times New Roman',15))
    select_id.grid(row=1,column=2,pady=10,padx=5,ipady=5)
    def show():
        record_id=select_id.get()
        edits.destroy
        editor(record_id)
    select_btn=Button(delete_frame3,text='OKAY',command=show,relief='groove',bd=4,bg='maroon',font=('Baskerville Old Face',20),fg='white')
    select_btn.grid(row=2,column=2,padx=5,ipadx=25,sticky='e')
    quit_btn=Button(delete_frame3,text='QUIT',command=edits.destroy,relief='groove',bd=4,bg='maroon',font=('Baskerville Old Face',20),fg='white' )
    quit_btn.grid(row=2,column=1,padx=5,ipadx=25,sticky='e')

    edits.mainloop()
    
#                                                                                                                                           DELETE QUERY                                                                                                                                                                                 
def delete():
    global editor
    editor=Toplevel(master)
    editor.title("DELETE WINDOW")
    editor.configure(bg='peach puff')
    editor.geometry("727x423")
    editor.resizable(False,False)

    txt='''Enter the Admission Number of the student record that
you wish to delete permanatly from tables
students_personal_info and students_marks from
Database report_card And press the button
'DELETE' to delete the record of the student and press the
'QUIT' button to exit.
            '''
    
    delete_frame=Frame(editor,bg='crimson',relief='groove',bd=5)
    delete_frame.place(x=10,y=10,width=700,height=400)

    delete_frame2=Frame(delete_frame,bg='crimson',relief='flat',bd=5)
    delete_frame2.place(x=0,y=0,width=690,height=200)

    select_id_label1=Message(delete_frame2,width=900,text=txt,font=('Times New Roman',18),bg='crimson',fg='yellow')
    select_id_label1.pack(fill=X,side=LEFT)

    delete_frame3=Frame(delete_frame,bg='crimson',relief='flat',bd=5)
    delete_frame3.place(x=50,y=180,width=560,height=150)

    delete_box=Entry(delete_frame3,width=20,font=('Times New Roman',15))
    delete_box.grid(row=1,column=2,pady=10,padx=5,ipady=5)

    delete_label=Label(delete_frame3,text='Selected Admission Number',font=('Times New Roman',19),bg='crimson',fg='black')
    delete_label.grid(row=1,column=1,pady=25,padx=10,sticky=W)

    def delete_query():
        #INTERFACE PYTHON MYSQL
        mycon=mysqltor.connect(host='localhost',user='root',password='abi@95*13&04*15',db='report_card')
        cursor=mycon.cursor()
        cursor.execute('use report_card')
        cursor.execute('DELETE from students_marks WHERE Admission_Number='+delete_box.get())
        cursor.execute('DELETE from students_personal_info WHERE Admission_Number='+delete_box.get())
        delete_box.delete(0,END)
        mycon.commit()
        mycon.close()
        editor.destroy
    select_btn=Button(delete_frame3,text='Delete',command=delete_query,relief='groove',bd=4,bg='maroon',font=('Baskerville Old Face',20),fg='white' )
    select_btn.grid(row=2,column=2,padx=5,ipadx=25,sticky='e')    
    quit_btn=Button(delete_frame3,text='QUIT',command=editor.destroy,relief='groove',bd=4,bg='maroon',font=('Baskerville Old Face',20),fg='white' )
    quit_btn.grid(row=2,column=1,padx=5,ipadx=25,sticky='e')

    editor.mainloop()
#                                                                                                                                              About                                                                                                                                                                                              

def about():
    root=Toplevel(master)
    root.title("HELP WINDOW")
    root.configure(bg="maroon")
    root.geometry("1360x700")
    root.resizable(False,False)
    sar=Scrollbar(root)
    sar.pack(side=RIGHT,fill=Y)

    my_text=Text(root,width=130,height=30,yscrollcommand=sar.set,bd=6,font=('Times New Roman',18),relief='groove',fg='yellow',bg='crimson')
    my_text.pack(pady=10,padx=10,fill=BOTH,expand=1)
    sar.configure(command=my_text.yview)

    def open_txt():
        text_file=open('about.txt','r')
        stuff=text_file.read()

        my_text.insert(END,stuff)
        text_file.close()

    open_txt()
    root.mainloop()

#                                                                                                                                             Student Display                                                                                                                                                                             

def display(a):
    root=Toplevel(master)
    root.title("REPORT CARD OF STUDENT ")
    root.configure(bg="peach puff")
    root.geometry("1370x700")
    root.resizable(False,False)

    mycon=mysqltor.connect(host='localhost',user='root',password='abi@95*13&04*15',database='report_card')
    cursor=mycon.cursor()
    cursor.execute('select* from students_marks where Admission_Number=' +a )
    marks=cursor.fetchall()
    cursor.execute('select*from students_personal_info where Admission_Number='+a)
    info=cursor.fetchall()
    
    for i in marks:
        a=2+2
     
    for j in info:
        a=1+2

    bb=j[4]
    dd=str(bb)
    bd=dd[8:10]+dd[4:8]+dd[0:4]
    dob=bd

    def checking(mark):
         if mark==8 or mark<8:
            pos='FAIL'
            return pos
         else:
            pos='PASS'
            return pos
 
    title_frame_display=Frame(root,bd=6,relief='groove',bg='crimson')
    title_frame_display.place(x=10,y=10,width=1350,height=680)

    title=Label(title_frame_display,text=j[8],bg='crimson',fg='yellow',font=('Times New Roman',25))
    title.pack(anchor='center',fill=X)

    title_frame_display2=Frame(root,bd=6,relief='flat',bg='crimson')
    title_frame_display2.place(x=25,y=55,width=680,height=610)

    title_frame_display3=Frame(root,bd=6,relief='flat',bg='crimson')
    title_frame_display3.place(x=710,y=55,width=630,height=610)

    marks_frame=Frame(title_frame_display2,bg='white',bd=2,relief='flat')
    marks_frame.place(x=4,y=250,width=182,height=350)

    marks_frame1=Frame(title_frame_display2,bg='white',bd=2,relief='flat')
    marks_frame1.place(x=186,y=250,width=152,height=350)

    marks_frame2=Frame(title_frame_display2,bg='white',bd=2,relief='flat')
    marks_frame2.place(x=338,y=250,width=168,height=350)

    marks_frame3=Frame(title_frame_display2,bg='white',bd=2,relief='flat')
    marks_frame3.place(x=506,y=250,width=166,height=350)

    marks_label=Label(marks_frame,text='SUBJECT',font=('Times New Roman',20),bg='indian red1',fg='black')
    marks_label.pack(fill=X,ipady=15)
    marks_label2=Label(marks_frame,text='ENGLISH',bg='white',font=('Times New Roman',15))
    marks_label2.pack(fill=X,ipady=10)
    marks_label3=Label(marks_frame,text='MATHEMATICS',bg='salmon1',font=('Times New Roman',15))
    marks_label3.pack(fill=X,ipady=10)
    marks_label4=Label(marks_frame,text='PHYSICS',bg='white',font=('Times New Roman',15))
    marks_label4.pack(fill=X,ipady=10)
    marks_label5=Label(marks_frame,text='CHEMISTRY',bg='salmon1',font=('Times New Roman',15))
    marks_label5.pack(fill=X,ipady=10)
    marks_label6=Label(marks_frame,text='BIOLOGY',bg='white',font=('Times New Roman',15))
    marks_label6.pack(fill=X,ipady=10)
    marks_label7=Label(marks_frame,text='CS',bg='salmon1',font=('Times New Roman',15))
    marks_label7.pack(fill=X,ipady=10)

    marks_label=Label(marks_frame1,text='EXAM',font=('Times New Roman',20),bg='indian red1',fg='black')
    marks_label.pack(fill=X,ipady=15)
    marks_label2=Label(marks_frame1,text=i[3],bg='white',font=('Times New Roman',15))
    marks_label2.pack(fill=X,ipady=10)
    marks_label3=Label(marks_frame1,text=i[4],bg='salmon1',font=('Times New Roman',15))
    marks_label3.pack(fill=X,ipady=10)
    marks_label4=Label(marks_frame1,text=i[5],bg='white',font=('Times New Roman',15))
    marks_label4.pack(fill=X,ipady=10)
    marks_label5=Label(marks_frame1,text=i[6],bg='salmon1',font=('Times New Roman',15))
    marks_label5.pack(fill=X,ipady=10)
    marks_label6=Label(marks_frame1,text=i[7],bg='white',font=('Times New Roman',15))
    marks_label6.pack(fill=X,ipady=10)
    marks_label7=Label(marks_frame1,text=i[8],bg='salmon1',font=('Times New Roman',15))
    marks_label7.pack(fill=X,ipady=10)

    marks_label=Label(marks_frame2,text='PRACTICALS',font=('Times New Roman',20),bg='indian red1',fg='black')
    marks_label.pack(fill=X,ipady=15)
    marks_label2=Label(marks_frame2,text=i[9],bg='white',font=('Times New Roman',15))
    marks_label2.pack(fill=X,ipady=10)
    marks_label3=Label(marks_frame2,text=i[10],bg='salmon1',font=('Times New Roman',15))
    marks_label3.pack(fill=X,ipady=10)
    marks_label4=Label(marks_frame2,text=i[11],bg='white',font=('Times New Roman',15))
    marks_label4.pack(fill=X,ipady=10)
    marks_label5=Label(marks_frame2,text=i[12],bg='salmon1',font=('Times New Roman',15))
    marks_label5.pack(fill=X,ipady=10)
    marks_label6=Label(marks_frame2,text=i[13],bg='white',font=('Times New Roman',15))
    marks_label6.pack(fill=X,ipady=10)
    marks_label7=Label(marks_frame2,text=i[14],bg='salmon1',font=('Times New Roman',15))
    marks_label7.pack(fill=X,ipady=10)

    marks_label=Label(marks_frame3,text='PASS/FAIL',font=('Times New Roman',20),bg='indian red1',fg='black')
    marks_label.pack(fill=X,ipady=15)
    marks_label2=Label(marks_frame3,text=checking(i[3]),bg='white',font=('Times New Roman',15))
    marks_label2.pack(fill=X,ipady=10)
    marks_label3=Label(marks_frame3,text=checking(i[4]),bg='salmon1',font=('Times New Roman',15))
    marks_label3.pack(fill=X,ipady=10)
    marks_label4=Label(marks_frame3,text=checking(i[5]),bg='white',font=('Times New Roman',15))
    marks_label4.pack(fill=X,ipady=10)
    marks_label5=Label(marks_frame3,text=checking(i[6]),bg='salmon1',font=('Times New Roman',15))
    marks_label5.pack(fill=X,ipady=10)
    marks_label6=Label(marks_frame3,text=checking(i[7]),bg='white',font=('Times New Roman',15))
    marks_label6.pack(fill=X,ipady=10)
    marks_label7=Label(marks_frame3,text=checking(i[8]),bg='salmon1',font=('Times New Roman',15))
    marks_label7.pack(fill=X,ipady=10)



    name_label=Label(title_frame_display2,text="Student Name",font=('Times New Roman',22),bg='crimson',fg='white')
    name_label.grid(row=1,column=1,pady=5,padx=10,sticky=W,columnspan=4)
    grade_label=Label(title_frame_display2,text="Class",font=('Times New Roman',22),bg='crimson',fg='white')
    grade_label.grid(row=2,column=1,pady=5,padx=10,sticky=W)
    exam_no_label=Label(title_frame_display2,text="Exam Number",font=('Times New Roman',22),bg='crimson',fg='white')
    exam_no_label.grid(row=3,column=1,pady=5,padx=10,sticky=W)
    dob_label=Label(title_frame_display2,text="Date of Birth",font=('Times New Roman',22),bg='crimson',fg='white')
    dob_label.grid(row=4,column=1,pady=5,padx=10,sticky=W)
    admission_no_label=Label(title_frame_display2,text="Admission Number",font=('Times New Roman',22),bg='crimson',fg='white')
    admission_no_label.grid(row=5,column=1,pady=5,padx=10,sticky=W)

    name_label2=Label(title_frame_display2,text=':'+j[1],font=('Times New Roman',22),bg='crimson',fg='white')
    name_label2.grid(row=1,column=2,pady=5,padx=10,sticky=W,columnspan=4)
    grade_label2=Label(title_frame_display2,text=':'+str(j[3]),font=('Times New Roman',22),bg='crimson',fg='white')
    grade_label2.grid(row=2,column=2,pady=5,padx=10,sticky=W)
    exam_no_label2=Label(title_frame_display2,text=':'+str(j[2]),font=('Times New Roman',22),bg='crimson',fg='white')
    exam_no_label2.grid(row=3,column=2,pady=5,padx=10,sticky=W)
    dob_label2=Label(title_frame_display2,text=':'+str(dob),font=('Times New Roman',22),bg='crimson',fg='white')
    dob_label2.grid(row=4,column=2,pady=5,padx=10,sticky=W)
    admission_no_label2=Label(title_frame_display2,text=':'+str(j[0]),font=('Times New Roman',22),bg='crimson',fg='white')
    admission_no_label2.grid(row=5,column=2,pady=5,padx=10,sticky=W)


    gender_label=Label(title_frame_display3,text="Gender",font=('Times New Roman',22),bg='crimson',fg='white')
    gender_label.grid(row=1,column=1,pady=10,padx=10,sticky=W)
    father_name_label=Label(title_frame_display3,text="Father Name",font=('Times New Roman',22),bg='crimson',fg='white')
    father_name_label.grid(row=2,column=1,pady=10,padx=10,sticky=W)
    mother_name_label=Label(title_frame_display3,text="Mother Name",font=('Times New Roman',22),bg='crimson',fg='white')
    mother_name_label.grid(row=3,column=1,pady=10,padx=10,sticky=W)
    exam_board_label=Label(title_frame_display3,text="Examination Board",font=('Times New Roman',22),bg='crimson',fg='white')
    exam_board_label.grid(row=4,column=1,pady=10,padx=10,sticky=W)
    language_medium_label=Label(title_frame_display3,text="Language of Medium",font=('Times New Roman',22),bg='crimson',fg='white')
    language_medium_label.grid(row=5,column=1,pady=10,padx=10,sticky=W)
    state_label=Label(title_frame_display3,text="State",font=('Times New Roman',22),bg='crimson',fg='white')
    state_label.grid(row=6,column=1,pady=10,padx=10,sticky=W)
    phone_label=Label(title_frame_display3,text="Phone Number",font=('Times New Roman',22),bg='crimson',fg='white')
    phone_label.grid(row=7,column=1,pady=10,padx=10,sticky=W)
    email_id_label=Label(title_frame_display3,text="Email ID",font=('Times New Roman',22),bg='crimson',fg='white')
    email_id_label.grid(row=8,column=1,pady=10,padx=10,sticky=W)

    gender_label2=Label(title_frame_display3,text=':'+j[5],font=('Times New Roman',22),bg='crimson',fg='white')
    gender_label2.grid(row=1,column=2,pady=10,padx=10,sticky=W)
    father_name_label2=Label(title_frame_display3,text=':'+j[6],font=('Times New Roman',22),bg='crimson',fg='white')
    father_name_label2.grid(row=2,column=2,pady=10,padx=10,sticky=W)
    mother_name_label2=Label(title_frame_display3,text=':'+j[7],font=('Times New Roman',22),bg='crimson',fg='white')
    mother_name_label2.grid(row=3,column=2,pady=10,padx=10,sticky=W)
    exam_board_label2=Label(title_frame_display3,text=':'+j[9],font=('Times New Roman',22),bg='crimson',fg='white')
    exam_board_label2.grid(row=4,column=2,pady=10,padx=10,sticky=W)
    language_medium_label2=Label(title_frame_display3,text=':'+j[10],font=('Times New Roman',22),bg='crimson',fg='white')
    language_medium_label2.grid(row=5,column=2,pady=10,padx=10,sticky=W)
    state_label2=Label(title_frame_display3,text=':'+j[11],font=('Times New Roman',22),bg='crimson',fg='white')
    state_label2.grid(row=6,column=2,pady=10,padx=10,sticky=W)
    phone_label2=Label(title_frame_display3,text=':'+j[12],font=('Times New Roman',22),bg='crimson',fg='white')
    phone_label2.grid(row=7,column=2,pady=10,padx=10,sticky=W)
    email_id_label2=Label(title_frame_display3,text=':'+j[13],font=('Times New Roman',22),bg='crimson',fg='white')
    email_id_label2.grid(row=8,column=2,pady=10,padx=10,sticky=W)

    
    mycon.commit()
    mycon.cursor()
    root.mainloop()
    
def students():
    global edits
    edits=Toplevel(master)
    edits.title("DISPLAY  WINDOW")
    edits.configure(bg="peach puff")
    edits.geometry("727x423")
    edits.resizable(False,False)
    txt='''Enter the Admission Number of the student's record
that you wish to view in the from of a REPORT CARD format
where you can see the marks of the students and all details
of students in detailed view.'''
    delete_frame=Frame(edits,bg='crimson',relief='groove',bd=5)
    delete_frame.place(x=10,y=10,width=700,height=400)
    delete_frame2=Frame(delete_frame,bg='crimson',relief='flat',bd=5)
    delete_frame2.place(x=0,y=0,width=690,height=200)
    delete_frame3=Frame(delete_frame,bg='crimson',relief='flat',bd=5)
    delete_frame3.place(x=50,y=180,width=560,height=150)
    select_id_label=Label(delete_frame3,text="Select Admission Number",font=('Times New Roman',19),bg='crimson',fg='black')
    select_id_label.grid(row=1,column=1,pady=25,padx=5,sticky=W)
    select_id_label1=Message(delete_frame2,width=900,text=txt,font=('Times New Roman',19),bg='crimson',fg='yellow')
    select_id_label1.pack(fill=X,side=LEFT)
    select_id=Entry(delete_frame3,width=20,font=('Times New Roman',15))
    select_id.grid(row=1,column=2,pady=10,padx=5,ipady=5)
    def show():
        record_id=select_id.get()
        display(record_id)
    select_btn=Button(delete_frame3,text='OKAY',command=show,relief='groove',bd=4,bg='maroon',font=('Baskerville Old Face',20),fg='white')
    select_btn.grid(row=2,column=2,padx=5,ipadx=25,sticky='e')
    quit_btn=Button(delete_frame3,text='QUIT',command=edits.destroy,relief='groove',bd=4,bg='maroon',font=('Baskerville Old Face',20),fg='white' )
    quit_btn.grid(row=2,column=1,padx=5,ipadx=25,sticky='e')

    edits.mainloop()

#                                                                                                                                             Class Display                                                                                                                                                                           

def class_display():
    root=Toplevel(master)
    root.title("MARKS OF ALL STUDENTS OF A CLASS")
    root.configure(bg="peach puff")
    root.geometry("1370x700")
    root.resizable(False,False)

    title_frame_display=Frame(root,bd=6,relief='ridge',bg='maroon')
    title_frame_display.place(x=10,y=10,width=1350,height=680)

    title=Label(title_frame_display,text='CLASS MARKS',bg='maroon',fg='white',font=('Times New Roman',40))
    title.pack(anchor='center')

    record_display=Frame(root,relief='flat',bg='crimson')
    record_display.place(x=290,y=100,width=800,height=500)


    # Interface PYTHON MYSQL
    mycon=mysqltor.connect(host='localhost',user='root',password='abi@95*13&04*15',database='report_card')
    cursor=mycon.cursor()

    style=ttk.Style()

    style.theme_use('clam')

    style.configure('Treeview',background='peach puff',foreground='maroon',rowheight=25,fieldbackground='navajo white')
    style.configure("Treeview.heading",foreground='red',font=('Helvetica',11,'bold'))
    style.map('Treeview',background=[('selected','green')])

    my_tree=ttk.Treeview(record_display,height=30)
    my_tree.pack(side=RIGHT,fill=BOTH)
    my_tree.place(x=0,y=0)

    yscrollbar=ttk.Scrollbar(record_display,orient='vertical',command=my_tree.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)

    xscrollbar=ttk.Scrollbar(record_display,orient='horizontal',command=my_tree.xview)
    xscrollbar.pack(side=BOTTOM,fill=X)

    my_tree.configure(yscrollcommand=yscrollbar.set)
    my_tree.configure(xscrollcommand=xscrollbar.set)
    my_tree.tag_configure('oddrow',background='white')
    my_tree.tag_configure('evenrow',background='light blue')

    cursor.execute('select* from students_marks')
    conn=cursor.fetchall()

    my_tree['columns']=('admission_no','exam_no','name','english_marks_box','maths_marks_box','physics_marks_box','chemistry_marks_box','biology_marks_box','cs_marks_box','english_assignment_box','maths_record_box','physics_practicals_box','chemistry_practicals_box','biology_record_box' ,'cs_practicals_box')
    my_tree.column('#0',width=0,stretch=NO)
    my_tree.column('admission_no',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('exam_no',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('name',width=100,minwidth=100,anchor=CENTER)
    my_tree.column('english_marks_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('maths_marks_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('physics_marks_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('chemistry_marks_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('biology_marks_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('cs_marks_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('english_assignment_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('maths_record_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('physics_practicals_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('chemistry_practicals_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('biology_record_box',width=50,minwidth=70,anchor=CENTER)
    my_tree.column('cs_practicals_box',width=50,minwidth=70,anchor=CENTER)

    my_tree.heading('#0',text='',anchor=W)
    my_tree.heading('admission_no',text='Admission Number',anchor=CENTER)
    my_tree.heading('exam_no',text='Exam Number',anchor=CENTER)
    my_tree.heading('name',text='Name',anchor=CENTER)
    my_tree.heading('english_marks_box',text='English Marks',anchor=CENTER)
    my_tree.heading('maths_marks_box',text='Mathematics Marks',anchor=CENTER)
    my_tree.heading('physics_marks_box',text='Physics Marks',anchor=CENTER)
    my_tree.heading('chemistry_marks_box',text='Chemistry Marks',anchor=CENTER)
    my_tree.heading('biology_marks_box',text='Biology Marks',anchor=CENTER)
    my_tree.heading('cs_marks_box',text='CS Marks',anchor=CENTER)
    my_tree.heading('english_assignment_box',text='English Assignment',anchor=CENTER)
    my_tree.heading('maths_record_box',text='Mathematics Record',anchor=CENTER)
    my_tree.heading('physics_practicals_box',text='Physics Practicals',anchor=CENTER)
    my_tree.heading('chemistry_practicals_box',text='Chemistry Practicals',anchor=CENTER)
    my_tree.heading('biology_record_box',text='Biology Record',anchor=CENTER)
    my_tree.heading('cs_practicals_box',text='CS Practicals',anchor=CENTER)

    my_tree.tag_configure('oddrow',background='white')
    my_tree.tag_configure('evenrow',background='light blue')

    count=0
    for i in conn:
        if count%2==0:
            my_tree.insert('',count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14]),tags=('evenrow',))
        else:
             my_tree.insert('',count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14]),tags=('oddrow',))
            
        count+=1

    next_frame3=Frame(root,bd=6,bg='maroon',relief='flat')
    next_frame3.place(x=1170,y=610,width=170,height=70)

    quit_btn=Button(next_frame3,text='QUIT',command=root.destroy,relief='groove',bd=4,bg='crimson',font=('Baskerville Old Face',20) )
    quit_btn.grid(row=1,column=5,padx=5,ipadx=25,sticky='e')

    mycon.commit()
    mycon.close()
    root.mainloop()
#                                                                                                                                       Theme                                                                                                                                                                                                 

def theme():
    root=Toplevel(master)
    root.title("THEME OF THE PROJECT")
    root.configure(bg="maroon")
    root.geometry("1360x700")
    root.resizable(False,False)
    sar=Scrollbar(root)
    sar.pack(side=RIGHT,fill=Y)

    my_text=Text(root,width=130,height=30,yscrollcommand=sar.set,bd=6,font=('Baskerville Old Face',20),relief='groove',fg='yellow',bg='crimson')
    my_text.pack(pady=10,padx=10,fill=BOTH,expand=1)
    sar.configure(command=my_text.yview)

    def open_txt():
        text_file=open('theme.txt','r')
        stuff=text_file.read()

        my_text.insert(END,stuff)
        text_file.close()

    open_txt()
    root.mainloop()



#                                                                                                                                             Home Window                                                                                                                                                                                         

#Creating Home Window Frames and Labels
title_frame=Frame(master,bd=6,relief='ridge',bg='peach puff')
title_frame.place(x=5,y=5,width=1360,height=690)

title=Label(title_frame,text='REPORT CARD',bg='peach puff',font=('Times New Roman',40))
title.pack(anchor='center')

btn_frame=Frame(title_frame,bd=8,relief='groove',bg='crimson')
btn_frame.place(x=90,y=100,width=1190,height=440)

display_single_student_btn=Button(btn_frame,text='Display student records',command=students,font=('Times New Roman',22),bg='navajo white',relief='raised',bd=6)
display_single_student_btn.grid(row=1,column=1,pady=10,padx=30,ipady=11,ipadx=9)

update_btn=Button(btn_frame,text='Update students  record',command=edit,font=('Times New Roman',22),bg='navajo white',relief='raised',bd=6)
update_btn.grid(row=1,column=2,pady=30,padx=30,ipady=11,ipadx=5)

delete_btn=Button(btn_frame,text='Delete students  records',command=delete,font=('Times New Roman',22),bg='navajo white',relief='raised',bd=6)
delete_btn.grid(row=2,column=1,pady=30,padx=10,ipady=10,ipadx=5)

display_class_btn=Button(btn_frame,text='Display class  records',command=class_display,font=('Times New Roman',22),bg='navajo white',relief='raised',bd=6)
display_class_btn.grid(row=2,column=2,pady=30,padx=30,ipadx=19,ipady=10)
    
insert_info_btn=Button(btn_frame,text='Insert Details',command=insert_students_personal_info_window,font=('Times New Roman',22),bg='navajo white',relief='raised',bd=6)
insert_info_btn.grid(row=1,column=3,pady=30,padx=30,ipadx=70,ipady=9,sticky='W')

insert_marks_btn=Button(btn_frame,text='Insert Marks',command=insert_students_marks_window,font=('Times New Roman',22),bg='navajo white',relief='raised',bd=6)
insert_marks_btn.grid(row=2,column=3,pady=30,padx=30,ipadx=74,ipady=9,sticky='W')

display_single_student_btn=Button(btn_frame,text='      Create Database      ',command=create_db,font=('Times New Roman',22),bg='navajo white',relief='raised',bd=6)
display_single_student_btn.grid(row=3,column=1,pady=30,padx=30,ipadx=10,ipady=10)

display_single_student_btn=Button(btn_frame,text='           THEME            ',command=theme,font=('Times New Roman',22),bg='navajo white',relief='raised',bd=6)
display_single_student_btn.grid(row=3,column=2,pady=30,padx=30,ipadx=10,ipady=10)

display_single_student_btn=Button(btn_frame,text='             HELP               ',command=about,font=('Times New Roman',22),bg='navajo white',relief='raised',bd=6)
display_single_student_btn.grid(row=3,column=3,pady=30,padx=30,ipady=9)

quit_btn=Button(title_frame,text='QUIT',bg='crimson',font=('Baskerville Old Face',20),relief='groove',bd=4,width=10,command=master.destroy)
quit_btn.pack(side=BOTTOM,anchor='e',ipadx=10,padx=10)
                
master.mainloop()
