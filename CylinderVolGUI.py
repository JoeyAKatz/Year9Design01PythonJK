import tkinter as tk

root = tk.Tk()
root.title("volume of a Cylinder")

labr = tk.Label(root, text="Radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="Height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit")
btn.pack()

output = tk.Text(root, width=200, height=40, borderwidth=12, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()




root.mainloop()
