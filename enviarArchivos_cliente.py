import socket
import os
import tkinter as tk
from tkinter import filedialog, messagebox

client_socket = None

def send_file(filename):
    global client_socket
    if not os.path.isfile(filename):
        messagebox.showerror("Error", f"El archivo '{filename}' no existe.")
        return
    
    try:
        filesize = os.path.getsize(filename)
        
        client_socket.send(os.path.basename(filename).encode('utf-8'))
        filename_ack = client_socket.recv(1024).decode('utf-8')
        if filename_ack != 'ACK_FILENAME':
            print(f'Error: No se pudo confirmar el nombre del archivo correctamente. Recibido: {filename_ack}')
            return
        
        client_socket.send(str(filesize).encode('utf-8'))
        filesize_ack = client_socket.recv(1024).decode('utf-8')
        if filesize_ack != 'ACK_FILESIZE':
            print(f'Error: No se pudo confirmar el tamaño del archivo correctamente. Recibido: {filesize_ack}')
            return
        
        with open(filename, "rb") as f:
            bytes_sent = 0
            while True:
                bytes_read = f.read(4096)
                if not bytes_read:
                    break
                client_socket.sendall(bytes_read)
                bytes_sent += len(bytes_read)
                print(f'Bytes enviados: {bytes_sent}/{filesize}')
        
        print(f'Archivo {filename} enviado correctamente')
        messagebox.showinfo("Archivo enviado", f"Archivo {filename} enviado correctamente")
    except Exception as e:
        print(f"Error al enviar el archivo: {e}")
    finally:
        client_socket.close()

def receive_file(dest_folder):
    global client_socket
    try:
        filename = client_socket.recv(1024).decode('utf-8')
        client_socket.send('ACK_FILENAME'.encode('utf-8'))
        
        filesize = client_socket.recv(1024).decode('utf-8')
        if not filesize.isdigit():
            print(f'Error: Tamaño del archivo no es un número válido: {filesize}')
            return
        filesize = int(filesize)
        client_socket.send('ACK_FILESIZE'.encode('utf-8'))
        
        filepath = os.path.join(dest_folder, os.path.basename(filename))
        
        with open(filepath, "wb") as f:
            bytes_received = 0
            while bytes_received < filesize:
                bytes_read = client_socket.recv(4096)
                if not bytes_read:
                    break
                f.write(bytes_read)
                bytes_received += len(bytes_read)
                print(f'Bytes recibidos: {bytes_received}/{filesize}')
        
        print(f'Archivo {filename} recibido correctamente y guardado en {filepath}')
        messagebox.showinfo("Archivo recibido", f"Archivo {filename} recibido correctamente y guardado en {filepath}")
    except Exception as e:
        print(f"Error al recibir el archivo: {e}")
    finally:
        client_socket.close()

def start_client(host, port):
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f'Conectado a {host}:{port}')
        return client_socket
    except Exception as e:
        print(f"Error al conectar al servidor: {e}")
        return None

def send_action():
    global client_socket
    if not client_socket:
        messagebox.showerror("Error", "No hay conexión establecida.")
        return
    
    filename = filedialog.askopenfilename(title="Seleccionar archivo a enviar")
    if filename:
        client_socket.send('SEND'.encode('utf-8'))
        send_file(filename)

def connect_action():
    global client_socket
    host = '172.168.3.104'
    port = 44444
    
    client_socket = start_client(host, port)
    if client_socket:
        messagebox.showinfo("Conexión exitosa", f"Conectado a {host}:{port}")
        send_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Cliente de Envío y Recepción de Archivos")

root.geometry("380x180")
root.resizable(False, False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (380 // 2)
y = (screen_height // 2) - (180 // 2)

root.geometry(f"380x180+{x}+{y}")

tk.Label(root, text="Modo: Cliente").pack(pady=10)

connect_button = tk.Button(root, text="Conectar", command=connect_action)
connect_button.pack(pady=10)

send_button = tk.Button(root, text="Enviar archivo", command=send_action, state=tk.DISABLED)
send_button.pack(pady=10)

tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

root.mainloop()