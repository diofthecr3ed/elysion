#Import the required Libraries
from tkinter import *
from tkinter import ttk
import addrec

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x550")

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)


def master_9():
   global entry
   string = entry.get()
   var1 = addrec.reformat(string)
   addrec.grade9(var1)

def master_11():
   global entry2
   string = entry2.get()
   var1 = addrec.reformat(string)
   addrec.grade11(var1)

def master_12():
   global entry3
   string = entry3.get()
   var1 = addrec.reformat(string)
   addrec.grade12(var1)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

label2=Label(win, text="Grade 9", font=("Courier 22 bold"))
label2.pack()
#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()
entry.insert(0, "<Enter register filepath>")

ttk.Button(win, text= "Generate Transcripts",width= 20, command=master_9).pack(pady=20)


label3=Label(win, text="Grade 11", font=("Courier 22 bold"))
label3.pack()

entry2= Entry(win, width= 40)
entry2.focus_set()
entry2.pack()
entry2.insert(0, "<Enter register filepath>")

ttk.Button(win, text= "Generate Transcripts",width= 20, command=master_11).pack(pady=20)


label4=Label(win, text="Grade 12", font=("Courier 22 bold"))
label4.pack()
entry3= Entry(win, width= 40)
entry3.focus_set()
entry3.pack()
entry3.insert(0, "<Enter register filepath>")
ttk.Button(win, text= "Generate Transcripts",width= 20, command=master_12).pack(pady=20)



#exit button doesn't work yet, use code editor stop button to stop
exit_button = Button(win, text="Exit", command=win.destroy)
exit_button.pack(pady=20)
win.mainloop()