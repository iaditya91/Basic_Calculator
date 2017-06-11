from tkinter import*

master=Tk()
display= Entry(master,width=46,justify="right",bd=10,bg='lightgrey')
master.title("Calculator")

class calculator:

    def __init__(self):
        self.var1=""
        self.var2=""
        self.result=0
        self.current=0
        self.operator=0

    def num_buttons(self,index):
        if self.current==0:
            self.var1= str(self.var1) + str(index)
            display.delete(first=0,last= END)
            display.insert(0, string=self.var1)
        else:
            self.var2= str(self.var2) + str(index)
            display.delete(first=0,last= END)
            display.insert(0, self.var2)

    def equate(self):
        if self.operator is 0:
            self.result = float(self.var1) + float(self.var2)
        elif self.operator is 1:
            self.result=float(self.var1) - float(self.var2)
        elif self.operator is 2:
            self.result=float(self.var1) * float(self.var2)
        elif self.operator is 3:
            self.result=float(self.var1) / float(self.var2)
        display.delete(first=0 ,last=END)
        display.insert(0, self.result)
        self.var1= self.result

    def set_op(self, op):
        self.operator= op
        display.delete(0, END)
        if self.current is 0:
            self.current = 1
        else:
         self.equate()
         self.var2 = ""

    def clear(self):
        self.__init__()
        display.delete(0,END)


calc=calculator()
#buttons
b0= Button(master,text='0',width=15,command=lambda : calc.num_buttons(0))
b1= Button(master,text='1',width=15,command=lambda : calc.num_buttons(1))
b2= Button(master,text='2',width=15,command=lambda : calc.num_buttons(2))
b3= Button(master,text='3',width=15,command=lambda : calc.num_buttons(3))
b4= Button(master,text='4',width=15,command=lambda : calc.num_buttons(4))
b5= Button(master,text='5',width=15,command=lambda : calc.num_buttons(5))
b6= Button(master,text='6',width=15,command=lambda : calc.num_buttons(6))
b7= Button(master,text='7',width=15,command=lambda : calc.num_buttons(7))
b8= Button(master,text='8',width=15,command=lambda : calc.num_buttons(8))
b9= Button(master,text='9',width=15,command=lambda : calc.num_buttons(9))
b_dot= Button(master,text='.',width=15,command=lambda : calc.num_buttons('.'))

#operators
plus= Button(master,text='+',width=15,command=lambda : calc.set_op(0))
minus= Button(master,text='-',width=15,command=lambda : calc.set_op(1))
times = Button(master,text='x',width=15,command=lambda : calc.set_op(2))
divide= Button(master,text='/',width=15,command=lambda : calc.set_op(3))
equals= Button(master,text='= ',width=15,command= calc.equate)
clear= Button(master,text='CE',width=15,command= calc.clear)


#positioning
display.place(x=0,y=2)
b7.grid(row=1 ,column=0)
b8.grid(row=1 ,column=1)
b9.grid(row=1 ,column=2)
b4.grid(row=2 ,column=0)
b5.grid(row=2 ,column=1)
b6.grid(row=2 ,column=2)
b1.grid(row=3 ,column=0)
b2.grid(row=3 ,column=1)
b3.grid(row=3 ,column=2)
b0.grid(row=4 ,column=0)
b_dot.grid(row=4 ,column=1)
clear.grid(row=4 ,column=2)
plus.grid(row=0 ,column=3)
minus.grid(row=1 ,column=3)
times.grid(row=2 ,column=3)
divide.grid(row=3 ,column=3)
equals.grid(row=4 ,column=3)
master.minsize(200,400);
master.mainloop()

