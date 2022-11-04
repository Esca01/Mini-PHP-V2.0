#Sergio Ospina Zuluaga 
#Esteban Escalante Cordoba
#Juan Andres Obando Davila
import sys
import ply.yacc as yacc
import mini_php
from mini_php import tokens


VERBOSE = 1

precedence = (
    ('left', 'INCLUDE', 'REQUIRE'),
    ('left', 'COMMA'),
    ('left', 'EQUAL', 'PLUSEQUAL', 'MINUSEQUAL'),
    ('left', 'SEMI'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
    ('nonassoc', 'ISEQUAL', 'DEQUAL'),
    ('nonassoc', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'LBRACKET'),
    ('nonassoc', 'NEW', 'CLONE'),
    ('left', 'ELSEIF'),
    ('left', 'ELSE'),
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC'),
)

def p_program(p):
    '''program : OPENTAG declaration_list CLOSETAG'''
    pass

def p_declaration_list(p):
   '''declaration_list : declaration_list  declaration
   					   | declaration
   '''
   pass

def p_declaration(p):
	'''declaration : var_declaration
				   | fun_declaration
				   | area fun_declaration
				   | header_declaration
				   | class_declaration
				   | echo_stmt
				   | selection_stmt
			     | iteration_stmt
				   | typeclass
           | comments
	'''
	pass

def p_echo_stmt(p):
	'''echo_stmt : echo_stmt ECHO STRING SEMI
				 | echo_stmt ECHO VARIABLE SEMI
				 | empty
				 | echo_stmt ECHO NUM SEMI
				 | echo_stmt ECHO boolean SEMI
				 | echo_stmt ECHO fun_declaration SEMI
	'''
	pass

def p_header_declaration(p):
	'''header_declaration : REQUIRE LPAREN STRING RPAREN SEMI
                          | INCLUDE LPAREN STRING RPAREN SEMI
    '''
	pass

def p_class_declaration(p):
	'''class_declaration : area CLASS ID LBLOCK attribute RBLOCK
						 | CLASS ID LBLOCK attribute RBLOCK
             | CLASS ID LBLOCK RBLOCK
             | CLASS ID EXTENDS ID LBLOCK attribute RBLOCK
             | CLASS ID EXTENDS ID LBLOCK RBLOCK
	'''
	pass

def p_attribute1(p):
	'''attribute : attribute area var_declaration
				 | area var_declaration
				 | attribute area fun_declaration
				 | area fun_declaration
	'''
	pass

def p_comments(p):
	'''comments : COMMENTS
	'''
	pass


def p_area(p):
	'''area : PRIVATE
			| PUBLIC
			| PROTECTED
	'''
	pass

def p_var_declaration(p):
	'''var_declaration : VARIABLE SEMI var_declaration
                       | VARIABLE SEMI
                       | TIMESTIMES VARIABLE SEMI
                       | TIMESTIMES VARIABLE SEMI var_declaration
                       | VARIABLE EQUAL NUM SEMI var_declaration
                       | VARIABLE EQUAL NUM SEMI
                       | VARIABLE EQUAL boolean SEMI var_declaration
                       | VARIABLE EQUAL boolean SEMI
                       | VARIABLE EQUAL VARIABLE SEMI var_declaration
                       | VARIABLE EQUAL VARIABLE SEMI
                       | AMPERSANT VARIABLE SEMI var_declaration
                       | AMPERSANT VARIABLE EQUAL VARIABLE SEMI  selection_stmt
                       | AMPERSANT VARIABLE SEMI
                       | VARIABLE EQUAL simple_expression SEMI
	'''
	pass

def p_fun_declaration(p):
	'''fun_declaration : FUNCTION ID LPAREN params RPAREN
					   | FUNCTION ID LPAREN params RPAREN compount_stmt
	'''
	pass

def p_params(p):
	'''params : param_list
			  | empty
	'''
	pass

def p_param_list(p):
	'''param_list : param_list COMMA param_list
				  | param
	'''
	pass

def p_param(p):
	'''param : VARIABLE
             | VARIABLE LBRACKET RBRACKET
    '''
	pass


def p_compount_stmt(p):
	'compount_stmt : LBLOCK echo_stmt local_declarations echo_stmt statement_list echo_stmt RBLOCK'
	pass

def p_local_declarations(p):
	'''local_declarations : local_declarations var_declaration
						  | empty
	'''
	pass

def p_statement_list(p):
	'''statement_list : statement_list statement
					  | empty
	'''
	pass

def p_statement(p):
	'''statement : expression_stmt
				 | compount_stmt
				 | selection_stmt
				 | iteration_stmt
			     | return_stmt
			     | class_declaration
				 | echo_stmt
	'''
	pass

def p_expression_stmt(p):
	'expression_stmt : expression SEMI'
	pass


def p_selection_stmt_1(p):
	'''selection_stmt : IF LPAREN expression RPAREN statement
					  | IF LPAREN expression RPAREN statement selection

	'''
	pass

def p_selection(p):
	'''selection : ELSE statement
				 | ELSEIF statement selection
	 '''
	pass

def p_selection_stmt_2(p):
	'''selection_stmt : SWITCH LPAREN var RPAREN statement
					  | CASE NUM COLON statement BREAK SEMI
					  | DEFAULT COLON statement BREAK SEMI

	'''
	pass

def p_iteration_stmt_1(p):
	'iteration_stmt : FOR LPAREN var_declaration SEMI expression SEMI additive_expression RPAREN statement '
	pass
def p_iteration_stmt_2(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN statement'
	pass

def p_iteration_stmt_3(p):
	'iteration_stmt : DO LBLOCK statement SEMI RBLOCK WHILE LPAREN expression RPAREN'
	pass


def p_return_stmt(p):
	'''return_stmt : RETURN SEMI
				   | RETURN expression SEMI
	'''
	pass

def p_expression(p):
	'''expression : var EQUAL expression
				  | simple_expression
				  | var EQUAL AMPERSANT VARIABLE
			      | expression AND expression
				  | expression OR expression
	'''
	pass

def p_var(p):
	'''var : VARIABLE
		   | VARIABLE LBRACKET expression RBRACKET
	'''
	pass


def p_simple_expression(p):
	'''simple_expression : additive_expression relop additive_expression
						 | additive_expression
	'''
	pass

def p_relop(p):
	'''relop : LESS
			 | LESSEQUAL
			 | GREATER
			 | GREATEREQUAL
			 | DEQUAL
			 | DISTINT
			 | ISEQUAL
	'''
	pass

def p_additive_expression(p):
	'''additive_expression : additive_expression addop term
    					   | term
    					   | term MINUSMINUS
    				       | term PLUSPLUS
	'''
	pass

def p_addop(p):
	'''addop : PLUS
			 | MINUS
	'''
	pass

def p_term(p):
	'''term : term mulop factor
			| factor
	'''
	pass

def p_mulop(p):
	'''mulop : TIMES
			 | DIVIDE
	'''
	pass

def p_factor(p):
	'''factor : LPAREN expression RPAREN
			  | var
			  | NUM
			  | boolean
			  | VARIABLE LPAREN args RPAREN
	'''
	pass

def p_args(p):
	'''args : args_list
			| empty
			| VOID
	'''
	pass

def p_args_list(p):
	'''args_list : args_list COMMA expression
				 | expression
	'''
	pass

def p_boolean(p):
	'''boolean : TRUE
			   | FALSE
	'''
	pass

def p_tclass(p):
	'typeclass : ID VARIABLE EQUAL NEW constructor SEMI'
	pass

def p_costructor(p):
	'''constructor : ID LPAREN RPAREN
				   | ID LPAREN args RPAREN
	'''
	pass

def p_empty(p):
	'empty :'
	pass

cont = 0

def p_error(t):
  global cont  
  if VERBOSE:
        if t is not None:
            print ("ERROR SINTACTICO EN LA LINEA " + str(t.lexer.lineno) + " NO SE ESPERABA EL TOKEN  " + str(t.value))
            cont+=1
        else:
            print ("ERROR SINTACTICO EN LA LINEA: " + str(mini_php.lexer.lineno))
            cont+=1
  else:
        raise Exception('syntax', 'error')
        cont+=1

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.php'

	f = open(fin, 'r')
	data = f.read()
	parser.parse(data, tracking=True)
	if cont < 1:
	  print("Compila mani")
	