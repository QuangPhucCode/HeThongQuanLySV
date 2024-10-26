############################################-Thư viện-############################################
from tkinter import *
import time
import random
from tkinter import Toplevel

###########################################-FUNCTION-#############################################

# Kết nối Database.
def Connectdb():
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('images/student.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='blue1')

    #
    hostlabel = Label(dbroot, text="Nhập Máy Chủ:",bg='yellow1',font=('Times New Roman',18,'bold'), relief=GROOVE,borderwidth=3,width=12, anchor='w')
    hostlabel.place(x=10, y=10)

    usernamelabel = Label(dbroot, text="Tài Khoản:",bg='yellow1',font=('Times New Roman',18,'bold'), relief=GROOVE,borderwidth=3,width=12, anchor='w')
    usernamelabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Mật Khẩu:",bg='yellow1',font=('Times New Roman',18,'bold'), relief=GROOVE,borderwidth=3,width=12, anchor='w')
    passwordlabel.place(x=10, y=130)

    #
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    
    hostentry = Entry(dbroot, font=('Times New Roman',16,'bold'),width=21,bd=4,textvariable=hostval)
    hostentry.place(x=200, y=10)

    userentry = Entry(dbroot, font=('Times New Roman',16,'bold'),width=21,bd=4,textvariable=userval)
    userentry.place(x=200, y=70)

    passwordentry = Entry(dbroot, font=('Times New Roman',16,'bold'),width=21,bd=4,textvariable=passwordval)
    passwordentry.place(x=200, y=130)

    #
    submitbutton = Button(dbroot, text='Đăng Nhập', font=('Times New Roman',16,'bold'),bg='red',bd=5, width=12,activebackground='black', activeforeground='white')
    submitbutton.place(x=165, y=187)


    dbroot.mainloop()

# Set Ngày, Giờ.
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Ngày : '+date_string+"\n"+"Giờ : "+time_string)
    clock.after(200,tick)

# Tạo chuyển động cho dòng chữ 'Chào Mừng đến với Hệ thống Quản lý Sinh Viên'.
def IntrolLabelTick(): 
    global count, text
    if(count >= len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(180, IntrolLabelTick)

# Tạo màu sắc ngẫu nhiên cho dòng chữ 'Chào Mừng đến với Hệ thống Quản lý Sinh Viên'.
colors = ['red', 'purple', 'blue']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(100,IntroLabelColorTick)  

###########################################-MAINCODE-################################################
root = Tk()

# Đặt tiêu đề và set màu cho background.
root.title('Hệ Thống Quản lý Sinh Viên')
root.config(bg='cyan2')

# Set Kích thước và icon.
root.geometry('1174x700+200+50')
root.iconbitmap('images/student.ico')
root.resizable(False, False)

# Tạo khung.
DataEntryFrame = Frame(root, bg='cyan2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500,height=600)

# khung hiển thị dữ liệu.
ShowDataFrame = Frame(root, bg='cyan2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=550, y=80, width=620,height=600)

# tạo khung chữ 'Chào Mừng đến với Hệ thống Quản lý Sinh Viên' và chỉnh kiểu chữ.
ss = 'Chào Mừng đến với Hệ thống Quản lý Sinh Viên'
count = 0
text = ''
SliderLabel = Label(root, text=ss,font=('Times New Roman',25, 'italic bold'), relief=RIDGE, borderwidth=4,width=35,bg='gold2')
SliderLabel.place(x=210, y=0)
IntrolLabelTick()
IntroLabelColorTick()

# Tạo đồng hồ.
clock = Label(root,font=('Times', 14, 'bold'), relief=RIDGE, borderwidth=4, bg='lawn green')
clock.place(x=0,y=0)
tick()

# Tạo nút nhấn login Admin.
connectbutton = Button(root,text='Login Admin', width=17,font=('Times New Roman',18, 'italic bold'), relief=RIDGE, borderwidth=4, bd=6, bg='lawn green',
                       activebackground='blue1', activeforeground='white',command=Connectdb)
connectbutton.place(x=919, y=0)



root.mainloop()

