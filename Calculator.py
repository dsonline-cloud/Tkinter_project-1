#Building a Calculator:

from tkinter import *


#Creating a function named "click":
def click(event): #To create an event function for binding it with the buttons we have to take the "event" as the argument while defining the funtion.
    global scvalue #With this we can modify the value of the variable "scvalue" within the funtion.
    text = event.widget.cget("text") 
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get()) #If the scvalue is digit then it will be assigned to value variable after typecasting it to the integer value.
        else:
            try:
                value = eval(screen.get()) #In case it's not a digit which means it's an expression like 2*3, 5+8, 6/6 then it will be converted to appropriate type for performing the operations.
            
            except Exception as e:
                print(e)
                value ="Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
         scvalue.set("") #Whatever the value of scvalue variable might be but if we click "C" on calculator then it's value will again be updated as empty sring.
         screen.update() #Updaing the scvalue in the screen object(entry class/function).


    else:
        scvalue.set(scvalue.get() + text) #We are updating the value of variable "scvalue". Quite Smart!
        screen.update() #It will update the values in the screen(which is the entry function for taking the input). So it will basically update the current value of scvalue variable with the new value and it will keep the old scvalue as it is.




#scvalue.set(scvalue.get() + text) 
#1. scvalue.set() -> It will set the value of the variable "scvalue".
#2. scvalue.get() -> It will get the value of "scvariable" which is currently set(in this case it's empty strint).

root = Tk()
root.geometry("550x700")
root.title("Calculator")

#Creating the icon of the calculator.
# photo = PhotoImage(file = "Calc.png") #PhotoImage object is created.
# root.iconphoto(False, photo) #Icon setput of for gui window.

#Creating an icon using .ico (icon) file, for this I have searched ".ico file in google" and found multiple .ico files at this website: "https://icon-icons.com/icon". Downloaded a file from here and used it.
root.wm_iconbitmap("calc.ico") 

#Creating a variale.
scvalue = StringVar()
scvalue.set("") #Initial value of this variable is set as empty string.

#Taking an input from the user. It's a normal input in tkinter which will create kind of a space(screen) for entering the value in the gui window.
screen = Entry(root, textvar = scvalue, font = "lucida 32 bold") #For taking the input.
screen.pack(fill = X, pady = 10, padx = 10)

#Creating frame for packing the buttons. We will be creating multiple button.
f= Frame(root, bg= "grey") #creating a frame.
#Button - 1
b= Button(f, text = "9", padx=25, pady= 18, font =  "lucida 32 bold") #Creating a button and packing it in the frame. This button's label is 9 hence the button which will be created will have the value 9 and obviously we can press that button.
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click) #Binding the button with click function/event. Whenever this button will be clicked the function "click" will be called.
#Button - 2
b= Button(f, text = "8",padx=25, pady= 18, font =  "lucida 32 bold")
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)
#Button - 3
b= Button(f, text = "7",padx=25, pady= 18, font =  "lucida 32 bold") 
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)
#Button - 4
b= Button(f, text = "6",padx=25, pady= 18, font =  "lucida 32 bold")
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)

f.pack() #We will pack the frame in the end after packing all the buttons.


#Creating another frame for packing the buttons. We will again be creating multiple button.
f= Frame(root, bg= "grey") #creating a frame.
#Button - 5
b= Button(f, text = "5",padx=25, pady= 18, font =  "lucida 32 bold") 
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)
#Button - 6
b= Button(f, text = "4",padx=25, pady= 18, font =  "lucida 32 bold")
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)
#Button - 7
b= Button(f, text = "3", padx=25, pady= 18,font =  "lucida 32 bold")
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)
#Button - 8
b= Button(f, text = "2", padx=25, pady= 18, font =  "lucida 32 bold") 
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)

f.pack()


#Creating another frame for packing the buttons. We will create multiple button.
f= Frame(root, bg= "grey") #creating a frame.
#Button - 9
b= Button(f, text = "1", padx=27, pady= 18,font =  "lucida 32 bold") 
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click) 
#Button - 10
b= Button(f, text = "-", padx=27, pady= 18,font =  "lucida 32 bold")
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)
#Button - 11
b= Button(f, text = "+", padx=27, pady= 18, font =  "lucida 32 bold")  
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)
#Button - 12
b= Button(f, text = "*", padx=27, pady= 18,font =  "lucida 32 bold") 
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)

f.pack()

#Creating another frame for packing the buttons. We will create multiple button.
f= Frame(root, bg= "grey") #creating a frame.
#Button - 13
b= Button(f, text = "/",padx=26, pady= 18, font =  "lucida 32 bold") 
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click) #Binding the button with click function/event. Whenever this button will be clicked the function "click" will be called.
#Button - 14
b= Button(f, text = "C",padx=25, pady= 18, font =  "lucida 32 bold") 
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)
#Button - 15
b= Button(f, text = "=",padx=25, pady= 18, font =  "lucida 32 bold")  
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)
#Button - 16
b= Button(f, text = "%",padx=20, pady= 18, font =  "lucida 32 bold") 
b.pack(side = LEFT, padx=18, pady= 5)
b.bind("<Button - 1>", click)

f.pack()


root.mainloop()
