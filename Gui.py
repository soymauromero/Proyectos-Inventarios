import tkinter

Ventana = tkinter.Tk()
Ventana.geometry("1200x570")

#Etiquetas

etiqueta = tkinter.Label(Ventana, text = "Proyecto Inventarios")
etiqueta.pack()

Eti1 = tkinter.Label(Ventana, text= "Costo de Adquisicion",bg= "blue")
Eti1.place(x=10,y=20,width=350,height=30)

Eti2 = tkinter.Label(Ventana, text= "Costo Mantener Inventarios",bg= "blue")
Eti2.place(x=10,y=60,width=350,height=30)

Eti3 = tkinter.Label(Ventana, text= "Costo de mantener inventarios",bg= "blue")
Eti3.place(x=10,y=100,width=350,height=30)

Eti4 = tkinter.Label(Ventana, text= "Costo Debido Al faltante",bg= "blue")
Eti4.place(x=10,y=140,width=350,height=30)

Eti5 = tkinter.Label(Ventana, text= "Costo de Operacion",bg= "blue")
Eti5.place(x=10,y=180,width=350,height=30)

Eti6 = tkinter.Label(Ventana, text= "Tiempo Despues de nivelar productos pendiente",bg= "blue")
Eti6.place(x=10,y=220,width=350,height=30)

Eti7 = tkinter.Label(Ventana, text= "Tiempo desde el imax a 0",bg= "blue")
Eti7.place(x=10,y=260,width=350,height=30)

Eti8 = tkinter.Label(Ventana, text= "Tiempo acumulacion de faltantes",bg= "blue")
Eti8.place(x=10,y=300,width=350,height=30)

Eti9 = tkinter.Label(Ventana, text= "Tiempo de puesta en marcha hasta nivelar los faltantes ",bg= "blue")
Eti9.place(x=10,y=340,width=350,height=30)

Eti10 = tkinter.Label(Ventana, text= "Inventario Maximo",bg= "blue")
Eti10.place(x=10,y=380,width=350,height=30)

Eti11 = tkinter.Label(Ventana, text= "Tasa de Produccion",bg= "blue")
Eti11.place(x=10,y=420,width=350,height=30)

Eti12 = tkinter.Label(Ventana, text= "Tasa de Demanda",bg= "blue")
Eti12.place(x=10,y=460,width=350,height=30)



#Cuadros texto

cu = tkinter.Entry(Ventana,bg= "blue")
cu.place(x=370,y=20,width=100,height=30)

cp = tkinter.Entry(Ventana,bg= "blue")
cp.place(x=370,y=60,width=100,height=30)

cmi = tkinter.Entry(Ventana,bg= "blue")
cmi.place(x=370,y=100,width=100,height=30)

cf = tkinter.Entry(Ventana,bg= "blue")
cf.place(x=370,y=140,width=100,height=30)

cop = tkinter.Entry(Ventana,bg= "blue")
cop.place(x=370,y=180,width=100,height=30)

t1 = tkinter.Entry(Ventana,bg= "blue")
t1.place(x=370,y=220,width=100,height=30)

t2 = tkinter.Entry(Ventana,bg= "blue")
t2.place(x=370,y=260,width=100,height=30)

t3 = tkinter.Entry(Ventana,bg= "blue")
t3.place(x=370,y=300,width=100,height=30)

t4 = tkinter.Entry(Ventana,bg= "blue")
t4.place(x=370,y=340,width=100,height=30)

imax = tkinter.Entry(Ventana,bg= "blue")
imax.place(x=370,y=380,width=100,height=30)

r = tkinter.Entry(Ventana,bg= "blue")
r.place(x=370,y=420,width=100,height=30)

d = tkinter.Entry(Ventana,bg= "blue")
d.place(x=370,y=460,width=100,height=30)

calcular = tkinter.Button(Ventana, text="Calcular", command=True,bg="Blue")
calcular.place(x=10,y=510,width=220,height=50)

limpiar = tkinter.Button(Ventana, text="Limpiar", command=True,bg="Blue")
limpiar.place(x=250,y=510,width=220,height=50)

EOQ1 = tkinter.Frame(Ventana,bg="yellow")
EOQ1.place(x=480, y=20, width=350,height=265)


EOQ2 = tkinter.Frame(Ventana,bg="yellow")
EOQ2.place(x=840, y=20, width=350,height=265)

LEP1 = tkinter.Frame(Ventana,bg="yellow")
LEP1.place(x=480, y=295, width=350,height=265)

LEP2 = tkinter.Frame(Ventana,bg="yellow")
LEP2.place(x=840, y=295, width=350,height=265)

t1 = tkinter.Label(EOQ1, text="Economic Order Quantity Sin Faltante")
t1.pack()

t1 = tkinter.Label(EOQ2, text="Economic Order Quantity Con Faltante")
t1.pack()

t1 = tkinter.Label(LEP1, text="Learning Environment Preferences Sin Faltante")
t1.pack()

t1 = tkinter.Label(LEP2, text="Learning Environment Preferences Con Faltante")
t1.pack()

Ventana.mainloop()