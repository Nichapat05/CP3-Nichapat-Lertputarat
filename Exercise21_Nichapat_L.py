from tkinter import *
import math

def Calculate(event):
    BMI = float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2)
    labelResult.configure(text=BMI)
    if BMI >= 30 :
        labelBMI.configure(text="อ้วนมาก",fg = "red",font=(100))
    elif BMI >= 25 :
        labelBMI.configure(text="อ้วน",fg = "orange",font=(100))
    elif BMI >= 23:
        labelBMI.configure(text="น้ำหนักเกิน",fg="yellow",font=(100))
    elif BMI >= 18.6:
        labelBMI.configure(text="น้ำหนักปกติ เหมาะสม",fg="green",font=(100))
    else:
        labelBMI.configure(text="ผอมเกินไป",fg="red",font=(100))


MainWindow  = Tk()

labelTitle = Label(MainWindow,text="BMI calculator program",font=(100),bg="#DCDCDC",fg="#330066").grid(row=0)

labelHeight =Label(MainWindow,text="ส่วนสูง (Cm)",font=(100))
labelHeight.grid(row =1,column = 0)
textboxHeight = Entry(MainWindow,font=(100))
textboxHeight.grid(row = 1,column = 1)

labelWeight =Label(MainWindow,text="น้ำหนัก (Kg)",font=(100))
labelWeight.grid(row =2,column = 0)
textboxWeight = Entry(MainWindow,font=(100))
textboxWeight.grid(row = 2,column = 1)

calculatebutton = Button(MainWindow,text="คำนวณ",font=(100),bg="#7CFC00")
calculatebutton.grid(row = 3)
calculatebutton.bind('<Button-1>',Calculate)

labelResult = Label(MainWindow,text="ผลลัพธ์",font=(100))
labelResult.grid(row = 3,column=1)

labelBMI = Label(MainWindow,text=" ",font=(100))
labelBMI.grid(row =3,column = 2)
MainWindow.mainloop()