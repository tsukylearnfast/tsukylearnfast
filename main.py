
from tkinter import *

def warning():
    askokcancel("Confirm",'Are you sure')#Confirmation

def getentry():
    keepedinput = input.get()
    if keepedinput == "":
        askokcancel("Error","Error STR_______VOID")
    else:
        label_welcome.configure(text = 'Welcome '+ keepedinput)
        input.destroy()
        label.destroy()
        quit_button.destroy()
        comfirm_button.destroy()



###############################################################

window = Tk()
window.title("Fortnite SoftAim")
window.geometry('800x800')



label = Label(window, text = 'Kroom AimV3',fg = 'sky blue', font =("Rockstar Extra Bold",30))#Titlle
label.pack()

quit_button = Button(window , width=30,text = 'Leave',fg = "black" , command = window.destroy)#Bouton quittez 
quit_button.pack(side = BOTTOM)

input = Entry(window,width=30)#Saisie de text
input.focus()
input.pack()


label_welcome = Label(window, text = '',fg = 'black', font =("Bebas Neue",30))#Label qui va etre edit par keeped input
label_welcome.pack()


comfirm_button = Button(window,text = 'Confirm',bg ='sky blue',command= getentry)#Confirmation de id
comfirm_button.pack()


window.mainloop()   

