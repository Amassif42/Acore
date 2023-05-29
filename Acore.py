import os
import openai
import xerox
import webbrowser

from tkinter import *

######################
#se que va faire le programe
pdfs = "Corrige les fautes d'orthographe de se texte en français :\n\n"
action = "Corrige"
######################

#couleur du fond
fond='white'

#info fenètre 1
master = Tk()
master.title("Acore")
master.geometry("350x428")#350x435
master.minsize(350, 428)
master.iconbitmap("logo.ico")
master.config(background= fond)

#création des frame
box1 = Frame(master, bg=fond)
box1.pack()
box2 = Frame(master, bg=fond)
box2.pack()
box3 = Frame(master, bg=fond)
box3.pack()
box4 = Frame(master, bg=fond)
box4.pack()
box5 = Frame(master, bg=fond)
box5.pack()


#action bouton coriger
def Action():
    #recupération clée API
    with open("API_key.txt", "r+") as file:
        api_key=file.readline().rstrip()
        openai.api_key = api_key
        file.close
    #recuperation texte input
    input_var = input.get(1.0, END)
    request = pdfs + input_var
    output.delete(1.0,END),
    #truc api
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=request,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    #encoyer la réponse
    print(response)
    data_out = response["choices"]
    for key_file in data_out:
        data = key_file["text"]
    datastrip = data.strip()
    output.insert(END, datastrip)
    print("------- Demande :")
    print(request)
    print("------- Resultat :")
    print(datastrip)

#action bouton copier
def copy():
    input_var = output.get(1.0, END)
    outputstrip = input_var.strip()
    xerox.copy(outputstrip),

#action bouton clear
def clear():
    input.delete(1.0,END)
    output.delete(1.0,END),

def urlkey():
    webbrowser.open("https://bit.ly/AcoreAPI")

#paramétre de key
def fkey():
    #fenètre d'info
    info = Toplevel(master)
    info.title("Fonctionnement")
    info.geometry("300x50")
    info.minsize(100, 75)
    info.iconbitmap("logo.ico")
    info.config(background= fond)
    #feunétre d'entrer de key
    def keyset():
        info.destroy()
        key = Toplevel(master)
        key.title("Acore key")
        key.geometry("255x130")
        key.minsize(100, 75)
        key.iconbitmap("logo.ico")
        key.config(background= fond)
        #enregisstre la key
        def savekey():
            print(key_input.get(1.0, END))
            keyfile = open('API_key.txt', 'w')
            keyfile.write(key_input.get(1.0, END))
            keyfile.close
            key.destroy()

        #bonton url 
        button_keyurl = Button(key, text="Clée API :\n https://beta.openai.com/account/api-keys", command=urlkey ,bg='white',fg='black')
        button_keyurl.pack()
        #texte d'info
        title_key = Label(key, text="Entrer votre API keys gpt3",bg=fond)
        title_key.pack()
        #entrer de texte
        key_input=Text(key, bg='#F2F3F5',width=30, height = 2)
        key_input.pack()
        #bouton enregisstre
        button_save_key = Button(key, text="Enregisstre", command=savekey ,bg='white',fg='black')
        button_save_key.pack()

        key.mainloop()
    #ifno
    txt = Label(info, bg='#F2F3F5', text="Pour fontionner Acore utilise l'API de GPT3\n il faut donc une clée API GPT3")
    txt.pack()
    #ok& info
    ok = Button(info, text="OK& ✅", command=keyset ,bg='white',fg='black')
    ok.pack()

    info.mainloop()

def Amassif_twitter():
    webbrowser.open("https://bit.ly/twitterAmassif")

#remplissage honteux
rempl = Label(box1, text="clée d'API", bg=fond, fg=fond)
rempl.pack(side = LEFT)


#image titre Acore
canvas = Canvas(box1, width = 125, height = 50,bg=fond, )      
canvas.pack(side = LEFT, padx = 35)
img = PhotoImage(file="acore_title.png")      
canvas.create_image(10,10, anchor=NW, image=img)

#bouton clée API
APIboutn = Button(box1, text="clée d'API", command=fkey,bg='white',fg='black')
APIboutn.pack(side = BOTTOM)


#zone de texte 1
input = Text(box2, height=10, width=40,bg='#F2F3F5')
input.pack()

#bouton corriger
getTextArea = Button(box3, text= action, command=Action,bg='white',fg='black')
getTextArea.pack(side = LEFT)

#bouton copier
getTextArea = Button(box3, text="Copier", command=copy,bg='white',fg='black')
getTextArea.pack(side= LEFT)

#bouton clear
getTextArea = Button(box3, text="X", command=clear,bg='red',fg='black')
getTextArea.pack(side = LEFT)

#zone de texte 2
output = Text(box4, height=10, width=40,bg='#F2F3F5')
output.pack()

#crédit
fait_par = Label(box5,text="Créer par",fg='black',bg=fond)
fait_par.pack(side=LEFT)

Amassif = Button(box5,text="Amassif",fg='#017AC1',bg=fond,command=Amassif_twitter,border=NO)
Amassif.pack(side=BOTTOM)

master.mainloop()

