# importacionespantallas_clientes
import socket
import cv2
import numpy as np
import struct
from mss import mss

def capture_and_send_screen(conn):
    with mss() as sct:
        while True:
         
            screen = sct.grab(sct.monitors[0])
           
            screen_np = np.array(screen)
         
            _, frame = cv2.imencode('.jpg', screen_np)
            data = frame.tobytes()
            msg_size = struct.pack(">L", len(data))
            conn.sendall(msg_size + data)

def client_program():
    host = '172.168.3.104'
    port = 5001  
    client_socket = socket.socket()
    client_socket.connect((host, port))
    capture_and_send_screen(client_socket)
    client_socket.close()

if __name__ == '__main__':
    client_program()
