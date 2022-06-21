import socket

def simulacao_cliente(host = 'localhost', porta=None): 
    '''
    Esta Função funcionará de forma a simular o servidor como se fosse um cliente, 
    fazendo a conexão com outro servidor passado por parametro
    '''
    
    # Cria um socket TCP/IP 
    socket_auxiliar = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # Conecta o socket no servidor 
    endereco_servidor = (host, porta) 
    print ("Connectando em: %s porta: %s" % endereco_servidor) 
    socket_auxiliar.connect(endereco_servidor)      
    
    return socket_auxiliar


def Servidor(host = 'localhost', porta=8081):#Parametros padrao para essa funcao: IP=localhost Porta = 8081, mesmos que o do cleinte, para que a conexão funcione
    tamanho = 2048 #Tamanho máximo de dados a ser recebidos em um envio
    
    # Cria um socket TCP
    socket_servidor_1 = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
    # Ativar endereço/porta 
    socket_servidor_1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Liga o socket à porta
    endereco_servidor = (host, porta)
    print ("Servido ligado em: %s porta: %s" % endereco_servidor)
    
    socket_servidor_1.bind(endereco_servidor)
    # Espera pelos clientes, o argumento especifica o número máximo de conexões enfileiradas
    socket_servidor_1.listen(5) 
    i = 0
    print ("Esperando por Cliente")
    conexao_com_cliente, endereco = socket_servidor_1.accept() #Aceitar o cliente
    
    while True: 
        
        #Envia Menu
        print("Enviando Menu")
        menu = "\nBem Vindo!\nDigite:\n1 - Para Soma de inteiros\n2 - Para Concatenação de Strings\n3 - Para Sair"
        conexao_com_cliente.send(menu.encode())

        #Recebe Resposta
        mensagem_do_cliente = conexao_com_cliente.recv(tamanho) 
        
        if mensagem_do_cliente.decode() != "3": #verifica se a mensagem do cliente não foi para sair
            print ("Resposta: %s" %mensagem_do_cliente.decode())
            
            if mensagem_do_cliente.decode() == "1":  #Caso a mensagem do cliente seja somar inteiros, conecta com servidor 2
                
                #Conecta com servidor 2 atraves de socket auxiliar
                socket_auxiliar = simulacao_cliente(porta = 8082)
                
                if socket_auxiliar: #Caso a conexão funcione
                    print("Conectado!")
                    
                    #Solicita primeiro numero
                    conexao_com_cliente.send("Primeiro número: ".encode())
                    
                    #Recebe do Cliente o primeiro numero
                    mensagem_do_cliente = conexao_com_cliente.recv(tamanho)
                    print("Primeiro Numero: ", mensagem_do_cliente.decode())
                    
                    #envia para o servidor 2
                    socket_auxiliar.send(mensagem_do_cliente)
                    print("Enviado Ao Servidor 2")
                    
                    #recebe confirmacao de recebimento
                    confirmacao = socket_auxiliar.recv(tamanho)
                    print("Servidor 2> ",confirmacao.decode())
                    
                    if confirmacao.decode() == "Recebido": #Caso tenha recebido corretamente
                        #Solicita o Segundo numero
                        conexao_com_cliente.send("Segundo número: ".encode())
                        
                        #Recebe do Cliente o segundo numero
                        mensagem_do_cliente = conexao_com_cliente.recv(tamanho)
                        print("Segundo Numero: ",mensagem_do_cliente.decode())
                        
                        #envia para o servidor 2
                        socket_auxiliar.send(mensagem_do_cliente)
                        print("Enviado Ao Servidor 2")
                        
                        #recebe a resposta do servidor 2 e armazena na variável 'resposta' para ser enviada ao cliente depois das condicoes
                        resposta = socket_auxiliar.recv(tamanho)
                        print("Servidor 2> ",resposta.decode())
                    
                    #fecha esse socket auxiliar
                    socket_auxiliar.close()

            elif mensagem_do_cliente.decode() == "2": #Caso a mensagem do cliente seja para concatenar strings 
                #Conecta com servidor 3 via socket auxiliar
                socket_auxiliar = simulacao_cliente(porta = 8083)
                
                if socket_auxiliar: #Caso a conexao de certo
                    print("Conectado!")
                    
                    #Solicita primeira string para o cliente
                    conexao_com_cliente.send("Primeira String: ".encode())
                    
                    #Recebe do Cliente a primeira string
                    mensagem_do_cliente = conexao_com_cliente.recv(tamanho)
                    print("Primeira String: ", mensagem_do_cliente.decode())
                    
                    #envia para o servidor 3
                    socket_auxiliar.send(mensagem_do_cliente)
                    print("Enviado Ao Servidor 3")
                    
                    #recebe confirmacao de recebimento
                    confirmacao = socket_auxiliar.recv(tamanho)
                    print("Servidor 3> ",confirmacao.decode())
                    
                    if confirmacao.decode() == "Recebido":#Caso tenha recebido corretamente
                        
                        #Solicita a Segunda string
                        conexao_com_cliente.send("Segunda String: ".encode())
                        
                        #Recebe do Cliente a segunda string
                        mensagem_do_cliente = conexao_com_cliente.recv(tamanho)
                        print("Segunda String: ",mensagem_do_cliente.decode())
                        
                        #envia para o servidor 3
                        socket_auxiliar.send(mensagem_do_cliente)
                        print("Enviado Ao Servidor 3")

                        #recebe a resposta do servidor 3 e armazena na variável 'resposta' para ser enviada ao cliente depois das condicoes
                        resposta = socket_auxiliar.recv(tamanho)
                        print("Servidor 3> ",resposta.decode())
                        
                #fecha esse socket auxiliar
                socket_auxiliar.close()
                
        elif mensagem_do_cliente.decode() == "3": #Caso a mensagem do cliente seja para sair
            #Finalizando tudo
            print("Desligando Servidor...")
            
            resposta = "Finalizado".encode()
            
            socket_aux_s2 = simulacao_cliente(porta = 8082)
            socket_aux_s2.send(resposta)
            socket_aux_s2.close()
            
            socket_aux_s3 = simulacao_cliente(porta = 8083)
            socket_aux_s3.send(resposta)
            socket_aux_s3.close()
            
            print("Ate Logo!")
            break 
        else:
            resposta = "Opcao Invalida".encode()

        #Envia resposta final que ficou salva na variavel 'resposta' para o cliente 
        print("Enviando Resposta Final Ao Cliente")
        conexao_com_cliente.send(resposta)

        #Recebe do cliente a resposta dizendo Que foi recebido
        mensagem_do_cliente = conexao_com_cliente.recv(tamanho)
        print("Cliente> ", mensagem_do_cliente.decode())

    #caso caia no 'break' da opção 3 do menu, fecha os sockets deste servidor e do cliente
    conexao_com_cliente.close()
    socket_servidor_1.close()

Servidor(host='localhost',porta=8081) #Chama a funcao criada passando os parametros de conexao que serão usados
