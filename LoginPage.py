import tkinter as tk

def submit():
	#next step is to take all the inputs 
	#then you need error check

	username.append(nameIn.get())
	nameIn.delete(0,tk.END)
	print(username)

	password.append(passwordIn.get())
	passwordIn.delete(0,tk.END)
	print(password)

username = []
password = []
#main Window
root = tk.Tk()#creates the standard main window

#**************Widget I, II, III, IV**************
output = tk.Text(root,height = 15, width = 25)


output.config(state = "disable")
output.grid(row = 0, column = 0, rowspan = 5)

loginTitle1 = tk.Label(root, text = "Login", font = "georgia")
loginTitle1.config(background = "blue")
loginTitle1.grid(row = 1, column = 0, columnspan = 3, sticky = "NESW")
loginTitle1.columnconfigure(1, minsize= 1)

nameInput2 = tk.Label(root, text = "Name: ", font = "georgia")
nameInput2.grid(row = 3, column = 0, sticky = "E")

passInput3 = tk.Label(root, text = "Password: ", font = "georgia")
passInput3.grid(row = 4, column = 0, sticky = "E")

#**************Widget V, VI, VII**************
nameIn = tk.Entry(root)
nameIn.grid(row = 3, column = 1, sticky = "W")

passwordIn = tk.Entry(root, show = "*")
passwordIn.grid(row = 4, column = 1, sticky = "W")


loginBu = tk.Button(root, text="Login", width = 30, height = 5, command = submit)
loginBu.grid(row = 5, column = 0, columnspan = 2)









root.mainloop()


