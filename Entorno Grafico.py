from tkinter import Tk, Label, Entry
from math import floor


# Diccionario
calificaciones = {'Saul' : 8.3 , 'Greta' : 9.5 , 
                  'Alex' : 7.8, 'Oscar' : 6.9, 'Jose' : 9.2}


# Creo la ventana
ventana = Tk()
ventana.title("Calificación")
ventana.eval('tk::PlaceWindow . center')

#Creo los elementos a poner en la ventana 
texto = Label(ventana,  font=('Arial 15 bold'), text = '¿Cuál es tu nombre?')
entrada = Entry(ventana, font=('Arial 15 bold'),background='#00ffff', width=30)
score = Label(ventana,font=('Arial 15 bold'),text='')


# Pongo los elementos en la ventana
texto.pack(side = 'top', padx=(20,5), pady=10)
entrada.pack(side='top', padx=(20,5), pady=10)
score.pack(side='bottom', padx= (0,10),pady=(10))

# Toma el dato de la entrada después de dar enter
# e imprime el nombre en consola
def mi_entrada(event):
    nombre = entrada.get()
    resultado = floor(calificaciones.get(nombre, -1))
    if resultado != -1:
        score.configure(text = 'Tu calificación es: '+ str(resultado))
    else:
        score.configure(text = 'Ingresa un nombre que esté en la lista')    

# Enlaza el recuadro de entrada con dar Return    
entrada.bind('<Return>', mi_entrada)

ventana.mainloop()