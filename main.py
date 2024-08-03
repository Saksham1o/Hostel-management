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
                