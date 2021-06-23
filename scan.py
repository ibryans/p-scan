# lib que fornece uma conexão com os protocolos de rede da máquina
import socket

host = 'bancocn.com'

# lista de portas para teste
# 21 = FTP (File Transfer Protocol)
# 23 = Telnet Protocol (texto sem criptografia)
# 80 = HTTP
# 443 = HTTPS
# 8080 = HTTP alternativo (web server ou web proxy)
ports = [21, 23, 80, 443, 8080]

print('Conectando em ' + host + '\n')

# retorna o resultado da conexão baseada no retorno de connect_ex()
def code_status(code):
    switch = {
        0: 'Open',
        11: 'Unavailable',
        114: 'In Progress'
    }
    return switch.get(code, 'Inválido')

print('Porta\t| Cod\t| Status')

# Fazendo uma conexão com o host para cada porta, com um código de status da conexão como retorno
for port in ports:

    # socket.socket() usa 2 principais argumentos: address-family e socket-type
    # address-family: AF_INET = internet domain address family, suporta endereços ipv4
    # socket-type: SOCK_STRETAM para TCP, SOCK_DGRAM para UDP, ou SOCK_RAW para acessar diretamente o protocolo IP.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Mudando o tempo da tentativa de se conectar a uma porta pelo host
    client.settimeout(0.2)
    
    code = client.connect_ex((host, port))
    print(port, '\t|', code, '\t|', code_status(code))


