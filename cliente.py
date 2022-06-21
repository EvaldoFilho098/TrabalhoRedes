import socket
def Cliente(host = 'localhost', porta=8081):  #Parametros padrao para essa funcao: IP=localhost Porta = 8081
    # Cria um socket TCP/IP 
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # Conecta o socket no servidor
    endereco_servidor = (host, porta)  
    socket_cliente.connect(endereco_servidor)
    print ("Connectando em: %s porta: %s" % endereco_servidor)     
       
    try: 
        
        while True:
            #recebe menu
            mensagem_do_servidor = socket_cliente.recv(2048)
            print ("%s" % mensagem_do_servidor.decode())
            
            #pega resposta
            mensagem_de_resposta = input("> ")
            
            if mensagem_de_resposta != "3": #A resposta 3 é para sair, caso não seja a resposta 3, executar codigo abaixo
                #Envia resposta
                socket_cliente.send(mensagem_de_resposta.encode())

                #Recebe primeira solicitacao
                mensagem_do_servidor = socket_cliente.recv(2048)
                print ("%s" % mensagem_do_servidor.decode())
                
                #pega resposta da primeira solicitacao
                mensagem_de_resposta = input("> ")
                
                #Envia resposta da primeira solicitacao
                socket_cliente.send(mensagem_de_resposta.encode())

                #Recebe segunda solicitacao
                mensagem_do_servidor = socket_cliente.recv(2048)
                print ("%s" % mensagem_do_servidor.decode())
                
                #pega resposta da segunda solicitacao
                mensagem_de_resposta = input("> ")
                
                #Envia resposta da segunda solcitacao
                socket_cliente.send(mensagem_de_resposta.encode())

                #Recebe resposta
                mensagem_do_servidor = socket_cliente.recv(2048)
                print ("\n\nResposta: %s" % mensagem_do_servidor.decode())

                #Envia Confirmacao de Recebimento
                socket_cliente.send("Recebido".encode())
                
            else: #Caso seja a resposta 3, envia a resposta para o servidor e para o loop infinito de execução e finaliza o socket
                socket_cliente.send(mensagem_de_resposta.encode())
                print ("Desligando...") 
                socket_cliente.close() 
                break

    except:
        print ("Houve um problema e não foi possível realizar a conexão.\nDesligando...") 
        socket_cliente.close() 

Cliente(host='localhost',porta=8081) #Chama a funcao criada passando os parametros de conexao que serão usados
