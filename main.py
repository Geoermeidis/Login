from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import re
import webbrowser
import tkinter.messagebox as tkm


def username_(user):
    a = user.get()
    x = re.findall("\d", a)
    y = re.findall("^[A-Z]", a)
    h = re.findall("[ ]", a)

    u_c = False
    if len(a) > 8 and x and y and not h:
        u_c = True
    print(u_c)
    if u_c:
        print("Username is eligible")
    else:
        print("try again")


def password_(po):
    p = po.get()
    p_c = False
    if len(p) > 8 and re.findall("\d", p) and not (re.findall("[ ]", p)):
        p_c = True
    print(p_c)
    if p_c:
        print("Password is eligible")
    else:
        print("try again")


def password_checking(pass_, pass2):
    a = pass_.get()
    b = pass2.get()
    if a == b:
        print("Password is good")
    else:
        print("The two passwords do not match, please try again")


def email_():
    webbrowser.open("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")


def age_calculation(day_list, month_list, year_list):
    days_in_year = 365.2425
    day = int(str(day_list.get()))
    month = int(str(month_list.get()))
    year = int(str(year_list.get()))
    birthday = date(year, month, day)
    age = int((date.today()-birthday).days / days_in_year)
    print(age)
    return age


def message(day_list, month_list, year_list):
    age_calculation(day_list, month_list, year_list)
    tkm.showinfo("Sign up", "Congratulations you have made a new account")


def open_new_window():
    new_window = Toplevel(bg="royalblue")
    new_window.title("Registration page")
    new_window.geometry("500x700")


    up_canvas = Canvas(new_window, bg="royalblue", height=60, width=500, highlightthickness=0)
    line = up_canvas.create_line(0, 45, 500, 45, fill="white")
    up_canvas.pack(fill=BOTH)
    main_label = Label(new_window, text="REGISTRATION", bg="royalblue", fg="white", font="Impact 20")
    main_label.place(x=160, y=4)

    entry1 = StringVar()
    entry2 = StringVar()
    entry3 = StringVar()
    entry4 = StringVar()
    entry5 = StringVar()
    entry6 = StringVar()
    entry1.set("Enter your name")
    entry2.set("Enter your surname")
    entry3.set("Enter your username")
    entry4.set("Enter your password")
    entry5.set("Confirm your password")
    entry6.set("Enter your email")

    name = Entry(new_window, bg="white", fg="black", bd=5, textvariable=entry1)
    surname = Entry(new_window, bg="white", fg="black", bd=5, textvariable=entry2)
    user = Entry(new_window, bg="white", fg="black", bd=5, textvariable=entry3)
    user_b = Button(new_window, bg="white", fg="black", command=lambda: username_(user))
    pass_ = Entry(new_window, bg="white", fg="black", bd=5, textvariable=entry4)
    pass_b = Button(new_window, bg="white", fg="black", command=lambda: password_(pass_))
    pass2 = Entry(new_window, bg="white", fg="black", bd=5, textvariable=entry5)
    pass2_b = Button(new_window, bg="white", fg="black", command=lambda: password_checking(pass_, pass2))
    email = Entry(new_window, bg="white", fg="black", bd=5, textvariable=entry6)


    user_b.place(x=220, y=175, width=20)
    pass_b.place(x=450, y=175, width=20)
    pass2_b.place(x=350, y=230, width=20)
    name.place(x=50, y=65, width=150)
    surname.place(x=275, y=65, width=150)
    user.place(x=50, y=175, width=150)
    pass_.place(x=275, y=175, width=150)
    pass2.place(x=50, y=230, width=250)
    email.place(x=50, y=120, width=300)


    age_label = Label(new_window, text="Date of birth", borderwidth=5, relief="sunken")
    day_ = StringVar()
    month_ = StringVar()
    year_ = StringVar()
    day_list = Combobox(new_window, textvariable=day_)
    month_list = Combobox(new_window, textvariable=month_)
    year_list = Combobox(new_window, textvariable=year_)
    ex1 = list()
    ex2 = list()
    ex3 = list()
    for i in range(1, 32):
        ex1.append(i)
    for i in range(1, 13):
        ex2.append(i)
    for i in range(1900, 2021):
        ex3.append(i)
    day_list["values"], month_list["values"], year_list["values"] = ex1, ex2, ex3
    age_label.place(x=50, y=285, height=30, width=150)
    day_list.place(x=50, y=325, height=20, width=60)
    month_list.place(x=150, y=325, height=20, width=80)
    year_list.place(x=270, y=325, height=20, width=60)


    sex_label = Label(new_window, text="Sex", borderwidth=5, relief="sunken")
    sex_label.place(x=50, y=360, width=100, height=30)
    main = IntVar()
    male_ = Radiobutton(new_window, text="Male", variable=main, bg="white", bd=3, relief="groove", value=1)
    female_ = Radiobutton(new_window, text="Female", variable=main,  bg="white", bd=3, relief="groove", value=2)
    different_ = Radiobutton(new_window, text="Different", variable=main,  bg="white", bd=3, relief="groove", value=3)
    male_.place(x=50, y=400, width=70, height=25)
    female_.place(x=150, y=400, width=70, height=25)
    different_.place(x=250, y=400, width=110, height=25)

    t_c = IntVar()
    terms_check = Checkbutton(new_window, text="I agree with the Terms of Services", variable=t_c, fg="white",
                              bg="royalblue", selectcolor="royalblue", activebackground="royalblue",
                              activeforeground="white")
    terms_check.place(x=50, y=435, width=200, height=30)

    reg_button = Button(new_window, text="REGISTER", bd=5, font="Impact 20", relief="sunken", bg="red", fg="white",
                        activeforeground="gray", activebackground="red",
                        command=lambda: message(day_list, month_list, year_list))
    reg_button.place(x=150, y=480, width=200, height=50)

    email_symbol = Label(new_window, text="❎", bg="royalblue", fg="white", bd=0, relief="flat")
    email_text = Label(new_window, bg="royalblue", fg="white", bd=0, relief="flat", font="Verdana 8",
                       text="Create a gmail account if you do not have one ")
    email_b = Button(new_window, text="HERE", bg="royalblue", fg="white", activebackground="royalblue",
                     activeforeground="red", font="Verdana 8 underline", bd=0, relief="flat", command=lambda: email_())
    email_text.place(x=55, y=550, width=280)
    email_symbol.place(x=35, y=550, width=15)
    email_b.place(x=335, y=547)



