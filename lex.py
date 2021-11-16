# ------------------------------------------------------------
 # calclex.py
 #
 # tokenizer for a simple expression evaluator for
 # numbers and +,-,*,/
 # ------------------------------------------------------------
from typing import ClassVar
import ply.lex as lex
 
 # List of token names.   This is always required
token = [
    'numero',
    'ID',
    'add',
    'sub',
    'mlt',
    'divv',
    'men',
    'mai',
    'atr',
    'menig',
    'maiig',
    'ig',
    'dif',
    'pv',
    'vir',
    'apar',
    'fpar',
    'acol',
    'fcol',
    'acha',
    'fcha',
    #'comment1',
    #'comment2'
 ]

#t_IF = r'if'
#t_ELSE = r'else'
#t_INT = 'int'
#t_VOID = r'void'
#t_RETURN = r'return'
#t_WHILE = r'while'

reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'int' : 'INT',
   'void' : 'VOID',
   'return' : 'RETURN'
}

tokens = token + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z][a-zA-Z]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t


t_numero = r'[0-9][0-9]*'

t_add = r'\+'
t_sub = r'-'
t_mlt = r'\*'
t_divv = r'/'
t_men = r'<'
t_mai = r'>'
t_atr = r'='
t_menig = r'<='
t_maiig = r'>='
t_ig = r'=='
t_dif = r'!='
t_vir = r','
t_pv = r';'
t_apar = r'\('
t_fpar = r'\)'
t_acol = r'\['
t_fcol = r'\]'
t_acha = r'\{'
t_fcha = r'\}'
# Regular expression rules for simple tokens
 
# A regular expression rule with some action code

# Define a rule so we can track line numbers
def t_newline(t):
    r'[\n][\n]*'
    #t.lexer.lineno += len(t.value)
    pass

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])

def t_comment1(t):
    r'(/\*(.|\n)*?\*/)'
    pass

# Line comment
def t_comment2(t):
    r'(//.*?(\n|$))'
    pass

# Build the lexer
lexer = lex.lex()

# Testar

'''
data = 'int main(){}'
# Give the lexer some input
lexer.input(data)

cont = True
# Tokenize
invalido = 0
while cont == True:
    
    try:
        tok = lexer.token()
        if not tok:
            if invalido != 0:
                print("\n\nCodigo Invalido!!\nForam apresentados %s erros" % invalido)
            break      # No more input
        print(tok)
    except:
        invalido +=1
        tok.lexer.skip(1) 
        #print("Codigo Invalido!!")
        #break

'''