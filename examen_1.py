import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
def calificar ():
    calif =4
    if opcion_1.get() ==1 or opcion_4.get() == 1:
        calif = calif+2
    if opcion.get() == 1:
        calif = calif +2
    if opcion_2.get() == 1:
        calif = calif +2  
    txt_final = (str) "Tu calificaciones de: "+calif
    mBox.showinfo('Calificacion',txt_final)
    print ("hola")
ventana = tk.Tk()
ventana.geometry('+450+100')
ventana.title("Examen historia de méxico")
ttk.Label(ventana, text="1.- ¿ De que cultura Chichén Itzá fue una poderosa ciudad?").grid(pady = 10,padx = 10,column=0,row=0)
caja_1 = scrolledtext.ScrolledText(ventana, width  = '45', height='3', wrap = tk.WORD)
caja_1.grid(column = 0,row = 1,columnspan=3,padx = 10)
#respuesta maya

ttk.Label(ventana, text="2.- ¿Nombre de México durante la epoca colonial?").grid(pady = 10,padx = 10,column=0,row=2)

caja_2 = scrolledtext.ScrolledText(ventana, width  = '45', height='3', wrap = tk.WORD)
caja_2.grid(column = 0,row = 3,columnspan=3,padx = 10)
#Respuesta Nueva españa
ttk.Label(ventana, text="3.- ¿Año en el que los españoles conquistaron tenochtitlan?").grid(pady = 10,padx = 10,column=0,row=4)
opcion = tk.IntVar()
radio1 = tk.Radiobutton(ventana,text = "1521", variable = opcion, value=1,)
radio1.grid(pady =10,padx=10,column =0, row = 5, sticky = tk.W)
radio1.select()
radio2 = tk.Radiobutton(ventana,text = "2012", variable = opcion, value=3)
radio2.grid(pady =10,padx=10,column =1, row = 5, sticky = tk.W)
radio3 = tk.Radiobutton(ventana,text = "1518", variable = opcion, value=2)
radio3.grid(pady =10,padx=10,column =2, row = 5, sticky = tk.W)

ttk.Label(ventana, text="4.- ¿Nombre del conquistador que derroto al imperio mexica?").grid(pady = 10,padx = 10,column=0,row=6)
opcion_2 = tk.IntVar()
radio4 = tk.Radiobutton(ventana,text = "Cristobal Colon", variable = opcion_2, value=2,)
radio4.grid(pady =10,padx=10,column =0, row = 7, sticky = tk.W)

radio5 = tk.Radiobutton(ventana,text = "Hernán cortéz", variable = opcion_2, value=1)
radio5.grid(pady =10,padx=10,column =1, row = 7, sticky = tk.W)
radio6 = tk.Radiobutton(ventana,text = "Guadalupe Victoria", variable = opcion_2, value=3)
radio6.grid(pady =10,padx=10,column =2, row = 7, sticky = tk.W)
radio4.select()

ttk.Label(ventana, text="5.- ¿Nombre de las naves que llegaron con Cristobal Colon a América?").grid(pady = 10,padx = 10,column=0,row=8)
opcion_1 = tk.IntVar()
casilla_1 = tk.Checkbutton(ventana, text= "La niña", variable = opcion_1)
casilla_1.grid(pady=10,column=0,row=9)
opcion_2 = tk.IntVar()
casilla_2 = tk.Checkbutton(ventana, text = "La maría", variable = opcion_2)
casilla_2.grid(pady = 10,column=1, row =9,sticky=tk.W)

opcion_3 = tk.IntVar()
casilla_3 = tk.Checkbutton(ventana,text= "El arca", variable = opcion_3)
casilla_3.grid(pady=10,column=2,row=9,sticky = tk.W)

opcion_4 = tk.IntVar()
casilla_4 = tk.Checkbutton(ventana,text= "la pinta", variable = opcion_4)
casilla_4.grid(pady=10,column=0,row=10,sticky = tk.W)
opcion_5 = tk.IntVar()
casilla_5 = tk.Checkbutton(ventana,text= "Teresita", variable = opcion_5)
casilla_5.grid(pady=10,column=1,row=10,sticky = tk.W)

accion = tk.Button(ventana, text = "Calificar",command = calificar)
accion.grid(pady = 10,column=2,row=11)

ventana.mainloop()


