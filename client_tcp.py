import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

# client.connect(("google.com", 80))
# client.send(b"GET / HTTP/3\nHost: www.google.com\n\n\n")

try:
    client.connect(("127.0.0.1", 4466))
    client.send(b"Oi tudo bem?")
    pacotes_recebidos = client.recv(1024).decode()

    print(pacotes_recebidos)
except:
    print("Deu pal!")