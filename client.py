import socket
from tkinter import *
x = ""
#time=""
def ent(num):
    global x
    x = x + str(num)
    data.set(x)
    #if(x=='='):
     #   x = x.split('$')
     #   print("hiiiiiiiiiiiiiiiii")
     #   if(len(x)==4):
     #       data.set(x[1], x[2])
     #   elif(len(x)==5):
     #       data.set(x[1], x[2], x[3])
     #   else:
     #       print("wrng")
def eq():
    global x
    print(x)
    check = str(x)
    s.send(check.encode())
    x=""
    result = s.recv(1024).decode()

    if result == "ZeroDiv":
        data.set("You can't divide by 0, try again")
    elif result == "MathError":
        data.set("There is an error with your math, try again")
    elif result == "SyntaxError":
        data.set("There is an invalid syntax , please try again")
    elif result == "NameError":
        data.set("You did not enter an equation, try again")
    else:
        data.set(result)

def clear():
    global x
    x=""
    data.set("")


def create_calci():
    gui = Tk()
    gui.configure(background="white")
    gui.title("Socket_Calculator")
    gui.geometry("310x310")
    global data
    data = StringVar()
    x_field = Entry(gui, textvariable=data, bg='white')
    x_field.grid(columnspan=10, ipadx=100)

    #global timeMSG
    #timeMSG=StringVar()
    #msg='the time is:'
    #messageVar = Message(gui, text=msg)
    #messageVar.config(bg='lightgreen')
    #messageVar.pack()

    data.set('')

    button1 = Button(gui, text='1', fg='black', bg='grey81', command=lambda: ent(1), height=1, width=7, pady=10)
    button1.grid(row=2, column=0)
    button2 = Button(gui, text='2', fg='black', bg='grey81',command=lambda: ent(2), height=1, width=7, pady=10)
    button2.grid(row=2, column=1)
    button3 = Button(gui, text='3', fg='black', bg='grey81', command=lambda: ent(3), height=1, width=7, pady=10)
    button3.grid(row=2, column=2)
    buttondollar = Button(gui, text='$', fg='black', bg='yellow', command=lambda: ent('$'), height=1, width=7, pady=10)
    buttondollar.grid(row=2, column=3)
    button4 = Button(gui, text='4', fg='black', bg='grey81',command=lambda: ent(4), height=1, width=7, pady=10)
    button4.grid(row=3, column=0)
    button5 = Button(gui, text='5', fg='black', bg='grey81', command=lambda: ent(5), height=1, width=7, pady=10)
    button5.grid(row=3, column=1)
    button6 = Button(gui, text='6', fg='black', bg='grey81', command=lambda: ent(6), height=1, width=7, pady=10)
    button6.grid(row=3, column=2)
    buttonclear = Button(gui, text='AC', fg='black', bg='grey81', command=clear, height=1, width=7, pady=10)
    buttonclear.grid(row=3, column=3)
    button7 = Button(gui, text='7', fg='black', bg='grey81', command=lambda: ent(7), height=1, width=7, pady=10)
    button7.grid(row=4, column=0)
    button8 = Button(gui, text='8', fg='black', bg='grey81', command=lambda: ent(8), height=1, width=7, pady=10)
    button8.grid(row=4, column=1)
    button9 = Button(gui, text='9', fg='black', bg='grey81', command=lambda: ent(9), height=1, width=7, pady=10)
    button9.grid(row=4, column=2)
    button9 = Button(gui, text='SPC', fg='black', bg='grey81', command=lambda: ent(" "), height=1, width=7, pady=10)
    button9.grid(row=4, column=3)
    button0 = Button(gui, text='0', fg='black', bg='grey81', command=lambda: ent(0), height=1, width=7, pady=10)
    button0.grid(row=5, column=0)
    buttonf = Button(gui, text='.', fg='black', bg='grey81', command=lambda: ent('.'), height=1, width=7, pady=10)
    buttonf.grid(row=5, column=1)
    buttonAns = Button(gui, text='=', fg='black', bg='lightblue', command=eq, height=1, width=7, pady=10)
    buttonAns.grid(row=5, column=2)
    addB = Button(gui, text='Add', fg='black', bg='grey81', command=lambda: ent("Add"), height=1, width=7, pady=10)
    addB.grid(row=6, column=0)
    subB = Button(gui, text='Subtract', fg='black', bg='grey81', command=lambda: ent('Subtract'), height=1, width=7, pady=10)
    subB.grid(row=6, column=1)
    mulB = Button(gui, text='Multiply', fg='black', bg='grey81', command=lambda: ent('Multiply'), height=1, width=7, pady=10)
    mulB.grid(row=6, column=2)
    divB = Button(gui, text='Divide', fg='black', bg='grey81', command=lambda: ent('Divide'), height=1, width=7, pady=10)
    divB.grid(row=6, column=3)
    sinB = Button(gui, text='sin', fg='black', bg='grey81', command=lambda: ent("sin"), height=1, width=7, pady=10)
    sinB.grid(row=7, column=0)
    cosB = Button(gui, text='cos', fg='black', bg='grey81', command=lambda: ent("cos"), height=1, width=7, pady=10)
    cosB.grid(row=7, column=1)
    tanB = Button(gui, text='tan', fg='black', bg='grey81', command=lambda: ent('tan'), height=1, width=7, pady=10)
    tanB.grid(row=7, column=2)
    cotB = Button(gui, text='cot', fg='black', bg='grey81', command=lambda: ent('cot'), height=1, width=7, pady=10)
    cotB.grid(row=7, column=3)
    gui.mainloop()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.connect((host,port))
#inputdata = raw_input("num:")
#s.sendall(b'inputdata')
#print (s.recv(1024).decode())
create_calci()
s.close()
