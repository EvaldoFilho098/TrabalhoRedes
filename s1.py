import socket,threading

def simulacao_cliente(host_2 = 'localhost', port=None): 
    # Create a TCP/IP socket 
    sock_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host_2, port) 
    print ("Connectando em: %s porta: %s" % server_address) 
    sock_2.connect(server_address)      
    
    return sock_2


def Servidor(host = 'localhost', port=8081):
    data_payload = 2048 #The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Servido ligado em: %s porta: %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5) 
    i = 0
    print ("Esperando por Cliente")
    client, address = sock.accept()
    while True: 
        
        #Envia Menu
        print("Enviando Menu")
        menu = "Bem Vindo!\n[1] Soma de inteiros\n[2] Concatenação de Strings\n[3] Sair"
        client.send(menu.encode())

        #Recebe Resposta
        data = client.recv(data_payload) 
        if data.decode() != "3":
            print ("Resposta: %s" %data.decode())
            
            if data.decode() == "1":
                #Conecta com servidor 2
                sock_1 = simulacao_cliente(port = 8082)
                if sock_1:
                    print("Conectado!")
                    #Solicita primeiro numero
                    client.send("Primeiro número: ".encode())
                    #Recebe do Cliente o primeiro numero
                    data = client.recv(data_payload)
                    print("Primeiro Numero: ", data.decode())
                    #envia para o servidor 2
                    sock_1.send(data)
                    print("Enviado Ao Servidor 2")
                    #recebe confirmacao de recebimento
                    conf = sock_1.recv(data_payload)
                    print("Servidor 2> ",conf.decode())
                    if conf.decode() == "Recebido":
                        #Solicita o Segundo numero
                        client.send("Segundo número: ".encode())
                        #Recebe do Cliente o segundo numero
                        data = client.recv(data_payload)
                        print("Segundo Numero: ",data.decode())
                        #envia para o servidor 2
                        sock_1.send(data)
                        print("Enviado Ao Servidor 2")
                        #recebe a resposta do servidor 2
                        resposta = sock_1.recv(data_payload)
                        print("Servidor 2> ",resposta.decode())
                        #envia resposta para o Cliente
                    sock_1.close()

            elif data.decode() == "2":
                #Conecta com servidor 3
                sock_1 = simulacao_cliente(port = 8083)
                #Solicita primeiro numero
                client.send("Primeira String: ".encode())
                #Recebe do Cliente o primeiro numero
                data = client.recv(data_payload)
                #envia para o servidor 2
                sock_1.send(data)
                #recebe confirmacao de recebimento
                conf = sock_1.recv(data_payload)
                if conf.decode() == "Recebido":
                    #Solicita o Segundo numero
                    client.send("Segunda String: ".encode())
                    #Recebe do Cliente o segundo numero
                    data = client.recv(data_payload)
                    #envia para o servidor 2
                    sock_1.send(data)
                    #recebe a resposta do servidor 2
                    resposta = sock_1.recv(data_payload)
                sock_1.close()
        elif data.decode() == "3":
            print("Desligando Servidor...")
            resposta = "Finalizado".encode()
            sock_1 = simulacao_cliente(port = 8082)
            sock_2 = simulacao_cliente(port = 8083)
            sock_1.send(resposta)
            sock_2.send(resposta)
            sock_1.close()
            sock_2.close()
            print("Ate Logo!")
            break 
        else:
            resposta = "Opcao Invalida".encode()

        print("Enviando Resposta Ao Cliente")
        client.send(resposta)

        data = client.recv(data_payload)
        print("Cliente> ", data.decode())

    client.close()
    sock.close()

Servidor('192.168.99.254')

#thr = threading.Thread(target=Servidor)
#thr.start()
