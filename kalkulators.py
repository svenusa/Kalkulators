from tkinter import*

logs=Tk()
logs.title("Kalkulators")

num1 = 0
mathOp = ""

def notirit():
    global num1
    global mathOp
    Display.delete(0,END)
    num1=0
    mathOp=""
    return 0

def btnClick(number):
    current=Display.get()#Nolasa skaitli
    Display.delete(0,END)#Nodzēšs skaitļus
    newNumber=str(current)+str(number)
    Display.insert(0,newNumber)#Ievieto displejā
    return 0

def btnCommand(command):
    global number
    global num1
    global mathOp
    mathOp=command
    num1=int(Display.get())
    Display.delete(0,END)
    return 0

def Vienads():
    global num1
    global mathOp
    num2 = int(Display.get())
    result = 0
    if mathOp == "+":
        result = num1 + num2
    elif mathOp == "-":
        result = num1 - num2
    elif mathOp == "*":
        result = num1 * num2
    elif mathOp == "/":
        result = num1 / num2
    
    Display.delete(0, END)
    Display.insert(0, str(result))
    return 0


Display=Entry(logs,width=25,bd=15,font=("Roman",20),justify="right")#Lodziņš spociņš

btn0=Button(logs,text="0",padx="40",pady="20",bg="#F5B7B1",font=("Roman",15),command=lambda:btnClick(0))
btn1=Button(logs,text="1",padx="40",pady="20",bg="#F5B7B1",font=("Roman",15),command=lambda:btnClick(1))
btn2=Button(logs,text="2",padx="40",pady="20",bg="#F5B7B1",font=("Roman",15),command=lambda:btnClick(2))
btn3=Button(logs,text="3",padx="40",pady="20",bg="#F5B7B1",font=("Roman",15),command=lambda:btnClick(3))
btn4=Button(logs,text="4",padx="40",pady="20",bg="#F5B7B1",font=("Roman",15),command=lambda:btnClick(4))
btn5=Button(logs,text="5",padx="40",pady="20",bg="#F5B7B1",font=("Roman",15),command=lambda:btnClick(5))
btn6=Button(logs,text="6",padx="40",pady="20",bg="#F5B7B1",font=("Roman",15),command=lambda:btnClick(6))
btn7=Button(logs,text="7",padx="40",pady="20",bg="#F5B7B1",font=("Roman",15),command=lambda:btnClick(7))
btn8=Button(logs,text="8",padx="40",pady="20",bg="#F5B7B1",font=("Roman",15),command=lambda:btnClick(8))
btn9=Button(logs,text="9",padx="40",pady="20",bg="#F5B7B1",font=("Roman",15),command=lambda:btnClick(9))
btnSask=Button(logs,text="+",padx='40',pady="20",bg="#EC7063",font=("Roman",15),command=lambda:btnCommand("+") )
btnAtn=Button(logs,text="-",padx='40',pady="20",bg="#EC7063",font=("Roman",15),command=lambda:btnCommand("-") )
btnReiz=Button(logs,text="*",padx='40',pady="20",bg="#EC7063",font=("Roman",15),command=lambda:btnCommand("*") )
btnDal=Button(logs,text="/",padx='40',pady="20",bg="#EC7063",font=("Roman",15),command=lambda:btnCommand("/") )
btnC=Button(logs,text="C",padx='40',pady="20",bg="#F5B7B1",font=("Roman",15),command=notirit )
btnEQ=Button(logs,text="=",padx='40',pady="20",bg="#F5B7B1",font=("Roman",15),command=Vienads )

Display.grid(row=0, column=0, columnspan=4) #Atrašanās vieta pogām
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btnSask.grid(row=1,column=3)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btnAtn.grid(row=2,column=3)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btnReiz.grid(row=3,column=3)

btn0.grid(row=4,column=0)
btnC.grid(row=4,column=1)
btnEQ.grid(row=4,column=2)
btnDal.grid(row=4,column=3)

logs.mainloop()