import socket,threading

def Servidor(host = 'localhost', port=8082):
    data_payload = 2048 #Tamanho máximo de dados a ser recebidos em um envio
    # Cria um socket TCP
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Ativar endereço/porta 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Liga o socket à porta
    server_address = (host, port)
    print ("Servido ligado em: %s porta: %s" % server_address)
    sock.bind(server_address)
   # Espera pelos clientes, o argumento especifica o número máximo de conexões enfileiradas
    sock.listen(5)    
    i = 0
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
