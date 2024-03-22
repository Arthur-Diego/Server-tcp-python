import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET: Especifica que o socket será usado para comunicação através da família de endereços IPv4.
# socket.SOCK_STREAM: Indica que o tipo de socket será um fluxo de dados TCP, que fornece uma conexão bidirecional e confiável entre o cliente e o servidor.

file = open("output.txt", "w")

try:
    server.bind(("0.0.0.0", 4433))
    server.listen(5)
    # Este método define o socket do servidor para o modo de escuta (listening) e
    # especifica o número máximo de conexões de clientes que podem ser enfileiradas antes de serem aceitas.
    # Nesse caso, o argumento é 5, o que significa que o servidor permitirá que até 5 conexões de clientes fiquem na fila de espera antes de serem aceitas.
    # Quando o limite de conexões na fila é atingido, as conexões adicionais serão rejeitadas.
    print("Listening")

    client_socket, address = server.accept()
    print("Received from : {}".format(address))
    data = client_socket.recv(1024).decode()
    print(data)

    file.write(data)

    server.close()
except Exception as error:
    print("Erro: ", error)
    server.close()