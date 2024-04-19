import socket

def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            try:
                servicio = socket.getservbyport(port)
            except:
                servicio = 'Desconocido'
            print(f"Puerto Abierto: {port} ({servicio})")
            sock.close()
        else:
            print(f"Puerto cerrado: {port}")

if __name__ == "__main__":
    ip = input("Introduzca la dirección IP a escanear: ")
    start_port = int(input("Introduzca el puerto inicial: "))
    end_port = int(input("Introduzca el puerto final: "))

    print(f"Escaneando la IP {ip} desde el puerto {start_port} hasta el puerto {end_port}...")
    scan_ports(ip, start_port, end_port)