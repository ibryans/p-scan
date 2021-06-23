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

print('Conectando em ' + host)

# socket() usa 2 principais argumentos: address-family e socket-type
# address-family: AF_INET = internet domain address family, suporta endereços ipv4
# socket-type: SOCK_STRETAM para TCP, SOCK_DGRAM para UDP, ou SOCK_RAW para acessar diretamente o protocolo IP.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mudando o tempo da tentativa de se conectar a uma porta pelo host
client.settimeout(0.2)

# retorna o resultado da conexão baseada no retorno de connect_ex()
def code_status(code):
    switch = {
        11: 'Error',
        114: 'Success'
    }
    return switch.get(code, 'Inválido')

# Fazendo uma conexão com o host para cada porta, com um código de status da conexão como retorno
for port in ports:
    code = client.connect_ex((host, port))
    print('.: Porta ', port, '\t|', code, '\t[', code_status(code), ']')


# armazenando a resposta (1024 bytes)
# response = client.recv(1024)

# print('Resposta do cliente: ', response)
