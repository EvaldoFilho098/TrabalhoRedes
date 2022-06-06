import socket
def Cliente(host = 'localhost', port=8081): 
    # Cria um socket TCP/IP 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Conecta o socket no servidor
    server_address = (host, port) 
    print ("Connectando em: %s porta: %s" % server_address) 
    sock.connect(server_address)        
    try:
        while True:
            #recebe menu
            data = sock.recv(2048)
            print ("%s" % data.decode())
            #pega resposta
            resp = input("> ")
            if resp != "3":
                #Envia resposta
                sock.send(resp.encode())

                #Recebe primeira solicitacao
                data = sock.recv(2048)
                print ("%s" % data.decode())
                #pega resposta da primeira solicitacao
                resp = input("> ")
                #Envia resposta da primeira solicitacao
                sock.send(resp.encode())

                #Recebe segunda solicitacao
                data = sock.recv(2048)
                print ("%s" % data.decode())
                #pega resposta da segunda solicitacao
                resp = input("> ")
                #Envia resposta da segunda solcitacao
                sock.send(resp.encode())

                #Recebe resposta
                data = sock.recv(2048)
                print ("Resposta: %s" % data.decode())

                #Envia Confirmacao de Recebimento
                sock.send("Recebido".encode())
            else:
                sock.send(resp.encode())
                break

    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 

Cliente('192.168.99.254')
