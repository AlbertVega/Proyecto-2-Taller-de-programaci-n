from tkinter import *
import pygame, random
import time

def StartingWindow():
    #------------------------------------------------------------------------------------------------------
    # STARTING WINDOW
    #------------------------------------------------------------------------------------------------------
    window = Tk()
    window.title("The Fish Adventure")

    # WINDOW DIMENTIONS
    window.geometry("900x700")

    # BACKGROUND
    image = PhotoImage(file = "PNG/Start Background.png")
    background = Label(image = image)
    background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    # LABEL "CREA UN NOMBRE"
    commentary = Label(window, text = "Crea Un Nombre ", font = ("Ebrima",22))
    commentary.place(x = 335, y = 390 )

    # LABEL "SELECCIONA UN NIVEL"
    selectLevel = Label(window, text = "Selecciona Un Nivel ", font = ("Ebrima",15))
    selectLevel.place(x = 700, y = 320 )

    # TEXT BOX
    entry = StringVar
    text_box = Entry(window, textvariable = entry, font = ("Ebrima",18))
    text_box.place(x = 355, y = 450, height = 30, width = 200)

    def GameWindow():
        # GET THE NAME INTRODUCED
        Playername = text_box.get()
        # CLOSE THE STARTING WINDOW
        window.destroy()

    # BUTTON "EMPEZAR"
    StartButton = Button(window, text = "Empezar", height = 1, width = 10, command = GameWindow, font = ("Ebrima",17))
    StartButton.place(x = 385, y = 500)

    # LEVEL 1 RADIOBUTTON
    num = IntVar()
    levelOne = Radiobutton(window, text = "Nivel 1",value = 1, variable = num, font = ("Ebrima",17))
    levelOne.place(x = 737, y = 390)

    # LEVEL 2 RADIOBUTTON
    levelTwo = Radiobutton(window, text = "Nivel 2", value = 2 , variable = num, font = ("Ebrima",17))
    levelTwo.place(x = 737, y = 450)

    # LEVEL 2 RADIOBUTTON
    levelThree = Radiobutton(window, text = "Nivel 3", value = 3, variable = num, font = ("Ebrima",17))
    levelThree.place(x = 737, y = 510)
    #------------------------------------------------------------------------------------------------------
    # ABOUT WINDOW
    #------------------------------------------------------------------------------------------------------
    def AboutWindow():
        Aboutwindow = Toplevel()
        Aboutwindow.title("The Fish Adventure")

        # WINDOW DIMENTIONS
        Aboutwindow.geometry("900x700")

        # BACKGROUND
        image = PhotoImage(file = "PNG/About Background.png")
        background = Label(Aboutwindow, image = image)
        background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # PRODUCTION COUNTRY LABEL
        Country = Label(Aboutwindow, text = "Costa Rica", font = ("Ebrima",20))
        Country.place(x = 390, y = 50)

        # UNIVERSITY LABEL
        University = Label(Aboutwindow, text = "instituto Tecnológico de Costa Rica (TEC)", font = ("Ebrima",20))
        University.place(x = 210, y = 120)

        # CARRER LABEL
        Carrer = Label(Aboutwindow, text = "Ingeniería en Computadores", font = ("Ebrima",20))
        Carrer.place(x = 280, y = 190)

        # SIGNATURE LABEL
        SignatureYearGroup = Label(Aboutwindow, text = "Taller de Programación 2021 Grupo 03", font = ("Ebrima",20))
        SignatureYearGroup.place(x = 225, y = 260)

        # PROFESSOR LABEL
        Professor = Label(Aboutwindow, text = "Leonardo Araya Martínez", font = ("Ebrima",20))
        Professor.place(x = 305, y = 330)

        # VERSION LABEL
        Version = Label(Aboutwindow, text = "Python 3.9.4", font = ("Ebrima",20))
        Version.place(x = 375, y = 400)
        
        # AUTHORS LABELS
        Authors = Label(Aboutwindow, text = "Creado por:", font = ("Ebrima",20))
        Authors.place(x = 377, y = 470)

        Author1 = Label(Aboutwindow, text = "Albert Vega Camacho", font = ("Ebrima",20))
        Author1.place(x = 325, y = 540)

        Author2 = Label(Aboutwindow, text = "Meibel Ceciliano Picado", font = ("Ebrima",20))
        Author2.place(x = 312, y = 610)

        mainloop()

    # ABOUT BUTTON
    AboutButton = Button(window, text = "About", command = AboutWindow, font = ("Ebrima 15"))
    AboutButton.place(x = 100, y = 315)

    mainloop()

StartingWindow()