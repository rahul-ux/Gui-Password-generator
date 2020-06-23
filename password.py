Author : " codewithkapil"
"===========================================KAPIL KUMAR=================================================="

from tkinter import*
import random

root = Tk()

root.geometry("700x00")
root.minsize(700,400)
root.maxsize(800,400)
root.wm_iconbitmap("15.ico")
root.title("Password Generator")
root.config(bg="pink")


# creating password 

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]()*;/?.$#@%_-=+"

ALL = lower_case + upper_case + symbols




def helpmenu():
	import tkinter as Tkinter

	root =  Tk()

	root.geometry("400x200")
	root.maxsize(400,300)
	root.title("HELP!")
	root.wm_iconbitmap("21.ico")
	root.config(bg="yellow")

	Label(root,text="Contact Us At",font="Times 20 bold",bg="yellow",
		fg="green").pack(fill=BOTH)

	Label(root,text="kapilkumar\ngautam3652gmail.com",font="Times 20 italic",
		bg="yellow",fg="red").pack(fill=BOTH)

	Label(root,text="Instagram",font="Times 20 bold",bg="yellow",
		fg="blue").pack(fill=BOTH)

	Label(root,text="codewithkapil",font="Times 20 italic",bg="yellow",
		fg="red").pack(fill=BOTH)





	root.mainloop()

def password():
	try:
		Password = "".join(random.sample(ALL,int(length_value.get())))
		Pass_value.set(Password)
	except Exception as e:
		Pass_value.set("Enter length")

	if int(length_value.get()) <= 7:
		position_value.set("Weak")

	elif int(length_value.get()) <=10:
		position_value.set("Average",)

	elif int(length_value.get()) <=20:
		position_value.set("Strong")

	else:
		position_value.set("Strogest")
		
		
	




def clear():
	passentry.delete(0,END)
	lengthentry.delete(0,END)
	position_value.set("")



# creating label for Heading 
Label(root,text="PASSWORD GENERATOR",font="Times 24 bold",fg="green",bg="pink",
	justify=CENTER).grid(row=1,column=2,pady=20)


#defining variable for storing value

length_value = StringVar()
Pass_value = StringVar()
position_value = StringVar()


# creating label for length

#label1
Label(root,text="Length",font="lucida 14 bold",
	fg="black",bg="pink").grid(row=2,column=1,padx=10)
#label1 entry

lengthentry = Entry(root,textvariable=length_value,width=10,
	font="lucida 14 ",justify=CENTER,relief=SUNKEN,bd=3)
lengthentry.grid(row=2,column=2,padx=10)








Label(root,text="Password",font="lucida 14 bold",
	fg="black",bg="pink").grid(row=3,column=1,padx=10,pady=30)


passentry = Entry(root,textvariable=Pass_value,width=40,font="lucida 14 ",
	justify=CENTER,relief=SUNKEN,bd=3)
passentry.grid(row=3,column=2,padx=10)

situationentry = Entry(root,textvariable=position_value,width=10,font="lucida 10 bold",justify=CENTER).grid(row=3,column=3)



Button(root,text="CreatePass",font="Times 14 bold",
	bg="white",fg="black",width=10,height=1,command=password).grid(row=8,column=1,padx=10,pady=30)




Button(root,text="Clear",font="Times 14 bold",bg="white",
	fg="black",width=8,command=clear).grid(row=8,column=2)


Button(root,text="Exit",font="Times 14 bold",bg="white",
	fg="black",width=8,command=quit).grid(row=8,column=3)



Button(root,text="Help!",font="lucida 16 italic",bg="grey",fg="red",width=10
	,command=helpmenu).grid(row=12,column=2)

root.mainloop()
"===================================================KAPIL KUMAR==============================="