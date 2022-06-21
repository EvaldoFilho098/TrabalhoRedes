import socket

def Servidor(host = 'localhost', porta=8083): #Parametros padrao para essa funcao: IP=localhost Porta = 8083 (uma nova porta, para um novo servidor estar ouvindo)
    tamanho = 2048 #Tamanho máximo de dados a ser recebidos em um envio
    
    # Cria um socket TCP
    socket_servidor_3 = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
    # Ativar endereço/porta 
    socket_servidor_3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Liga o socket à porta
    endereco_servidor = (host, porta)
    socket_servidor_3.bind(endereco_servidor)
    print ("Servido ligado em: %s porta: %s" % endereco_servidor)
    
    # Espera pelos clientes, o argumento especifica o número máximo de conexões enfileiradas
    socket_servidor_3.listen(5) 
    i = 0   
    
    while True: 
        print ("Esperando Solicitacao")
        conexao_servidor_1, address = socket_servidor_3.accept()
        
        #Recebe o primeiro numero
        string_1 = conexao_servidor_1.recv(tamanho) 
        
        if string_1.decode() != "Finalizado":
            print ("Primeira String: %s" %string_1.decode())
            
            #Envia confirmacao de recebimento
            conexao_servidor_1.send("Recebido".encode())
            
            #Recebe o segundo numero
            string_2 = conexao_servidor_1.recv(tamanho)
            print ("Primeira String: %s" %string_2.decode())
            
            #fazendo a concatenacao
            string_1 = string_1.decode()
            string_2 = string_2.decode()
            concatenacao = string_1 + string_2
            resposta = string_1 + " + " + string_2 + " = " + str(concatenacao)
            print ("Resposta enviada: %s" %resposta)
            
            #Envia Resposta
            conexao_servidor_1.send(str(resposta).encode())
        
        else: #caso a mensagem seja de desligar, para o loop infinito de execucao
            print("Desligando Servidor")
            break   
          
    #Após finalizar o loop, fecha as conexoes com o servidor 1 e o socket deste servidor
    print("Ate Logo!")      
    conexao_servidor_1.close
    socket_servidor_3.close()
    
Servidor(host='localhost',porta=8083) #Chama a funcao criada passando os parametros de conexao que serão usados