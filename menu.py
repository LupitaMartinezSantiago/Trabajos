import tkinter as tk
import os
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Menu")
root.geometry("500x700")
root.configure(bg="#f0f0f0")  # Color de fondo

# Función para actualizar la barra de estado
def actualizar_estado(mensaje):
    barra_estado.config(text=mensaje)

# Función para mostrar mensajes de confirmación
def mostrar_confirmacion(mensaje):
    messagebox.showinfo("Confirmación", mensaje)

# Crear un título
titulo = tk.Label(root, text="Bienvenido, que quieres realizar pendejo?", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=20)

# Crear un marco para los botones
frame_botones = tk.Frame(root, bd=2, relief=tk.RAISED, padx=10, pady=10, bg="#ffffff")
frame_botones.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Funciones para ejecutar cada script
def monitoreo_cliente():
    os.system("python3 /Users/alexandermc/compu/doc/ciberseguridad/proyrcto/pantallas_clientes.py")
    mostrar_confirmacion("Monitoreo en cliente ejecutado")
    actualizar_estado("Monitoreo en cliente ejecutado")

def monitoreo_servidor():
    os.system("python3 /Users/alexandermc/compu/doc/ciberseguridad/proyrcto/pantallas_servidor.py")
    mostrar_confirmacion("Monitoreo en servidor ejecutado")
    actualizar_estado("Monitoreo en servidor ejecutado")

def envioArchivos_cliente():
    os.system("python3 /Users/alexandermc/compu/doc/ciberseguridad/proyrcto/enviarArchivos_cliente.py")
    mostrar_confirmacion("Envío de archivos en cliente ejecutado")
    actualizar_estado("Envío de archivos en cliente ejecutado")

def envioArchivos_servidor():
    os.system("python3 /Users/alexandermc/compu/doc/ciberseguridad/proyrcto/enviarArchivos_servidor.py")
    mostrar_confirmacion("Envío de archivos en servidor ejecutado")
    actualizar_estado("Envío de archivos en servidor ejecutado")

def ejecutar_bloqueo_teclado_mouse():
    os.system("python3 /Users/alexandermc/compu/doc/ciberseguridad/proyrcto/bloquearTM.py")
    mostrar_confirmacion("Bloqueo de teclado y mouse ejecutado")
    actualizar_estado("Bloqueo de teclado y mouse ejecutado")

def ejecutar_apagar_pc():
    os.system("python3 /Users/alexandermc/compu/doc/ciberseguridad/proyrcto/apagar.py")
    mostrar_confirmacion("Apagar PC remoto ejecutado")
    actualizar_estado("Apagar PC remoto ejecutado")

def denegar_ping():
    os.system("python3 /Users/alexandermc/compu/doc/ciberseguridad/proyrcto/denegarping.py")
    mostrar_confirmacion("Denegar ping remoto ejecutado")
    actualizar_estado("Denegar ping remoto ejecutado")

def permitir_ping():
    os.system("python3 /Users/alexandermc/compu/doc/ciberseguridad/proyrcto/permitirping.py")
    mostrar_confirmacion("Permitir ping remoto ejecutado")
    actualizar_estado("Permitir ping remoto ejecutado")

def chat_cliente():
    os.system("python3 /Users/alexandermc/compu/doc/ciberseguridad/proyrcto/chatCliente.py")
    mostrar_confirmacion("Chat cliente ejecutado")
    actualizar_estado("Chat cliente ejecutado")

def chat_servidor():
    os.system("python3 /Users/Gaby/Desktop/3701/proyectoChemo/proyrcto/chatServidor.py")
    mostrar_confirmacion("Chat servidor ejecutado")
    actualizar_estado("Chat servidor ejecutado")

def ejecutar_bloqueo_paginas():
    os.system("python3 /Users/alexandermc/compu/doc/ciberseguridad/proyrcto/bloquearpaginaa.py")
    mostrar_confirmacion("Bloqueo de páginas ejecutado")
    actualizar_estado("Bloqueo de páginas ejecutado")

