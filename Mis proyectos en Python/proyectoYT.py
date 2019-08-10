import serial, time, sys
from Tkinter import *
from time import sleep
Arduino = serial.Serial('COM12', 9600, timeout = 1)
print Arduino.readline()
def hora():
	return str (time.localtime()[2])+"-"+str(time.localtime()[1])+"-"+str(time.localtime()[0])+"\n"+str(time.localtime()[3])+":"+str(time.localtime()[4])+":"+str(time.localtime()[5])
def update():
	while 1: 
		e = Arduino.readline()
		temp= e [0:4]
		hume= e [5:9]
		met= e [10:13]
		readinghum.set(hume)#set
		readingtempe.set(temp)
		readingmetano.set(met)
		ventana.update()
		sleep(1)
ventana= Tk()
def imprimir(texto):
 print texto
def mostrar(a): 
	return a.deiconify # Muestra una ventana 
def ocultar(a): 
	return a.withdraw() # Oculta una ventana 
def ejecutar(f): 
	ventana.after(100, f)
ventana2=Toplevel(ventana)
ventana2.geometry("550x732")
imagen2= PhotoImage(file="C:\Users\AlVaRo\Desktop\pes1.gif")
lbl9= Label(ventana2,image= imagen2)
lbl9.pack()
ocultar(ventana)
def cerrar_splashscreen():
	ejecutar(ocultar(ventana2))
	ejecutar(mostrar(ventana))
ventana2.after(5000,cerrar_splashscreen)
#ventana.geometry("782x293")
ventana.title('Precipitador Electrostatico')
mifecha= StringVar()
lbl1=Label(ventana, textvar= mifecha,font=("Chiller",16))
lbl2= Label(ventana,text= "",font=("Chiller",16))
lbl2.grid(row= 15, column= 5)
def refresh_fecha():
	ventana.after(1000,refresh_fecha)
	mifecha.set(hora())
	lbl2.config(text=hora())
imagen1= PhotoImage(file = "C:\Users\AlVaRo\Desktop\pes.gif")
lbl3=Label(ventana,image=imagen1)
lbl3.grid(row=4,column=3)
Titulo = Label(ventana, text= 'Precipitador Electrostatico PES', fg = 'red', font = ("Bradley Hand ITC", 30))
Titulo.grid(row = 1, column = 3 )
nombre1= Label(ventana, text = 'Nombres ', fg = 'black',font = ("Arial", 8))
nombre1.grid(row= 15, column= 3)
btn1= Button(ventana,text= "SALIR",fg= "black", bg= "red",relief=SOLID)
btn1.grid(row= 15,column= 6)
readinghum= StringVar()
readingtempe = StringVar()
readingmetano= StringVar()
lbl3= Label(ventana,textvariable = readinghum,bg = 'blue')
lbl4= Label(ventana,textvariable = readingtempe,bg = 'pink')
lbl7= Label(ventana,textvariable = readingmetano,bg = 'cyan')
lbl5= Label(ventana, text= 'Humedad Relativa (%):', fg = 'black', font = ("Arial", 12))
lbl6= Label(ventana, tfupext= 'Temperatura (C): ', fg = 'black', font = ("Arial", 12))
lbl8= Label(ventana, text= 'Nivel de Metano (%): ', fg = 'black', font = ("Arial", 12))
lbl3.grid(row= 3, column= 1)
lbl4.grid(row= 7, column= 1)
lbl5.grid(row= 2,column= 1)
lbl6.grid(row= 6,column= 1)
lbl8.grid(row= 2,column= 6)
lbl7.grid(row= 3,column= 6)
def Salir():
	ventana.destroy()
btn1['command']= Salir
refresh_fecha()
ventana.after(5,update)
ventana.mainloop()