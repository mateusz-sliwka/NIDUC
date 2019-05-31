import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import transmitter
import numpy as np
from random import shuffle
from tkinter.filedialog import askopenfilename


class sender:
    def __init__(self):
        window = tk.Tk()
        window.title("Nadawca sygnału")
        window.geometry("600x490")

        def showoptions(): #pokazanie inputow na wlasciwosci generowanego obrazu
            data = IntVar()
            data2 = IntVar()
            entry1 = Entry(frame, width=5, textvariable=data)
            entry1.grid(row=0, column=0, sticky=tk.NW)
            text1 = Label(frame, text="Długośc boku obrazu (px)")
            text1.grid(row=0, column=1)
            entry2 = Entry(frame, width=5, textvariable=data2)
            entry2.grid(row=1, column=0, sticky=tk.NW)
            text2 = Label(frame, text="Liczba czarnych pikseli")
            text2.grid(row=1, column=1, sticky=tk.NW)
            generuj = Button(frame, text="Generuj obrazek", command=lambda: generateimg(data.get(), data2.get()))
            generuj.grid(row=2, column=1, sticky=tk.NW)
            frame.grid(row=3, column=0, sticky=tk.NW)

        def nooptions(): #schowanie inputow na wlasciwosci generowanego obrazu
            frame.grid_forget()

        def imgfromfile(): #wczytanie obrazu z pliku
            nooptions()
            filename = askopenfilename(initialdir="/", title="Select file")
            image = Image.open(filename).resize((250, 250))
            image = image.convert('1')
            photo = ImageTk.PhotoImage(image)
            global lab
            lab = Label(frame6, image=photo, borderwidth=2, relief="groove")
            lab.image = photo
            lab.grid(column=0, row=2, sticky=tk.N)
            img = Image.open(filename).convert('1')
            np_img = np.array(img)

            tabela = []
            y=0
            for x in np.nditer(np_img):
                tabela.append(x)
                y=y+1

            print(type(np_img))
            print(np_img.shape)
            print(np_img.size)
            print("po")
            print(type(tabela))
            print(len(tabela))

            global signal
            signal = tabela

        def coloredimg(): #generowanie jednolitego obrazu
            nooptions()
            value = []
            for i in range(250 * 250):
                value.append(0)
            global signal
            signal = value.copy()
            plt.imsave('colored_img.png', np.array(value).reshape(250, 250), cmap=cm.gray)
            image = Image.open("colored_img.png").resize((250, 250), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            lab = Label(frame6, image=photo, borderwidth=2, relief="groove")
            lab.image = photo
            lab.grid(column=0, row=2, sticky=tk.N)

        def generateimg(first, second): #generowanie obrazu o danym rozmiarze i ilosci czarnych pikseli
            value = []
            kontrolka = second
            for i in range (first * first):
                if (kontrolka > 0):
                    value.append(0)
                    kontrolka -= 1
                else:
                    value.append(1)

            shuffle(value)
            global signal
            signal = value.copy()
            plt.imsave('temp_img.png', np.array(value).reshape(first, first), cmap=cm.gray)
            image = Image.open("temp_img.png").resize((250, 250))
            photo = ImageTk.PhotoImage(image)
            global lab
            lab = Label(frame6, image=photo, borderwidth=2, relief="groove")
            lab.image = photo
            lab.grid(column=0, row=2, sticky=tk.N)

        def send(algorytm): #przeslanie obrazu z programu nadawczego do kanalu transmisyjnego
            print("=====WYSYLKA SYGNALU Z PROGRAMU NADAWCZEGO====")
            print("Sygnal do scramblingu: ")
            print(signal)
            print("O dlugosci: " + str(len(signal)))
            if (algorytm.get() == 0):
                print("Algorytm scramblowania: B8ZS")
                algo = "B8ZS"
            if (algorytm.get() == 1):
                algo = "HDB3"
                print("Algorytm scramblowania: HDB3")
            if(algorytm.get()==2):
                algo="AES"
                print("Algorytm scramblowania: AES")
            print("=====================")
            window.destroy()
            transmitter.transmitter(signal,algo)

        frame4 = tk.Frame()
        version = tk.Label(frame4, text="Scrambler sender v0.0", fg="grey", width=30, anchor="w")
        version.grid(row=0, column=0, sticky=tk.NW)

        author = tk.Label(frame4, text="Karasek, Kamieniecki, Śliwka", fg="grey", anchor="e", width=30)
        author.grid(row=0, column=1, sticky=tk.NW)

        lab1 = tk.Label(frame4, text="Podgląd obrazu", fg="black", width=28, anchor="center",
                        font=('Verdana', 15, 'bold'))
        lab1.grid(row=1, column=0)

        lab2 = tk.Label(frame4, text="Zródło obrazu: ", fg="black", width=30, anchor="w", font=('Verdana', 15, 'bold'))
        lab2.grid(row=1, column=1, pady=20)
        zrodlo = IntVar()
        algorytm = IntVar()

        frame2 = tk.Frame(frame4)
        frame = tk.Frame(frame2)
        button1 = tk.Radiobutton(frame2, text="Obraz z pliku", variable=zrodlo, value=1, anchor="w",
                                 command=lambda: imgfromfile(),
                                 height=2)
        button1.grid(row=1, column=0, sticky=tk.NW)
        button2 = tk.Radiobutton(frame2, text="Obraz jednokolorowy", variable=zrodlo, value=0, anchor="w",
                                 command=lambda: coloredimg(),
                                 height=2)
        button2.grid(row=0, column=0, sticky=tk.NW)
        button3 = tk.Radiobutton(frame2, text="Generuj obraz", variable=zrodlo, value=2, anchor="w",
                                 command=showoptions,
                                 height=2)
        button3.grid(row=2, column=0, sticky=tk.NW)

        labka = tk.Label(frame2, text="Rodzaj scramblingu: ", fg="black", width=30, anchor="w",
                         font=('Verdana', 15, 'bold'))
        labka.grid(row=7, column=0, sticky=tk.NW, pady=20)
        button11 = tk.Radiobutton(frame2, text="B8ZS", variable=algorytm, value=0, anchor="w", height=2)
        button11.grid(row=8, column=0, sticky=tk.NW)
        button12 = tk.Radiobutton(frame2, text="HDB3", variable=algorytm, value=1, anchor="w", height=2)
        button12.grid(row=9, column=0, sticky=tk.NW)
        button12 = tk.Radiobutton(frame2, text="AES", variable=algorytm, value=2, anchor="w", height=2)
        button12.grid(row=10, column=0, sticky=tk.NW)
        button13 = tk.Button(frame2, text="Wyślij", height=3, width=15, fg="#FFFFFF", highlightbackground="#000000",
                             command=lambda: send(algorytm))
        button13.grid(row=11, column=0, sticky=tk.SW, pady=20)
        frame2.grid(column=1, row=2)
        frame6 = tk.Frame(frame4)
        coloredimg()
        frame5 = tk.Frame(frame6)

        frame5.grid(column=0, row=3, pady=10, sticky=tk.N)
        frame6.grid(column=0, row=2, sticky=tk.N)
        frame4.grid(column=0, row=0, sticky=tk.N)

        frame3 = tk.Frame()

        frame3.grid(column=0, row=1)

        window.mainloop()
