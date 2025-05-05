from tkinter import *
import pandas as pd 

window=Tk()
window.geometry("640x640")
info=""
# w = Scrollbar ( window)
time=Label(window,text="time")
act=Label(window,text="activity")
time.grid(row=0,column=0)
act.grid(row=0,column=1)
textboxes=[]
for i in range(1, 12):  # Iterate from 1 to 12
    label = Label(window, text=f"{i} a.m.")  # Create a Label
    label.grid(row=i , column=0)  # Position it in the grid
    text1=Text(window,width=30,height=1) 
    text1.grid(row=i,column=1)
    textboxes.append(text1)
    

def submit():
    with open("C:/Users/adity/OneDrive/Desktop/tanista/tanishaclass/todo.txt", "w") as myfile:    
        for i in range(25):

            info=textboxes[i].get("1.0",END)
            myfile.write(f"{i+1}:{info}\n")
        print(f"{i},{info}\n")
        
for i in range(13, 24):  # Iterate from 1 to 12
    label2 = Label(window, text=f"{i-12} p.m.")  # Create a Label
    label2.grid(row=i , column=0)  # Position it in the grid
    text2=Text(window,width=30,height=1) 
    text2.grid(row=i,column=1)
    textboxes.append(text2)
            

         
            
submitbtn = Button(window, text="Submit All", width=20, height=2, command=submit)
submitbtn.grid(row=5, column=3, pady=10)
    # file=("C:/Users/adity/OneDrive/Desktop/tanista/tanishaclass/todo.txt","r")
            
            
    
    
label2=Label(window,text=f"12 noon.")
label2.grid(row=12,column=0)
for j in range(13,24):
    label3=Label(window,text=f"{j-12} p.m.")
    label3.grid(row=j,column=0)
label4=Label(window,text=f"12 midnight.")
label4.grid(row=25,column=0)
text=Text(window,width=30,height=1) 
submitbtn = Button(window, text="Submit All", width=20, height=2, command=submit)
submitbtn.grid(row=5, column=3, pady=10)
# for k in range(1,12):

#     def submit():

#         info=text.get("1.0",END)
#         print(info)
#         print(type(info))
#         with open("C:/Users/adity/OneDrive/Desktop/tanista/tanishaclass/todo.txt", "w") as myfile:
#             myfile.write(info)
        

    # text=Text(window,width=30,height=1) 
    
    # submitbtn=Button(window,text="Submit",width=15,height=1,command=submit)
    # file=("C:/Users/adity/OneDrive/Desktop/tanista/tanishaclass/todo.txt","r")
    
    # text.grid(row=k,column=1)
    # submitbtn.grid(row=k,column=2)
    


window.mainloop()