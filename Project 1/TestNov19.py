#This imports the tkinter "tool box" and contains all support material to make GUI Elements
#By using "as tk" we are giving a short name to use
import tkinter as tk

#main Window
root = tk.Tk()#creates the standard main window

#3 stages to build elements/objects
#1. Construct object(Build/Configure)
#2. Configure object(Specify behaviors and settings(OPTIONAL))
#3. Pack object(Put in the window)
output = tk.Tect(root,height = 10, width = 30) #Parameters(What we send in)

#We are writing an EVENT DRIVE PROGRAM
#Build the GUI 
#start it running
#wait for "Event"
root.mainloop()