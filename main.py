data = """int main( ){
    int x;
    x = ;

    return 1;
}
"""

from os import error
from yacc_2 import *
from lex import *

# Run a preprocessor
import sys

try:
    with open(sys.argv[1]) as f:
        entrada = f.read()
    
except:
    entrada = data

invalido = 0
print(" - - - - - - - - - - ANALISE LEXICA - - - - - - - - - -\n\n\n")
tok = lexer.input(data)
while True:
    try:
        tok = lexer.token()
        if not tok:
            if invalido != 0:
                print("\n\nCodigo Invalido!!\nForam apresentados %s erros" % invalido)
            break      # No more input
        print(tok)
    except :
        invalido +=1
        tok.lexer.skip(1) 
        #print("Codigo Invalido!!")
        #break

print("\n\n\n\n - - - - - - - - - - ANALISE SINTATICA - - - - - - - - - -\n\n\n")

if invalido == 0:
    while True:
        try:
            t = parser.parse(entrada,lexer=lexer,debug=True) 
            if not t:
                print("\n\n\n\n - - - - - - - - - - CODIGO VALIDO! - - - - - - - - - - ")
                break
        except error:
            print("\n\n\n\n - - - - - - - - - - CODIGO INVALIDO! - - - - - - - - - - ")
            break


