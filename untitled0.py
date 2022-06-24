from tkinter import *

root=Tk()

root.geometry("400x400")

root.title("FIBONACCI")

root.configure(bg="lightblue")

label_series = Label(root, text="Fibonacci series: ", bg="lightblue")
label_sum = Label(root,bg="lightblue")

inputbox=Entry(root)
inputbox.place(relx=0.5,rely=0.5,anchor=CENTER)

def Fibonacci():
    num = int(inputbox.get())
    first_no = 0
    second_no = 1
    sum = 0
    s = 0
    counter = 1
    while (counter<= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1 
        first_no = second_no
        second_no = sum
        s = s + sum
        sum = first_no + second_no
        label_sum["text"]="sum is " + str(s)
        
        
btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
label_series.place(relx=0.5,rely=0.3,anchor=CENTER)
label_sum.place(relx=0.5,rely=0.7,anchor=CENTER)







root.mainloop()
