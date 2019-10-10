#!/usr/bin/python
# encoding: utf-8

# Script sencillo para descifrar contraseñas encriptadas

# Importamos el modulo hashlib que permite cifrar con los algoritmos
# de hash seguros como SHA1, SHA224, SHA256, MD5, etc.
import hashlib

# Funcion abrirfichero(fichero) para recorrer fichero con las cuentas de usuario de las victimas.
def abrirfichero(fichero):
	for l in fichero.readlines():
		l = l.strip('\n')
		cuenta = l.split(':')
		descifrar(cuenta)

# Funcion tiposhash(password) para cifrar las contraseñas que tengamos guardadas en un fichero,
def tiposhash(password):
# Ciframos con el algoritmo md5, para ello creamos el objeto md5
	md5 = hashlib.md5()
# Actualizamos el objeto md5 con la contraseña codificada mediante encode() y la ciframos
	md5.update(password.encode())
# Ciframos con el algoritmo sha1
	sha1 = hashlib.sha1()
	sha1.update(password.encode())
# Ciframos con el algoritmo sha224
	sha224 = hashlib.sha224()
	sha224.update(password.encode())
# Ciframos con el algoritmo sha256
	sha256 = hashlib.sha256()
	sha256.update(password.encode())
# Ciframos con el algoritmo sha512
	sha512 = hashlib.sha512()
	sha512.update(password.encode())

	return md5,sha1,sha224,sha256,sha512

# Funcion comprobacion(cuenta,password,hash) que comprobara si la contraseña cifrada es
# igual a alguna de las contraseñas de las cuentas de usuario de la victima. 
def comprobacion(cuenta,password,hash):
# Mediante hexdigest() devolvemos la cadena cifrada en hexadecimal.
	if cuenta[1] == hash.hexdigest():
		print 'Contraseña encontrada: ' + password
		print cuenta[0] + ':' + cuenta[1] + ' -- Descifrada' + ' (' + hash.name + ')' + '--> ' + cuenta[0] + ':' + password
		print '\n'
	else:
		return

# Funcion descifrar(cuenta) que abrira el fichero con las contraseñas, lo recorrera y llamara
# a la funcion tiposhash(password) para cifrar cada una de ellas.
def descifrar(cuenta):
	p = open('passwords.txt','r')
	for l in p.readlines():
		password = l.strip('\n')
		md5,sha1,sha224,sha256,sha512 = tiposhash(password)
		for hash in [md5,sha1,sha224,sha256,sha512]:
# Comprobara para cada contraseña los diferentes algoritmos.
			comprobacion(cuenta,password,hash)
	return 

def main():
	print ' SCRIPT PARA DESCIFRAR CONTRASEÑAS'
	print '-----------------------------------'
	opcion = 3
	while(opcion == 3):
		print '1) Introducir fichero con las contraseñas de la victima.'
		print '2) Introducir manualmente una contraseña.'
		print '0) Salir.'
		
		opcion = int(raw_input('> '))
# Opcion si tenemos un fichero con las cuentas de usuario de las victimas.
		if opcion == 1:
			f = raw_input('Indica ruta del fichero: ')
			print '\n'
			try:
				fichero = open(f,'r')
			except:
				print '*** No se encuentra fichero en la ruta indicada.'
				break
			abrirfichero(fichero)
# Opcion si queremos introducir la cuenta manualmente.
		elif opcion == 2:
			cuenta = []
			u = str(raw_input('Usuario: '))
			p = str(raw_input('Contraseña: '))
			print '\n'
			cuenta.append(u)
			cuenta.append(p)
			descifrar(cuenta)

		elif opcion == 0:
			print 'Terminando script ...'
			break

		else:
			print 'Opcion no valida, vuelva a intentarlo.'
			opcion = 3
			continue




if __name__ == '__main__':
	main()
