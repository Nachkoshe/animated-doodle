from tkinter import *
from keyboard import press

root=Tk()

# output text area
txt= Text(root)
txt.grid(row=0, column=0, columnspan=5)
txt.configure(background="light green")

# send.
def send ():
    send = "you : " + e.get()
    txt.insert(END,"\n"+ send )

    if (e.get()== "hello"):
            txt.insert(END, "\n" + "Bot: hi, welcome to fynd academy")
            txt.insert(END, "\n" + "Bot: hello, welcome to fynd academy")
            txt.insert(END, "\n" + "Build smart coding skills in 10-weeks at Fynd Academy")
            txt.insert(END, "\n" + "following are the courses offered !!")
            txt.insert(END, "\n" + "select amongst following running courses to know start dates!")
            txt.insert(END, "\n" + "python backend development= 0")
            txt.insert(END, "\n" + "Full stack development= 1")


    elif(e.get() == "hii"):
            txt.insert(END, "\n" + "Bot: hello, welcome to fynd academy")
            txt.insert(END, "\n" + "Build smart coding skills in 10-weeks at Fynd Academy")
            txt.insert(END, "\n" + "following are the courses offered !!")
            txt.insert(END, "\n" + "select amongst following running courses to know start dates!")
            txt.insert(END, "\n" + "python backend development= 0")
            txt.insert(END, "\n" + "Full stack development= 1")
    elif (e.get() == "0"):
            txt.insert(END, "\n" + "Bot: python backend development course will be starting from 25th nov 2021")
    elif (e.get() == "1"):
            txt.insert(END, "\n" + "Bot: full stack development course will be starting from 26th nov 2021")

    else:
        txt.insert(END, "\n" + "Bot: sorry i didnt get it")
        txt.insert(END, "\n" + "Bot: for more details visit 'www.fynd.academy'")
        txt.insert(END, "\n" + "Bot: thank you for contacting us, have a nice dat!!")
    
    e.delete(0,END)
    
# input message area
e = Entry(root,width=100)
e.grid(row=1, column=0)
e.configure(background= "white")


#SEND MESSAGE BUTTON
# send = press('enter')
send = Button( root, text="send", command= send)
send.grid(row=1, column=1)
send.configure(background= "yellow")


# title for the chatbot

root.title("CHATBOT")

root.mainloop()


