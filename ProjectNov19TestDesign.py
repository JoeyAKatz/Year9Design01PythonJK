import tkinter as tk


def submit():
	#next step is to take all the inputs 
	#then you need error check

	vardis = distanceIn.get()
	distance.append(distanceIn.get())
	distanceIn.delete(0,tk.END)
	print(distance)
	

	varroute = routeIn.get()
	route.append(routeIn.get())
	routeIn.delete(0,tk.END)
	print(route)
	

	vartime = timeIn.get()
	time.append(timeIn.get())
	timeIn.delete(0,tk.END)
	print(time)


	vardate = dateIn.get()
	date.append(dateIn.get())
	dateIn.delete(0,tk.END)
	print(date)

	f.write(vardis+","+varroute+","+vartime+","+vardate+"\n")
	f.close()

f = open("testfile.txt","w")


#Store you data
#When you press submit you need to add an element ot list. You will use this list
#to display historial data. 
route = []
distance = []
time = []
date = []
#main Window
root = tk.Tk()#creates the standard main window

#**************Widget I, II, III, IV, V**************
output = tk.Text(root,height = 35, width = 10)

output.config(state = "disable")
output.grid(row = 0, column = 0, rowspan = 5)

labInput1 = tk.Label(root, text = "Running Tracker", font = "georgia")
labInput1.config(background = "blue")
labInput1.grid(row = 1, column = 0, columnspan = 4, sticky = "NESW")

labInput2 = tk.Label(root, text = "Distance: ", font = "georgia")
labInput2.grid(row = 3, column = 0, sticky = "E")

labInput3 = tk.Label(root, text = "Route: ", font = "georgia")
labInput3.grid(row = 3, column = 2, sticky = "E")

labInput4 = tk.Label(root, text = "Time: ", font = "georgia")
labInput4.grid(row = 4, column = 0, sticky = "E")

labInput5 = tk.Label(root, text = "Date: ", font = "georgia")
labInput5.grid(row = 4, column = 2, sticky = "E")

#**************Widget VI, VII, VIII, IX**************
distanceIn = tk.Entry(root)
distanceIn.grid(row = 3, column = 1, sticky = "E")

routeIn = tk.Entry(root)
routeIn.grid(row = 3, column = 3, sticky = "E")

timeIn = tk.Entry(root)
timeIn.grid(row = 4, column = 1, sticky = "E")

dateIn = tk.Entry(root)
dateIn.grid(row = 4, column = 3, sticky = "E")

#**************Widget X**************

bu1 = tk.Button(root, text="Input Data", width = 57, height = 5, command = submit)
bu1.grid(row = 5, column = 0, columnspan = 6, sticky = "W")

#**************Widget XI**************

page2title = tk.Label(root, text = "Past Data", font = "georgia")
page2title.config(background = "lime green")
page2title.grid(row = 1, column = 4, columnspan = 4, sticky = "NESW")

#**************Widget XI**************

page2lab1 = tk.Label(root, text = "Distance", font = "georgia")
page2lab1.grid(row = 2, column = 4)

page2lab2 = tk.Label(root, text = "Route", font = "georgia")
page2lab2.grid(row = 2, column = 5)

page2lab3 = tk.Label(root, text = "Time", font = "georgia")
page2lab3.grid(row = 2, column = 6)

page2lab4 = tk.Label(root, text = "Date", font = "georgia")
page2lab4.grid(row = 2, column = 7)


root.mainloop()