# Crear un marco para agrupar los botones de Monitoreo
frame_monitoreo = tk.LabelFrame(frame_botones, text="Monitoreo", padx=10, pady=10, bg="#ffffff")
frame_monitoreo.pack(padx=10, pady=10, fill="both", expand="yes")

# Botones de monitoreo
boton_monitoreo_cliente = tk.Button(frame_monitoreo, text="Monitoreo en cliente", command=monitoreo_cliente, bg="#64ffda", fg="black", width=25)
boton_monitoreo_cliente.pack(pady=5)

boton_monitoreo_servidor = tk.Button(frame_monitoreo, text="Monitoreo en servidor", command=monitoreo_servidor, bg="#64ffda", fg="black", width=25)
boton_monitoreo_servidor.pack(pady=5)

# Crear un marco para agrupar los botones de Envío de Archivos
frame_envios = tk.LabelFrame(frame_botones, text="Envío de Archivos", padx=10, pady=10, bg="#ffffff")
frame_envios.pack(padx=10, pady=10, fill="both", expand="yes")

# Botones de envío de archivos
boton_envioArchivos_cliente = tk.Button(frame_envios, text="Envio de Archivos en cliente", command=envioArchivos_cliente, bg="#ec407a", fg="black", width=25)
boton_envioArchivos_cliente.pack(pady=5)

boton_envioArchivos_servidor = tk.Button(frame_envios, text="Envio de Archivos en servidor", command=envioArchivos_servidor, bg="#ec407a", fg="black", width=25)
boton_envioArchivos_servidor.pack(pady=5)

# Crear un marco para agrupar los botones de Control
frame_control = tk.LabelFrame(frame_botones, text="Control Remoto", padx=10, pady=10, bg="#ffffff")
frame_control.pack(padx=10, pady=10, fill="both", expand="yes")

# Botones de control remoto
boton_bloqueo_teclado_mouse = tk.Button(frame_control, text="Bloqueo de teclado y mouse", command=ejecutar_bloqueo_teclado_mouse, bg="#7d1fa2", fg="white", width=25)
boton_bloqueo_teclado_mouse.pack(pady=5)

boton_apagar_pc = tk.Button(frame_control, text="Apagar el PC remoto", command=ejecutar_apagar_pc, bg="#7d1fa2", fg="white", width=25)
boton_apagar_pc.pack(pady=5)

boton_denegar_ping = tk.Button(frame_control, text="Denegar ping remoto", command=denegar_ping, bg="#7d1fa2", fg="white", width=25)
boton_denegar_ping.pack(pady=5)

boton_permitir_ping = tk.Button(frame_control, text="Permitir ping remoto", command=permitir_ping, bg="#7d1fa2", fg="white", width=25)
boton_permitir_ping.pack(pady=5)

# Crear un marco para agrupar los botones de Chat
frame_chat = tk.LabelFrame(frame_botones, text="Chat", padx=10, pady=10, bg="#ffffff")
frame_chat.pack(padx=10, pady=10, fill="both", expand="yes")

# Botones de chat
boton_chat_cliente = tk.Button(frame_chat, text="Chat cliente", command=chat_cliente, bg="#00bcd4", fg="black", width=25)
boton_chat_cliente.pack(pady=5)

boton_chat_server = tk.Button(frame_chat, text="Chat servidor", command=chat_servidor, bg="#00bcd4", fg="black", width=25)
boton_chat_server.pack(pady=5)

# Botón para bloqueo de páginas
boton_bloqueo_paginas = tk.Button(frame_control, text="Bloqueo de páginas", command=ejecutar_bloqueo_paginas, bg="#7d1fa2", fg="white", width=25)
boton_bloqueo_paginas.pack(pady=5)

# Botón de salir
boton_salir = tk.Button(root, text="Salir", command=root.quit, bg="red", fg="white", width=25)
boton_salir.pack(pady=20)

# Crear una barra de estado
barra_estado = tk.Label(root, text="Listo", bd=1, relief=tk.SUNKEN, anchor=tk.W)
barra_estado.pack(side=tk.BOTTOM, fill=tk.X)

# Ejecutar la ventana principal
root.mainloop()