#import GUI library
import tkinter
from tkinter import font
from  tkinter import *
from random import choice as ranChoice
from PIL import ImageTk,Image

#create a frame to store the GUI
ssGui = Tk(className = "Secret Santa Selector")

welcomeList = ['Shane', 'Maura', "Devin", "Connor", 'Molly', 'Ryan', "Maurina"]
choice2 = []
def create_new_frame(ssGui):
    #create the frame thats called with this function
    frame = Frame(ssGui, bg='#00873E', highlightbackground="#c54245", highlightthickness=20)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)

    '''treeImg = Image.open("christmas.jpg")
    test = ImageTk.PhotoImage(treeImg)
    label4 = Label(frame, image=test, borderwidth=0, highlightthickness=0, anchor=SE)
    label4.image = test
    label4.grid(column=1,row=3)
    '''


    # create a welcome message store all the siblings in it, make the message custom welcome each person in
    #choice = ranChoice(welcomeList)
    welcomeVar = StringVar()
    l1 = Label(frame, textvariable=welcomeVar, fg='black', bg='#c54245', font="Bold", relief=RIDGE, bd=1, padx=20, pady=20 )
    l1.grid(column=1, row=0, sticky=tkinter.NS, padx=20, pady=20)
    welcomeVar.set("Welcome " + welcomeList[0] + "\n Please select the Secret Santa Button to select your gift receipt")
    #l1.pack(side='top', expand="True")

    #Create a button (select secret santa), make sure to use a grid that can set the absolute position,
    #this button will be used to select a value from a list/array and then remove the selected value
    ssIVar = StringVar()
    ssButton = Button(frame, textvariable=ssIVar, fg="black", bg="#c54245", font="48", command = onClick)
    ssButton.grid(column=1, row=2, sticky=tkinter.W, padx=5, pady=5)
    ssIVar.set('Press to select your Secret Santa')
    #ssButton.pack(side='left', expand="True")

    # create a button to refresh the program (the next user button)
    nextButton = Button(frame, text='Click for next person', fg="black", bg="#c54245", font="48", command = clearAll)
    nextButton.grid(column=1, row=2, sticky=tkinter.E, padx=5, pady=5)
    #nextButton.pack(side='right', expand="True")
    #return value for the frame
    return frame

#-----------------------------------------------------------------------------------------------------------------#
ssList = ['Shane', 'Maura', "Devin", "Connor", 'Molly', 'Ryan', "Maurina"]
def onClick():
    choice2 = ranChoice(ssList)
    if welcomeList[0] == choice2:
        ssVar = StringVar()
        l5 = Label(frame, textvariable=ssVar, fg='black', bg='#c54245', font="60")
        l5.grid(column=1, row=3, padx=5, pady=5)
        ssVar.set('Try again Your Cant get youself '+ welcomeList[0] + " (:")
    else:
        ssVar = StringVar()
        l2 = Label(frame, textvariable=ssVar, fg='black', bg='#c54245', font="60")
        l2.grid(column=1, row=3, padx=5, pady=5)
        ssVar.set('Your Secret Santa is: ' + choice2 +'!')
        ssList.remove(choice2)

        #l2.pack(side='bottom', expand="True")

def clearAll():
    global frame
    frame.destroy()
    welcomeList.remove(welcomeList[0])
    frame = create_new_frame(ssGui)
    frame.pack(fill='both', expand="True")

#create an event loop so that the application updates
frame = create_new_frame(ssGui)
frame.pack(fill='both', expand="True")
print(font.families())
ssGui.mainloop()