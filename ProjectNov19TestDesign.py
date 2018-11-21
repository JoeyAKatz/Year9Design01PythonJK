import tkinter as tk

#main Window
root = tk.Tk()#creates the standard main window

#**************Widget I, II, III, IV, V**************
output = tk.Text(root,height = 35, width = 20)

output.config(state = "disable")
output.grid(row = 0, column = 0, rowspan = 5)

labInput1 = tk.Label(root, text = "Running Tracker", font = "georgia")
labInput1.config(background = "blue")
labInput1.grid(row = 1, column = 0, columnspan = 7, sticky = "NESW")

labInput2 = tk.Label(root, text = "Distance: ", font = "georgia")
labInput2.grid(row = 3, column = 0, sticky = "W")

labInput3 = tk.Label(root, text = "Route: ", font = "georgia")
labInput3.grid(row = 3, column = 4, sticky = "W")

labInput4 = tk.Label(root, text = "Time: ", font = "georgia")
labInput4.grid(row = 4, column = 0, sticky = "W")

labInput5 = tk.Label(root, text = "Date: ", font = "georgia")
labInput5.grid(row = 4, column = 4, sticky = "W")

#**************Widget VI, VII, VIII, IX**************
in1 = tk.Entry(root)
in1.grid(row = 3, column = 1, sticky = "W")

in2 = tk.Entry(root)
in2.grid(row = 3, column = 5, sticky = "W")

in3 = tk.Entry(root)
in3.grid(row = 4, column = 1, sticky = "W")

in4 = tk.Entry(root)
in4.grid(row = 4, column = 5, sticky = "W")

#**************Widget X**************

bu1 = tk.Button(root, text="Input Data", width = 20, height = 5)
bu1.grid(row = 5, column = 3)





root.mainloop()