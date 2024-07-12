from tkinter import Tk, Entry, Button, StringVar
from tkinter import ttk
class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='#35495e')
        master.resizable(False,False)

        self.equation=StringVar()
        self.entry_value=''
        


        Entry(width=17, borderwidth=5, highlightthickness=1,highlightbackground= '#eaf6f6', bg='#3baea0', font=('Arial Bold', 28), textvariable=self.equation, ).place(x=0, y=0)
        

        button_config = {
            'borderwidth':5,
            'highlightthickness': 1,
            
        }
        
        Button(master,width=11,height=4,text='(',relief='solid',bg='#eaf6f6',command=lambda:self.show('('), **button_config).place(x=0 ,y=50)
        Button(master,width=11,height=4,text=')',relief='solid',bg='#eaf6f6',command=lambda:self.show(')'), **button_config).place(x=90 ,y=50)
        Button(master,width=11,height=4,text='%',relief='solid',bg='#eaf6f6',command=lambda:self.show('%'),**button_config).place(x=180 ,y=50)
        Button(master,width=11,height=4,text='1',relief='solid',bg='#eaf6f6',command=lambda:self.show(1),**button_config).place(x=0 ,y=125)
        Button(master,width=11,height=4,text='2',relief='solid',bg='#eaf6f6',command=lambda:self.show(2), **button_config).place(x=90 ,y=125)
        Button(master,width=11,height=4,text='3',relief='solid',bg='#eaf6f6',command=lambda:self.show(3),**button_config).place(x=180 ,y=125)
        Button(master,width=11,height=4,text='4',relief='solid',bg='#eaf6f6',command=lambda:self.show(4), **button_config).place(x=0 ,y=200)
        
        Button(master,width=11,height=4,text='5',relief='solid',bg='#eaf6f6',command=lambda:self.show(5),  **button_config).place(x=90 ,y=200)
        Button(master,width=11,height=4,text='6',relief='solid',bg='#eaf6f6',command=lambda:self.show(6),  **button_config).place(x=180 ,y=200)
        Button(master,width=11,height=4,text='7',relief='solid',bg='#eaf6f6',command=lambda:self.show(7),  **button_config).place(x=0 ,y=275)
        Button(master,width=11,height=4,text='8',relief='solid',bg='#eaf6f6',command=lambda:self.show(8),  **button_config).place(x=180 ,y=275)
        Button(master,width=11,height=4,text='9',relief='solid',bg='#eaf6f6',command=lambda:self.show(9),  **button_config).place(x=90 ,y=275)
        Button(master,width=11,height=4,text='0',relief='solid',bg='#eaf6f6',command=lambda:self.show(0),  **button_config).place(x=90 ,y=350)
        Button(master,width=11,height=4,text='.',relief='solid',bg='#eaf6f6',command=lambda:self.show('.'),  **button_config).place(x=180 ,y=350)
        Button(master,width=11,height=4,text='+',relief='solid',bg='#eaf6f6',command=lambda:self.show('+'),  **button_config).place(x=270 ,y=275)
        Button(master,width=11,height=4,text='-',relief='solid',bg='#eaf6f6',command=lambda:self.show('-'),  **button_config).place(x=270 ,y=200)
        Button(master,width=11,height=4,text='/',relief='solid',bg='#eaf6f6',command=lambda:self.show('/'),  **button_config).place(x=270 ,y=50)
        Button(master,width=11,height=4,text='x',relief='solid',bg='#eaf6f6',command=lambda:self.show('*'),  **button_config).place(x=270 ,y=125)
        Button(master,width=11,height=4,text='=',relief='solid',bg='#eaf6f6',command=self.solve,  **button_config).place(x=270 ,y=350)
        Button(master,width=11,height=4,text='C',relief='solid',command=self.clear, **button_config).place(x=0 ,y=350)



    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)

    


root=Tk()
calculator=Calculator(root)
root.mainloop()
