from tkinter.ttk import *
from tkinter import *
import os

file_names = ["inouttime.txt", "leave_applications.txt", "room_info_boys.txt", "room_info_girls.txt", "student_info.txt", "room_info_others.txt", "visitor_info.txt"]

for file_name in file_names:
    if not os.path.exists(file_name):
        try:
            with open(file_name, "x") as fp:
                pass  # File created successfully
        except FileExistsError:
            print(f"File {file_name} already exists.")
    else:
        print(f"File {file_name} already exists.")



def date():
    from datetime import datetime
    # current date time
    now = datetime.now()
    t = now.strftime("%H:%M")
    s1 = now.strftime("%H:%M,%Y-%m-%d")
    s1 = str(s1)
    return s1 #returns Current Date And Time In String

base = Tk()
base.title("HOSTEL MANAGEMENT SYSTEM")
base.geometry(f'{1535}x{790}+{0}+{0}')
heading = Label(base, text="HOSTEL MANAGEMENT SYSTEM", font=("Arial 30 bold"), bg="lightseagreen", fg="white", padx=490, pady=20)
heading.pack()

canvas = Canvas(base, bg='silver', height=575, width=800)
canvas.place(x=330, y=130)

G = 1
def main():
    global G
    canvas = Canvas(base, bg='lightseagreen', height=675, width=310)
    canvas.place(x=-1, y=100)
    can = Canvas(base, bg='silver', height=675, width=1500)
    can.place(x=320, y=105)

    def add_stud():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)
        first_name = Label(base, text="First Name", font=("Arial 15 bold"), bg='silver', fg="black")
        first_name.place(x=400, y=150)
        fir_name_entry = Entry(base, width=15, font=("Arial 15"))
        fir_name_entry.place(x=400, y=180)
        fir_name_entry.focus()

        last_name = Label(base, text="Last Name", font=("Arial 15 bold"), bg="silver", fg="black")
        last_name.place(x=610, y=150)
        last_name_entry = Entry(base, width=15, font=("Arial 15"))
        last_name_entry.place(x=610, y=180)

        father_name = Label(base, text="Father Name", font=("Arial 15 bold"), bg="silver", fg="black")
        father_name.place(x=400, y=220)
        fathr_name_entry = Entry(base, width=15, font=("Arial 15"))
        fathr_name_entry.place(x=400, y=250)

        mother_name = Label(base, text="Mother Name", font=("Arial 15 bold"), bg="silver", fg="black")
        mother_name.place(x=610, y=220)
        mther_name_entry = Entry(base, width=15, font=("Arial 15"))
        mther_name_entry.place(x=610, y=250)

        dob = Label(base, text="DOB", font=("Arial 15 bold"), bg="silver", fg="black")
        dob.place(x=400, y=300)
        dob_entry = Entry(base, width=15, font=("Arial 15 bold"))
        dob_entry.place(x=400, y=330)
        m1 = Label(base, text="(Y-M-D)", font=("Arial 12 bold"), bg="silver", fg="black")
        m1.place(x=450, y=300)

        contact = Label(base, text="Contact", font=("Arial 15 bold"), bg="silver", fg="black")
        contact.place(x=610, y=300)
        cont_entry = Entry(base, width=15, font=("Arial 15 bold"))
        cont_entry.place(x=610, y=330)

        message = Label(base, text="(Contact No. will be your Hostel ID)", font=("Arial 10 bold"), bg="silver",
                        fg="black")
        message.place(x=690, y=300)

        email = Label(base, text="Email", font=("Arial 15 bold"), bg="silver", fg="black")
        email.place(x=400, y=370)
        email_entry = Entry(base, width=15, font=("Arial 15 bold"))
        email_entry.place(x=400, y=410)

        address = Label(base, text="Address", font=("Arial 15 bold"), bg="silver", fg="black")
        address.place(x=610, y=370)
        addrs_entry = Entry(base, width=15, font=("Arial 15 bold"))
        addrs_entry.place(x=610, y=410)


        vehicle = Label(base, text="Vehicle No.", font=("Arial 15 bold"), bg="silver", fg="black")
        vehicle.place(x=400, y=450)
        vehicle_entry = Entry(base, width="15", font=("Arial 15 bold"))
        vehicle_entry.place(x=400, y=490)
        m2 = Label(base, text="(MH20EU9295)", font=("Arial 11 bold"), bg="silver", fg="black")
        m2.place(x=470, y=450)

        work_place = Label(base, text="Work Place/College", font=("Arial 15 bold"), bg="silver", fg="black")
        work_place.place(x=610, y=450)
        place_entry = Entry(base, width="15", font=("Arial 15 bold"))
        place_entry.place(x=610, y=490)


        gender = Label(base, text="Gender", font=("Arial 15 bold"), bg="silver", fg="black")
        gender.place(x=400, y=580)
        G = 1
        def selected():
            global G
            if c1.get() == 1:
                G = 1
            elif c1.get() == 2:
                G = 2
            elif c1.get() == 0:
                G = 0
            else:
                G = 1
        c1 = IntVar()
        a = Radiobutton(base, text="Male", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=1,
                        command=selected)
        b = Radiobutton(base, text="Female", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=2,
                        command=selected)
        c = Radiobutton(base, text="Other", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=0,
                        command=selected)
        a.place(x=490, y=580)
        b.place(x=580, y=580)
        c.place(x=680, y=580)
        def available_roome():
            rooms_availble = Label(base, text="Rooms Available", font=("Arial 20 bold"), bg="lightseagreen",
                                   fg="white", padx=140)
            rooms_availble.place(x=1005, y=110)
            x = "    Room No.                       |                                 Beds"
            room = Label(base, text=x, font=("Arial 15 bold"), bg="dark slate grey", fg="white")
            room.place(x=1005, y=150)
            global G
            bed1 = None
            bed2 = None
            bed3 = None
            if G == 1:
                f1 = open("room_info_boys.txt","r")
                bed1 = "B1"
                bed2 = "B2"
                bed3 = "B3"
            elif G==2:
                f1 = open("room_info_girls.txt","r")
                bed1 = "G1"
                bed2 = "G2"
                bed3 = "G3"
            elif G==0:
                f1 = open("room_info_others.txt","r")
                bed1 = "O1"
                bed2 = "O2"
                bed3 = "O3"
            else:
                file_name = "room_info_boys.txt"
                bed1 = "B1"
                bed2 = "B2"
                bed3 = "B3"
            all_lines = f1.readlines()
            count = 1
            rooms = []
            for i in all_lines:
                temp1 = str(i)
                one_line = temp1.split(',')
                if one_line[1] == bed1 and one_line[2] == bed2 and one_line[3] == bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append(bed1)
                    temp.append(bed2)
                    temp.append(bed3)
                    rooms.append(temp)
                if one_line[1] != bed1 and one_line[2] == bed2 and one_line[3] == bed3:
                    count = 2
                    temp = []
                    temp.append(one_line[0])
                    temp.append("NA")
                    temp.append(bed2)
                    temp.append(bed3)
                    rooms.append(temp)
                if one_line[1] == bed1 and one_line[2] != bed2 and one_line[3] == bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append(bed1)
                    temp.append("NA")
                    temp.append(bed3)
                    rooms.append(temp)
                if one_line[1] == bed1 and one_line[2] == bed2 and one_line[3] != bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append(bed1)
                    temp.append(bed2)
                    temp.append("NA")
                    rooms.append(temp)
                if one_line[1] == bed1 and one_line[2] != bed2 and one_line[3] != bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append(bed1)
                    temp.append("NA")
                    temp.append("NA")
                    rooms.append(temp)

                if one_line[1] != bed1 and one_line[2] == bed2 and one_line[3] != bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append("NA")
                    temp.append(bed2)
                    temp.append("NA")
                    rooms.append(temp)
                if one_line[1] != bed1 and one_line[2] != bed2 and one_line[3] == bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append("NA")
                    temp.append("NA")
                    temp.append(bed3)
                    rooms.append(temp)
                if one_line[1] != bed1 and one_line[2] != bed2 and one_line[3] != bed3:
                    temp = []
                    count = 2
                    temp.append("--")
                    temp.append("NA")
                    temp.append("NA")
                    temp.append("NA")
                    rooms.append(temp)
            if count == 1:
                y = "No Rooms Available"
                x = Label(base, text=y, font=("Arial", 40), bg="dark slate grey", fg="white")
                x.place(x=1020, y=300)
            else:
                x1co = 1150
                y1co = 200
                x2co = 1350
                y2co = 200
                flag = 1
                for i in rooms:
                    r_no = Label(base, text=i[0], font=("Arial", 15), bg="silver", fg="black")
                    r_no.place(x=x1co, y=y1co)
                    y = i[1] + "   " + i[2] + "   " + i[3]
                    r_bk_no = Label(base, text=y, font=("Arial", 15), bg="silver", fg="black")
                    r_bk_no.place(x=x2co, y=y2co)
                    y1co = y1co + 40
                    y2co = y2co + 40
                    count = 2
                    if flag >= 8:
                        break
                    flag = flag + 1
            f1.close()

            c1 = Canvas(base, height=2, width=600)
            c1.place(x=1000, y=550)
            r1 = Label(base, text="Room No.", font=("Arial 15 bold"), bg="silver", fg="black")
            r1.place(x=1040, y=570)
            r2 = Entry(base, width=15, font=("Arial 15 bold"))
            r2.place(x=1150, y=570)
            r3 = Label(base, text="Bed No.", font=("Arial 15 bold"), bg="silver", fg="black")
            r3.place(x=1040, y=610)
            r4 = Entry(base, width=15, font=("Arial 15 bold"))
            r4.place(x=1150, y=610)
            r5 = Label(base, text="(B1 B2 B3)", font=("Arial 10 bold"), bg="silver", fg="black")
            r5.place(x=1040, y=640)
            r6 = Label(base, text="( Girl = G1 )", font=("Arial 15 bold"), bg="silver", fg="black")
            r6.place(x=1350,y=570)
            r7 = Label(base, text="( Other = O1)",font=("Arial 15 bold"), bg="silver", fg="black")
            r7.place(x=1350,y=610)
            def student():
                global G
                bed1 = None
                bed2 = None
                bed3 = None
                file_name = None
                if G == 1:
                    file_name = "room_info_boys.txt"
                    bed1 = "B1"
                    bed2 = "B2"
                    bed3 = "B3"
                elif G == 2:
                    file_name = "room_info_girls.txt"
                    bed1 = "G1"
                    bed2 = "G2"
                    bed3 = "G3"
                elif G == 0:
                    file_name = "room_info_others.txt"
                    bed1 = "O1"
                    bed2 = "O2"
                    bed3 = "O3"
                else:
                    file_name = "room_info_boys.txt"
                    bed1 = "B1"
                    bed2 = "B2"
                    bed3 = "B3"
                f1 = open("student_info.txt", "a")
                f2 = open(file_name,"a")
                n = str(fir_name_entry.get()) + " "
                b = str(r4.get()).upper()
                ln = str(last_name_entry.get()).lower()
                f = str(fathr_name_entry.get()).lower()
                m = str(mther_name_entry.get()).lower()
                d = str(dob_entry.get()).lower()
                add = str(addrs_entry.get()).lower()
                c = str(cont_entry.get()).lower()
                e = str(email_entry.get())
                w = str(place_entry.get()).lower()
                v = str(vehicle_entry.get()).lower()
                da = date().lower()
                rom = str(r2.get()).lower()
                f1.write(
                    c + "," + n + ln + "," + f + "," + m + "," + d + "," + e + "," + w + "," + v + "," + da + "," + b + "," + rom + "," + "\n")
                f1.close()  
                fobj = open(file_name, "r")
                fdata_ls = fobj.readlines()
                fobj.close()
                rdate = date()
                fobj = open(file_name, "w")
                if b == bed1:
                    for oneline in fdata_ls:
                        if oneline.startswith(rom + ",") and oneline.__contains__(","+bed1):
                            # write date
                            new_oneline = oneline.replace(","+bed1+",", "," + c + ",")
                            new_oneline2 = new_oneline.replace(",NOT,", "," + rdate + ",")
                            fobj.write(new_oneline)
                        else:
                            fobj.write(oneline)
                else:
                    if b == bed2:
                        for oneline in fdata_ls:
                            if oneline.startswith(rom + ",") and oneline.__contains__(","+bed2):
                                # write date
                                new_oneline = oneline.replace(","+bed2+"," , "," + c + ",")
                                new_oneline2 = new_oneline.replace(",NOT," , "," + rdate + ",")
                                fobj.write(new_oneline)
                            else:
                                fobj.write(oneline)
                    else:
                        for oneline in fdata_ls:
                            if oneline.startswith(rom + ",") and oneline.__contains__(","+bed3):
                                # write date
                                new_oneline = oneline.replace(","+bed3+"," , "," + c + ",")
                                new_oneline2 = new_oneline.replace(",NOT," , "," + rdate + ",")
                                fobj.write(new_oneline)
                            else:
                                fobj.write(oneline)
                fobj.close()

                l = Label(base, text="Student Added Successfully....!", font=("Arial 15 bold"), bg='silver',
                          fg="black")
                l.place(x=1150, y=650)
            add_student = Button(base, text="Add Student", font=("Arial 20 bold"), bg="white", fg="black" ,command=student)
            add_student.place(x=1040, y=700)

        c1 = IntVar()
        a = Radiobutton(base, text="Male", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=1, command=selected)
        b = Radiobutton(base, text="Female", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=2, command=selected)
        c = Radiobutton(base, text="Other", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=0, command=selected)
        a.place(x=490,y=580)
        b.place(x=580,y=580)
        c.place(x=680,y=580)
        continu = Button(base, text="Continue", font=("Arial 15 bold"), bg="white", command=available_roome)
        continu.place(x=490, y=670)

        line = Canvas(base, height=670, width=2)
        line.place(x=1000, y=105)
    def add_room():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)
        h1 = Label(base, text="Add New Room", bg="dark slate grey", font=("Arial 20 bold"), fg="white", padx=500,
                   pady=10)
        h1.place(x=320, y=105)

        n_rm_n = Label(base, text="New Room No.", font=("Arial 20 bold"), bg="silver", fg="black")
        n_rm_n.place(x=500, y=300)
        rm_n_entry = Entry(base, width=20, font=("Arial 15 bold"))
        rm_n_entry.place(x=750, y=303)
        gender = Label(base,text="Gender", font=("Arial 20 bold"), bg="silver", fg="black")
        gender.place(x=500,y=350)

        global G
        G = 1
        def selected():
            global G
            if c1.get() == 1:
                G = 1
            if c1.get() == 2:
                G = 2
            if c1.get() == 0:
                G = 0
        c1 = IntVar()
        a = Radiobutton(base, text="Male", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=1,
                        command=selected)
        b = Radiobutton(base, text="Female", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=2,
                        command=selected)
        c = Radiobutton(base, text="Other", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=0,
                        command=selected)
        a.place(x=750, y=350)
        b.place(x=840, y=350)
        c.place(x=950, y=350)
        def add():
            file_name = ""
            bed1 = bed2 = bed3 = None
            r = (rm_n_entry.get())
            if G==1:
                bed1 = "B1"
                bed2 = "B2"
                bed3 = "B3"
                file_name = "room_info_boys.txt"
                f2 = open(file_name, "r")
            if G==2:
                bed1 = "G1"
                bed2 = "G2"
                bed3 = "G3"
                file_name = "room_info_girls.txt"
                f2 = open(file_name, "r")
            if G==0:
                bed1 = "O1"
                bed2 = "O2"
                bed3 = "O3"
                file_name = "room_info_others.txt"
                f2 = open(file_name, "r")
            all_lines = f2.readlines()
            count = 0
            for i in all_lines:
                temp = str(i)
                one_line = temp.split(',')
                if one_line[0] == r:
                    l = Label(base, text="Room Is Already Addded....!", font=("Arial 25 bold"), bg='silver',
                              fg="black")
                    l.place(x=650, y=600)
                    f2.close()
                    count = 2
            f2.close()       