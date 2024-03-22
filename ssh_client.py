import paramiko

host = "127.0.0.1"
user = "xxxxx"
passwd = "xxxxx"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#  Define a política de tratamento de chaves de host ausentes como AutoAddPolicy(), o que faz com que o Paramiko adicione automaticamente as chaves dos hosts desconhecidos ao arquivo

client.connect(host, username=user, password=passwd)
# Estabelece uma conexão SSH com o servidor remoto especificado (host) usando o nome de usuário (username) e senha (password) fornecidos.

while True:
    stdin, stdout, stderr = client.exec_command(input("$: "))
    # Este comando solicita ao usuário uma entrada através da função input(), exibindo o prompt "$: ". Em seguida, executa o comando fornecido no servidor remoto e retorna três canais: stdin (entrada), stdout (saída padrão) e stderr (saída de erro).
    for line in stdout.readlines():
        print(line.strip())

    errors = stderr.readlines()
    if errors:
        print(errors)
