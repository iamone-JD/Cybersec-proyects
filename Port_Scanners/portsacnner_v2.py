import socket
import argparse
import sys

def escanear_puertos(ip, inicio, fin):
    try:
        for puerto in range(inicio, fin + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((ip, puerto))

            if result == 0:
                try:
                    servicio = socket.getservbyport(puerto)
                except:
                    servicio = 'Desconocido'
                print(f"Puerto Abierto: {puerto} ({servicio})")
                sock.close()
            else:
                print(f"Puerto cerrado: {puerto}")
    except KeyboardInterrupt:
        print("\nEscaneo interrumpido por el usuario.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Escáner de puertos simple similar a Nmap.")
    parser.add_argument("ip", help="Dirección IP a escanear.")
    parser.add_argument("-s", "--inicio", type=int, default=1, help="Puerto inicial (por defecto: 1).")
    parser.add_argument("-e", "--fin", type=int, default=65535, help="Puerto final (por defecto: 65535).")
    
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(f"Error en los argumentos: {e}")
        parser.print_help()
        sys.exit(1)
    except SystemExit:
        print("Error en los argumentos. Revisa la ayuda a continuación:")
        parser.print_help()
        sys.exit(1)
    
    try:
        ip = socket.gethostbyname(args.ip)
    except socket.gaierror:
        print("Error: Dirección IP o nombre de dominio inválido.")
        sys.exit(1)
    
    print(f"Escaneando la IP {ip} desde el puerto {args.inicio} hasta el puerto {args.fin}...")
    escanear_puertos(ip, args.inicio, args.fin)

if __name__ == "__main__":
    main()
