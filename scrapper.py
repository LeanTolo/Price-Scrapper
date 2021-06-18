from tkinter import *

from EbayScraper import EbayBot
from AmazonScraper import AmazonBot
from MercadoLibre_bot import MeliBot

from bs4 import BeautifulSoup

def EbayFunc():
    if (entrada.get() != ""):
        EbayScraper = EbayBot.main(entrada.get())
        etiquetaAlerta = Label(text="Gracias por usar nuestros Servicios").place(x=170,y=250)
    else:
        etiquetaAlerta = Label(text="Ingrese Lo Que Desea Scrapear Por Favor O Sera Hackeado").place(x=170,y=250)
    
def AmazonFunc():
    if (entrada.get() != ""):
        AmazonScraper = AmazonBot.main(entrada.get())
        etiquetaAlerta = Label(text="Gracias por usar nuestros Servicios").place(x=170,y=250)
    else:
        etiquetaAlerta = Label(text="Ingrese Lo Que Desea Scrapear Por Favor O Sera Hackeado").place(x=170,y=250)

def MeliFunc():
    if (entrada.get() != ""):
        MeliScraper = MeliBot.main(entrada.get())
        etiquetaAlerta = Label(text="Gracias por usar nuestros Servicios").place(x=170,y=250)
    else:
        etiquetaAlerta = Label(text="Ingrese Lo Que Desea Scrapear Por Favor O Sera Hackeado").place(x=170,y=250)

raiz = Tk()

raiz.title("Scrapper")

raiz.resizable(False,False)

#raiz.iconbitmap("icon.ico")

raiz.geometry("650x350")

raiz.config(bg="darkgreen")

ventana = Frame(height=650,width=350)
ventana.pack(padx=20,pady=20)

etiqueta = Label(text="Ingrese Lo Que Desea Scrapear: ",font=("Verdana",10)).place(x=210,y=50)

entrada = StringVar()
campo = Entry(ventana,textvariable=entrada).place(x=120,y=60)

boton1 = Button(ventana,command=EbayFunc,text="Ebay").place(x=160,y=90)
boton2 = Button(ventana,command=AmazonFunc,text="Amazon").place(x=150,y=120)
boton3 = Button(ventana,command=MeliFunc,text="Meli(ARG)").place(x=146,y=150)



raiz.mainloop()
