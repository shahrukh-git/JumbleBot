import tkinter
from tkinter import *
from tkinter import messagebox
import random 
from random import shuffle

answers = ["Afghanistan", "Albania",  "Algeria", "Andorra", "Angola", "Antigua", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",
          'Iceland', 'India' 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Turkey', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand' 
          'Kuwait', 'Kyrgyzstan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea', 'Kosovo', 'Romania', 'Russia', 'Rwanda', 'Qatar', 'Oman', 'Nepal']
questions = []

for i in answers:
    words = list(i)
    shuffle(words)
    questions.append(words)

num = random.randint(0, len(questions)-1)

def initial():
    global questions, num
    label1.configure(text=questions[num])

def answerscheck():
    global questions, num, answers
    userinput = entry1.get()
    if userinput == answers[num]:
        messagebox.showinfo('Success','Your Answer is correct') 
    else:
        messagebox.showinfo('Error','Your Answer is wrong') 
        entry1.delete(0,END) 

def resetswitch():
    global questions, answers, num
    num = random.randint(0, len(questions)-1)
    label1.configure(text=questions[num])
    entry1.delete(0,END)

window = Tk()
window.geometry("400x400+500+200")
window.resizable(0,0)
window.configure(background = '#2C3335')
window.title('jumbleBot')
window.iconbitmap(r'icon.ico')

label1 = Label(window, font='times 20', bg='#2C3335', fg='#DAE0E2')
label1.pack(pady=30, ipady=10, ipadx=10)

answer = StringVar()
entry1 = Entry(window, textvariable=answer)
entry1.pack(ipady=5, ipadx=5)

button1 = Button(window, text='Check', bg='#75DA8B', width=20, command=answerscheck)
button1.pack(pady=40)

button2 = Button(window, text='Reset', bg='#EA425C', width=20, command=resetswitch)
button2.pack()

initial()
window.mainloop()

