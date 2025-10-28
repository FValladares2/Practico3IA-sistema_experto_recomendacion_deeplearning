#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import font as tkFont
import random
import json
import os


# In[2]:


# Función para recomendar tecnica de aprendizaje profundo
def inferir_diagnostico(base, reglas):
    recomendaciones = []
    for regla in reglas:
        for condicion in regla["condiciones"]:
            if all(base[cond] for cond in list(condicion.keys()) ):
                recomendaciones.append(regla["conclusion"])
    if not recomendaciones:
        recomendaciones.append("Recomendación inconclusa")
        
    return recomendaciones

def recomendar_deeplearning(base):
    reglas = json.load(open('reglas.json'))
    #print(reglas)
    diagnostico = inferir_diagnostico(base, reglas)
    return diagnostico


# In[3]:


# Función para mostrar la recomendación como widget
def mostrar_rec(recomendacion):
    for widget in frame_resultados.winfo_children():
        widget.destroy()

    frame = tk.Frame(frame_resultados)
    frame.pack(side='left', padx=10)

    texto = ""
    for rec in recomendacion:
        texto = rec + "\n"
    
    label_text = tk.Label(frame, text=texto, wraplength=180)
    label_text.pack()


# In[4]:


# Función para manejar el botón de recomendación
def recomendar_boton():    
    tipo_datos = entry_tipodato.get()
    objetivo_apr = entry_objetivo.get()

    #tipo_datos = "Imagenes"
    #objetivo_apr = "Reconocimiento"
    
    base_conocimientos = {
        "tipoDato_imagen": False,
        "tipoDato_audio": False,
        "tipoDato_video": False,
        "tipoDato_texto": False,
        "tipoDato_estadistico": False,
        "tipoObjetivo_generacion": False,
        "tipoObjetivo_reconocimiento": False,
        "tipoObjetivo_traduccion": False,
        "tipoObjetivo_prediccion": False
    }

    if tipo_datos == "Imagenes":
        base_conocimientos["tipoDato_imagen"] = True
    elif tipo_datos == "Audio":
        base_conocimientos["tipoDato_audio"] = True
    elif tipo_datos == "Video":
        base_conocimientos["tipoDato_video"] = True
    elif tipo_datos == "Texto":
        base_conocimientos["tipoDato_texto"] = True
    elif tipo_datos == "Estadistico/csv":
        base_conocimientos["tipoDato_estadistico"] = True
        
    if objetivo_apr == "Reconocimiento":
        base_conocimientos["tipoObjetivo_reconocimiento"] = True
    elif objetivo_apr == "Traduccion":
        base_conocimientos["tipoObjetivo_traduccion"] = True
    elif objetivo_apr == "Generacion":
        base_conocimientos["tipoObjetivo_generacion"] = True
    elif objetivo_apr == "Prediccion":
        base_conocimientos["tipoObjetivo_prediccion"] = True
    
    
    recomendaciones = recomendar_deeplearning(base_conocimientos)

    if recomendaciones:
        mostrar_rec(recomendaciones)
    else:
        messagebox.showwarning("Sin recomendaciones", f"No se encontraron recomendaciones atingentes.")


# In[6]:


# Crear la ventana principal
root = tk.Tk()
root.geometry("500x400")
root.title("Sistema de recomendación ~ técnicas deeplearning")
root.configure(bg="#f0f0f5")  # Color de fondo de la ventana principal

# Fuente personalizada
font_label = tkFont.Font(family="Helvetica", size=16)
font_entry = tkFont.Font(family="Helvetica", size=15)
font_button = tkFont.Font(family="Helvetica", size=16, weight="bold")

# Etiqueta para eleccion tipo de dato
label_tipodato = tk.Label(root, text="Elige el tipo de dato del dataset :", font=font_label, bg="#f0f0f5")
label_tipodato.pack(pady=20)

# Dropdown menu para eleccion tipo de dato

a = ["Imagenes", "Texto", "Audio", "Video", "Estadistico/csv"]

entry_tipodato = ttk.Combobox(root, values=a, state="readonly")
entry_tipodato.set("Elije un tipo de dato..")
entry_tipodato.pack()

# Etiqueta para objetivo
label_objetivo = tk.Label(root, text="Con qué objetivo busca entrenar el modelo IA? :", font=font_label, bg="#f0f0f5")
label_objetivo.pack(pady=20)

# Dropdown menu para eleccion objetivo

b = ["Reconocimiento", "Traduccion", "Generacion", "Prediccion"]

entry_objetivo = ttk.Combobox(root, values=b, state="readonly")
entry_objetivo.set("Elije un objetivo..")
entry_objetivo.pack()

# Botón para mostrar recomendación
btn_recomendar = tk.Button(root, text="Recomendar Técnica", command=recomendar_boton, font=font_button, 
                           bg="#4CAF50", fg="white", height=2, width=20)
btn_recomendar.pack(pady=20)

# Frame para los resultados (en la misma ventana)
frame_resultados = tk.Frame(root, bg="#f0f0f5")
frame_resultados.pack(pady=20)

# Etiqueta para mostrar los resultados
label_resultado = tk.Label(frame_resultados, text="", font=font_label, bg="#f0f0f5", fg="#333333")
label_resultado.pack()

# Ejecutar el loop principal de la GUI
root.mainloop()


# In[ ]:




