from Tkinter import *

root = Tk()

photo = PhotoImage(file= r"a.gif")
w = Label(root, text="Hello, world!")
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())

canvas = Canvas(root) #, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(side='top', fill='both', expand='True') 
canvas.create_image(0, 0, image=photo, anchor='nw')

w.pack()

root.mainloop()

