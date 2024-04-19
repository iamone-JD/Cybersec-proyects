import socket

ip = input("Ingrese la direccion ip a escanear: ")

try:
    for puerto in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Reducido el tiempo de espera para un escaneo más rápido

        result = sock.connect_ex((ip, puerto))

        if result == 0:
            print("Puerto Abierto: " + str(puerto))
            sock.close()
        else:
            print("Puerto cerrado: " + str(puerto))

except KeyboardInterrupt:
    print("\nEscaneo interrumpido por el usuario.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
