import tkinter as tk

#main Window
root = tk.Tk()#creates the standard main window

#**************Widget I, II, III, IV, V**************
output = tk.Text(root,height = 37.5, width = 75)


output.config(state = "disable")
output.grid(row = 0, column = 0, rowspan = 10)

labInput1 = tk.Label(root, text = "Data", font = "georgia")
labInput1.config(background = "blue")
labInput1.grid(row = 0, column = 0, columnspan = 5, sticky = "NESW")
labInput1.columnconfigure(1, minsize= 1)

labInput2 = tk.Label(root, text = "Distance", font = "georgia")
labInput2.grid(row = 1, column = 0, sticky = "NW")

labInput3 = tk.Label(root, text = "Route", font = "georgia")
labInput3.grid(row = 1, column = 1, sticky = "NW")

labInput4 = tk.Label(root, text = "Time", font = "georgia")
labInput4.grid(row = 1, column = 2, sticky = "NW")

labInput5 = tk.Label(root, text = "Date", font = "georgia")
labInput5.grid(row = 1, column = 3, sticky = "NW")
s
#**************Widget VI, VII, VIII, IX**************







root.mainloop()