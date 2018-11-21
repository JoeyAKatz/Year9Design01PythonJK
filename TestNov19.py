#This imports the tkinter "tool box" and contains all support material to make GUI Elements
#By using "as tk" we are giving a short name to use
import tkinter as tk

#main Window
root = tk.Tk()#creates the standard main window


#**************Widget I**************
#3 stages to build elements/objects
#1. Construct object(Build/Configure)
#2. Configure object(Specify behaviors and settings(OPTIONAL))
#3. Pack object(Put in the window)
output = tk.Text(root,height = 50, width = 180) #Parameters(What we send in)
#ordered parameters: The order we send them matters (COMMON)
#named parameters: JavaScript and Pytjon specific
output.config(state = "disable", background = "orange")
output.grid(row = 0, column = 0, rowspan = 5)

#**************Widget II, III, IV**************
labInput1 = tk.Label(root, text = "Input 1", font = "georgia")
labInput1.grid(row = 5, column = 0)

labInput2 = tk.Label(root, text = "Input 2", font = "georgia")
labInput2.grid(row = 6, column = 0)

labInput3 = tk.Label(root, text = "Input 3", font = "georgia")
labInput3.grid(row = 7, column = 0)

#**************Widget V, VI, VII**************
var1 = tk.IntVar()
var2 = tk.IntVar()

cHC = tk.Checkbutton(root, text = "Expand", variable = var1)
cHC.grid(row = 0, column = 1)

cHF = tk.Checkbutton(root, text = "Expand", variable = var2)
cHF.grid(row = 1, column = 1)
#We are writing an EVENT DRIVE PROGRAM
#Build the GUI 
#start it running
#wait for "Event"
root.mainloop()