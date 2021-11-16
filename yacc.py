# Yacc example
 
from ply.lex import Lexer
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

def p_programa(p):
    'programa : lista_declaracao'

def p_lista_declaracao(p):
    """
    lista_declaracao : lista_declaracao declaracao
                     | declaracao 
    """
def p_declaracao(p):
    """
    declaracao : declaracao_variaveis
              | declaracao_funcoes
    """

def p_declaracao_variaveis(p):
    """
    declaracao_variaveis : tipo ID pv
                        | tipo ID acol numero fcol pv
    """

def p_tipo(p):
    """
    tipo : INT
        | VOID
    """

def p_declaracao_funcoes(p):
    """
    declaracao_funcoes : tipo ID apar parametros fpar declaracao_composta
    """

def p_parametros(p):
    """
    parametros : lista_parametros
              | VOID
    """

def p_lista_parametros(p):
    """
    lista_parametros : lista_parametros vir param 
                    | param 
    """

def p_param(p):
    """
    param : tipo ID
         | tipo ID acol fcol
    """

def p_declaracao_composta(p):
    """
    declaracao_composta : acha declaracoes_locais lista_comandos fcha
    """

def p_declaracoes_locais(p):
    """
    declaracoes_locais : declaracoes_locais declaracao_variaveis
                      | 
    """

def p_lista_comandos(p):
    """
    lista_comandos : lista_comandos comando
                  | empty
    """

def p_comando(p):
    """
    comando : declaracao_expressao
           | declaracao_composta
           | declaracao_selecao
           | declaracao_iteracao
           | declaracao_retorno
    """

def p_declaracao_expressao(p):
    """
    declaracao_expressao : expressao pv
             | pv
    """

def p_declaracao_selecao(p):
    """
    declaracao_selecao : IF apar expressao fpar comando
                      | IF apar expressao fpar comando ELSE comando
    """

def p_declaracao_iteracao(p):
    """
    declaracao_iteracao : WHILE apar expressao fpar comando
    """

def p_declaracao_retorno(p):
    """
    declaracao_retorno : RETURN pv
                      | RETURN expressao pv
    """

def p_expressao(p):
    """
    expressao : variavel atr expressao
             | expressao_simples
    """

def p_variavel(p):
    """
    variavel : ID
            | ID acol expressao fcol
    """

def p_expressao_simples(p):
    """
    expressao_simples : soma_expressao op_relacional soma_expressao
                     | soma_expressao
    """

def p_op_relacional(p):
    """
    op_relacional : menig
                 | men
                 | mai
                 | maiig
                 | ig
                 | dif
    """

def p_soma_expressao(p):
    """
    soma_expressao : soma_expressao soma termo
                  | termo
    """

def p_soma(p):
    """
    soma : add
        | sub
    """

def p_termo(p):
    """
    termo : termo mult fator
         | fator
    """

def p_mult(p):
    """
    mult : mlt
        | divv
    """

def p_fator(p):
    """
    fator : apar expressao fpar
         | variavel
         | ativacao
         | numero
    """

def p_ativacao(p):
    """
    ativacao : ID apar argumentos fpar
    """

def p_argumentos(p):
    """
    argumentos : lista_argumentos
              | empty
    """

def p_lista_argumentos(p):
    """
    lista_argumentos : lista_argumentos vir expressao
                    | expressao
    """

def p_empty(p):
     """
     empty :
     """
     pass 

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

data = '''
int main(){
    int x = 21;
}
'''
from lex import * 
#while True:
#    s = input('> ')
result = parser.parse(data, lexer=lexer,debug=True)

#    print(result)