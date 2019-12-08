from tkinter import *
'''
1. Frame
'''

# create root window

root = Tk()
#give a title for root window
root.title("My Frame")

#create a frame as child to root window
f = Frame(root,height=400,width = 500,bg="yellow", cursor="cross")
f.pack()
root.mainloop()

'''
2. Widgets - Button
Other widgets - Label,Messsage,Text,Scrollbar,Checkbutton,Radiobutton
Entry,Spinbox,Listbox,Menu
'''

#method to be called when the button is clicked

def buttonClick(self):
    print('you have clicked me')

# create root window
root = Tk()
#Create frame as child to root window

f = Frame(root,height=200,width=300)
# Let the frame will not shrink
f.propagate(0)
#Attach frame to the root window
f.pack()

#create push button as a child to frame
b = Button(f,text='My Button',width=15,height=2,bg='yellow',fg='blue',activebackground='green',activeforeground='red')

#Attach button to frame
b.pack()

#bind the left mouse button with the method to be called
b.bind("<Button-1>",buttonClick)
root.mainloop()


'''
3. Widgets - Button - Event handler

'''
def clickbutton():
    print('you  have clicked me')

root = Tk()
f = Frame(root,width=300,height=300)
f.propagate(0)
f.pack()
b = Button(f,text="click me", width = 30,height=20,bg='blue',fg='white',command=clickbutton)
b.pack()

root.mainloop()

'''
3. Widgets - Button - Event handler- with a class

'''

class MyButton():
    def __init__(self,root):
        #create a frame as a child to root window
        self.f = Frame(root,height=200,width=300)
        #let the frame will not shrink
        self.f.propagate(0)
        # attach the frame to root window
        self.f.pack()
        # create a button
        self.b = Button(self.f,text='My Button',width=50,height=30,bg='yellow',fg='blue',activebackground='green',activeforeground='red',command=self.buttonclick)
        #attach button to the frame
        self.b.pack()
    
    def buttonclick(self):
        print('you have clicked me')

root = Tk()
MyButton(root)
root.mainloop()

'''
4. Widgets - Button - Event handler- with a class-lambda

'''

class MyButton():
    def __init__(self,root):
        self.f = Frame (root,height=400,width=500)
        self.f.propagate(0)
        self.f.pack()
        
        self.b1= Button(self.f,text='Red',width=15,height=2,command=lambda: self.buttonClick(1))
        self.b2= Button(self.f,text='Green',width=15,height=2,command=lambda: self.buttonClick(2))
        self.b3= Button(self.f,text='Blue',width=15,height=2,command=lambda: self.buttonClick(3))
        
        # attach buttons to the frame
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        
    def buttonClick(self,num):
        if num==1:
            self.f["bg"] ='red'
        if num ==2:
            self.f["bg"]='green'
        if num ==3:
            self.f["bg"]='blue'
root = Tk()
mb=MyButton(root)
root.mainloop()
            
'''
5 - Arranging widgets in the Frame
Pack Layout,Grid Layout,Place Layout

b.pack(fill=X) - Occupy horizontally. No space outside the widget
b.pack(fill=Y) - Occupy vertically
b.pack(fill=BOTH) - Occupy both
b.pack(fill=NONE) - Occupy none
'''
#Pack
root=Tk()

f=Frame(root,width=400,height=300)
f.propagate()
f.pack()
b1=Button(f,width=30,height=10,text='Red',bg='red')
b1.pack(fill=X,padx=10,pady=20)
b2=Button(f,width=30,height=10,text='Green',bg='green')
b2.pack(fill=X,padx=20,pady=25)
b3=Button(f,width=30,height=10,text='Blue',bg='blue')
b3.pack(side=RIGHT)

root.mainloop()

#grid

root=Tk()

f=Frame(root,width=400,height=300)
f.propagate()
f.pack()
b1=Button(f,width=30,height=10,text='Red',bg='red')
b1.grid(row=0,column=0,padx=10,pady=20)
b2=Button(f,width=30,height=10,text='Green',bg='green')
b2.grid(row=0,column=1,padx=20,pady=25)
b3=Button(f,width=30,height=10,text='Blue',bg='blue')
b3.grid(row=1,column=0)

