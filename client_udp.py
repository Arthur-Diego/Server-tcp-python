import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        msg = input("Mensagem: ")
        client.sendto("{}\n ".format(msg).encode(), ("127.0.0.1", 4433))
        data, sender = client.recvfrom(1024)
        print("{}: {}".format(sender, data.decode()))

        if msg == "sair" or data.decode() == "sair":
            break

    client.close()

except Exception as error:
    print("Error de conexão")
    print(error)
