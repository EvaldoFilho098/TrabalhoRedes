import socket,threading

def Servidor(host = 'localhost', port=8082):
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
    #print ("Esperando Solicitacao")
    #client, address = sock.accept()
    while True: 
        print ("Esperando Solicitacao")
        client, address = sock.accept()
        #Recebe o primeiro numero
        data_1 = client.recv(data_payload) 
        if data_1.decode() != "Finalizado":
            print ("Primeiro Numero: %s" %data_1.decode())
            #Envia confirmacao de recebimento
            client.send("Recebido".encode())
            #Recebe o segundo numero
            data_2 = client.recv(data_payload)
            print ("Segundo Numero: %s" %data_2.decode())
            #fazendo a soma
            data_1 = data_1.decode()
            data_2 = data_2.decode()
            soma = int(data_1) + int(data_2)
            resposta = data_1 + " + " + data_2 + " = " + str(soma)
            print ("Resposta enviada: %s" %resposta)
            #Envia Resposta
            client.send(str(resposta).encode())
            # Finaliza conexao
            #client.close()
            #i+=1
            #if i>=3: break 
        else:
            print ("Desligando Servidor")
            break
    print("Ate Logo!")
    client.close
    sock.close()   

Servidor()
#thr = threading.Thread(target=Servidor)
#thr.start()