root.mainloop()

'''
6 - Display a label upon clicking a push button
'''
class MyButton():
    def __init__(self,root):
        self.f = Frame(root,height=350,width=500)
        #self.f.propagate(0)
        self.f.pack()
        
        self.b1=Button(self.f,text='Click Me',width = 20,height=5,command=self.buttonClick)
        self.b2=Button(self.f,text='Close',width = 20,height=5,command=quit)
        self.b1.grid(row=0,column=1)
        self.b2.grid(row=0,column=2)
        
    def buttonClick(self):
        self.lbl = Label(self.f,text='Welcome to Python',width=20, \
                             height=2,font=('Courier',-30,'bold underline'),fg='blue')
        self.lbl.grid(row=2,column=0)
        
root = Tk()
mb=MyButton(root)
root.mainloop()

'''
7 - Entry widget
'''

from tkinter import *

class MyEntry():
    def __init__(self,root):
        self.f = Frame(root,height=350, width = 500)
        #self.f.propagate(0)
        self.f.pack()
        
        # labels
        self.l1 = Label(text='Enter user name')
        self.l2 = Label(text='Enter password')
        self.l1.place(x=50,y=100)
        self.l2.place(x=50,y=150)
        
        #Entry for user name
        
        self.e1 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.e2 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14),show='*')
        
        self.e1.place(x=150,y=100)
        self.e2.place(x=150,y=150)
        self.e2.bind("<Return>",self.display)
        
    def display(self,event):
        str1 = self.e1.get()
        str2 = self.e2.get()
        
        # display the values uisng labels
        lbl1 = Label(text='Your name is : '+str1).place(x=150,y=200)
        lb12 = Label(text='Your password is " '+str2).place(x=150,y=220)

root = Tk()
me = MyEntry(root)
root.mainloop()

'''
8 - Checkbox widget
'''
from tkinter import *

class Mycheck():
    def __init__(self,root):
        self.f = Frame(root,width=500,height=300)
        self.f.propagate(0)
        self.f.pack()
        
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        
        self.c1 = Checkbutton(self.f,bg='yellow',fg='green',text='Java',variable=self.var1,command=self.display)
        self.c1.pack()
        self.c1.place(x=50,y=50)
    
        self.c2 = Checkbutton(self.f,bg='yellow',fg='green',text='Python',variable=self.var2,command=self.display)
        self.c2.pack()
        self.c2.place(x=100,y=50)
    
        self.c3 = Checkbutton(self.f,bg='yellow',fg='green',text='.Net',variable=self.var3,command=self.display)
        self.c3.pack()
        self.c3.place(x=150,y=50)
    
    def display(self):
        x = self.var1.get()
        y = self.var2.get()
        z = self.var3.get()
        
        str=''
        if (x==1):
            str+='Java '
        if (y==1):
            str+='Python '
        if (z==1):
            str+='.Net '
        
        lbl = Label(text=str,fg='blue').place(x=70,y=100,width=200,height=20)
root = Tk()
mc = Mycheck(root)
root.mainloop()

'''
9 - Radiobutton widget
'''
from tkinter import *

class RadioButtonDemo():
    def __init__(self,root):
        self.f = Frame(root,width=500,height=300)
        self.f.propagate(0)
        self.f.pack()
        
        self.var = IntVar()
        
        
        
        self.c1 = Radiobutton(self.f,bg='yellow',fg='green',text='Male',variable=self.var,value=1,command=self.display)
        self.c1.pack()
        self.c1.place(x=50,y=50)
    
        self.c2 = Radiobutton(self.f,bg='yellow',fg='green',text='Python',variable=self.var,value=2,command=self.display)
        self.c2.pack()
        self.c2.place(x=100,y=50)
    
        
    
    def display(self):
        x = self.var.get()
        print('value ',x)        
        
        str=''
        if (x==1):
            str+='You have selected Male '
        if (x==2):
            str+='You have selected Female '
        
        
        lbl = Label(text=str,fg='blue').place(x=70,y=100,width=200,height=20)
root = Tk()
mc = RadioButtonDemo(root)
root.mainloop()
