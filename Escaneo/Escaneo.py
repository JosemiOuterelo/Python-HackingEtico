#!/usr/bin/python
# encoding: utf-8

# Importamos la biblioteca socket
import socket

# La funcion opcioneshost() solicita al usuario que introduzca un solo host una red entera
def opcioneshost():
	print 'SCRIPT PARA EL ESCANEO DE HOST'
        print '------------------------------'
	opcion = 3
	while(opcion > 2):
		print 'Elige una de las opciones:'
		print '1) Escanear host.'
		print '2) Escanear red completa.'
		print '0) Salir.'
		opcion = int(raw_input('Opcion: '))
	if opcion == 0:
		exit(0)
	else:
		return opcion

# La funcion opcionespuerto() solicita al usuario que especifice puerto, o puertos, a escanear
def opcionespuerto():
	i=0
	puerto = []
	while (i == 0):
		print 'Quieres especificar puerto a escanear?(S/N)'
		opcion = str(raw_input('--> '))
		if opcion == 'S':
			p = None
			while (isinstance(p,(int)) == False):
				try:
					p = int(raw_input('Puerto: '))
				except:
					print '***¡Error!'
					print '***¡Introduce un numero de puerto valido!'
			puerto.append(p)
			return puerto
			i=1
		if opcion == 'N':
# Si el usuario quiere indicar mas de un puerto, se crea una lista de los puertos del 1 al 1024
			for x in range(1,1024):
				puerto.append(x)
			return puerto
			i=1
		else:
			print '***Respuesta desconocida,vuelva a intentarlo.'
			i=0

# La funcion ipred(lista) de que tipo es la IP de la red introduciza por el usuario (Clase A, B o C)
# dependiendo de su mascara de red
def ipred(lista):
	print lista
	lista2 = lista[0].split('.')
	if lista[1] == '8':
		ip = str(lista2[0] + '.')
		tipo = 1
	if lista[1] == '16':
		ip = str(lista2[0] + '.' + lista2[1] + '.')
		tipo = 2
	if lista[1] == '24':
		ip = str(lista2[0] + '.' + lista2[1] + '.' + lista2[2] + '.')
		tipo = 3
	else:
		print 'Mascara de red no valida'
		exit(0)
	return ip,int(tipo)

# La funcion escaneo, como su nombre indica, empezara el escaneo de puertos de un host
def escaneo(host,puerto=None):
        print '\n'
        print ' Resultado del escaneo de %s' %host
        print '--------------------------------------'
        for p in puerto:
# Creamos un socket INET de tipo STREAM
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Comprueba si ha habido algun error en la conexion, devuelve 0 si la conexion se realizo correctamente
# en otro caso devuelve error en la conexion
                if s.connect_ex((host,int(p))):
                        print 'Puerto %s Cerrado' %(p)
                else:
                        print 'Puerto %s Abierto - ' %(p) + s.recv(1024)
# Cerramos el socket
                s.close()

# Funcion escanearhost(host,puerto) para el escaeno de un solo host
def escanearhost(host,puerto):
	socket.setdefaulttimeout(2)
	escaneo(host,puerto)

# Funcion escanearred(ip,puerto,tipo) para el escaneo de los host de una red
def escanearred(ip,puerto,tipo):
	socket.setdefaulttimeout(2)
	if tipo == 1:
		for x in range(0,255):
			for y in range(0,255):
				for z in range(1,255):
					host = ip + str(x) + '.' + str(y) + '.' + str(z)
					escaneo(host,puerto)
				
	if tipo == 2:
		for x in range(0,255):
			for y in range(1,255):
				host = ip + str(x) + '.' + str(y)
				escaneo(host,puerto)

	if tipo == 3:
		for x in range(1,255):
			host = ip + str(x)
			escaneo(host,puerto)
                

def main():
	op = opcioneshost()
	if op == 1:
		host = str(raw_input('Indica IP del host: '))
		puerto = opcionespuerto()
		escanearhost(host,puerto)
	if op == 2:
		red = str(raw_input('Indica IP de la red <IP>/<Mascara>: '))
		lista = red.split('/')
		while(len(lista) != 2):
			print 'Error de sintaxis'
			red = str(raw_input('Vuelva a introducir IP de la red <IP>/<Mascara>: '))
			lista = red.split('/')
		ip,tipo = ipred(lista)
		puerto = opcionespuerto()
		escanearred(ip,puerto,tipo)



if __name__ == '__main__':
	main()