gui = Tk()

gui.configure(bg="maroon")
gui.title("Login")
gui.geometry("1000x500")


upframe = Frame(gui, bg="maroon")
loginframe = Frame(gui, bg="maroon")
registrationframe = Frame(gui, bg="maroon")
upframe.place(x=250, y=20, width=500, height=130)
loginframe.place(x=250, y=150, width=500, height=80)
registrationframe.place(x=250, y=400, width=500, height=100)


usernamelabel = Label(upframe, text="Username/Email: ", bg="maroon", fg="white", font="Impact 15")
usernamelabel.place(x=50, y=50, width=150, height=20)

passwordlabel = Label(upframe, text="Password:", bg="maroon", fg="white", font="Impact 15")
passwordlabel.place(x=50, y=95, width=100, height=20)

usernameentry = Entry(upframe, bg="white", fg="black", bd=5)
usernameentry.place(x=250, y=50, width=170, height=25)

passwordentry = Entry(upframe, show="*", bg="white", fg="black", bd=5)
passwordentry.place(x=250, y=95, width=170, height=25)

loginButton = Button(loginframe, text="Login", font="LITHOGRAPH 15", bg="darkblue", fg="white",
                     activebackground="lightseagreen", activeforeground="black")
loginButton.place(x=100, y=10, width=300, height=35)

question_text = Label(registrationframe, text="Are you not registered?", font="15", bg="maroon", fg="white")
registration_text = Button(registrationframe, text="Create an account", font="15", bg="maroon", fg="white",
                           command=lambda: open_new_window(), relief="flat", activebackground="maroon",
                           activeforeground="gray")
question_text.place(x=150, y=20)
registration_text.place(x=165, y=50)

gui.mainloop()


