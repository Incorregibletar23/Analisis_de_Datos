# 1.- ---------- Encabezado ----------

'''
Programa: Ejercicio 1 Personas - Ej1 Personas.py
Autor: Ramírez Vásquez Eduardo
Fecha de creación: 04/09/2025
Descripción: Este Programa es el
'''

# 2.- ---------- Importación de módulos y bibliotecas ----------

import tkinter as tk

# 3.- ---------- Definición de funciones o clases ----------

def ventana():
    ventana1 = tk.Tk()
    ventana1.title('Ejercicio 1')
    ventana1.geometry('400x300+520+270')
    izquierda = tk.Frame(ventana1, bg='#f0f0f0', width=200, height=300)
    izquierda.pack(side='left', fill='y')
    derecha = tk.Frame(ventana1, bg='white', width=200, height=300)
    derecha.pack(side='right', fill='y')

    texto = tk.Text(derecha,# En donde se coloca el contenedor
        width=160,                  # Ancho de la etiqueta
        height=30,                  # Define cuantas líneas de texto se pueden mostrar
        font=("Century Gothic", 10),# Fuente, tamaño y estilo
        fg="white",                 # Color del texto
        bg="#5E6069"                # Color de fondo de la etiqueta
    )
    nombre = tk.Label(
        izquierda,
        text=f"Nombre",# Texto que muestra la etiqueta
        font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
        fg="black",                         # Color del texto
        bg="#f0f0f0",                       # Color del fondo de la etiqueta
        anchor="center",                    # Posición del texto dentro de la etiqueta
        relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
        bd=2,                               # Grosor del borde
        padx=10,                            # Espacio interno horizontal
        pady=5                              # Espacio interno vertical
    )
    entnomb = tk.Entry(
        izquierda,
        font=("Century Gothic", 12),
        bg="#ffffff",           # Fondo
        fg="#333333",           # Texto
        bd=2,                   # Grosor del borde
        relief="groove",        # Estilo del borde
        width=15,               # Ancho en caracteres
        justify="center",       # Texto centrado
        insertbackground="black"# Color del cursor
    )
    nacional = tk.Label(
        izquierda,
        text=f"Nacionalidad",# Texto que muestra la etiqueta
        font=("Century Gothic", 12, "bold"),# Fuente, tamaño y estilo (negrita)
        fg="black",                         # Color del texto
        bg="#f0f0f0",                       # Color del fondo de la etiqueta
        anchor="center",                    # Posición del texto dentro de la etiqueta
        relief="flat",                      # Tipo de borde (puede ser flat, raised, sunken, ridge, groove, solid)
        bd=2,                               # Grosor del borde
        padx=10,                            # Espacio interno horizontal
        pady=5                              # Espacio interno vertical
    )
    paises = ["México", "USA", "España", "Francia", "Alemania"]
    pais1 = tk.StringVar(value=paises[0])
    cajapais = tk.OptionMenu(izquierda, pais1, *paises)
    cajapais.config(
        font=("Century Gothic", 12),
        bg="#ffffff",
        fg="#333333",
        relief="groove",
        bd=2,
        width=11,
        anchor="center"
    )
    boton = tk.Button(
        izquierda,
        text='Ingresar',
        font=("Century Gothic", 10),
        bg="#abaeb8",              # Fondo
        fg="black",                # Color del texto
        activebackground="#4b5572",# Fondo al presionar
        activeforeground="white",  # Color del texto al presionar
        padx=40,                   # Espacio horizontal interno
        pady=3,                    # Espacio vertical interno
        relief="raised",           # Estilo de borde
        bd=3,                      # Grosor del borde
        cursor="hand2",            # Cambia a manita
        command=lambda: ingresarPersona(entnomb, pais1, texto)
    )
    def ingresarPersona(persona, nacionalidad, texto):
        pers = persona.get()
        nac = nacionalidad.get()
        text=pers + '---' + nac + '\n'
        texto.insert(tk.END, text)
    nombre.pack(pady=5, fill='x')
    entnomb.pack(pady=5,padx=20, fill='x')
    nacional.pack(pady=5, fill='x')
    cajapais.pack(pady=5, padx=10)
    boton.pack(pady=8, padx='20')
    texto.pack(pady=10)
          
    return ventana1

# 4.- ---------- Variables u objetos globales ----------
# 5.- ---------- Bloque Principal ----------

v = ventana()
v.mainloop()

# 6.- ---------- Documentación y comentarios ----------
