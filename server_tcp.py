import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(("0.0.0.0", 4433))
    server.listen(5)
    print("Listening")

    client_socket, address = server.accept()
    print("Received from : {}".format(address))
    data = client_socket.recv(1024).decode()
    print(data)

    server.close()
except Exception as error:
    print("Erro: ", error)
    server.close()