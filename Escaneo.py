#!/usr/bin/python
# encoding: utf-8

import socket

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
			for x in range(1,1024):
				puerto.append(x)
			return puerto
			i=1
		else:
			print '***Respuesta desconocida,vuelva a intentarlo.'
			i=0


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


def escanearhost(host,puerto):
	socket.setdefaulttimeout(2)
	print '\n'
	print ' Resultado del escaneo de %s' %(host)
	print '----------------------------------------'
	for p in puerto:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if s.connect_ex((host,int(p))):
			print 'Puerto %s Cerrado' %(p)
		else:
			print 'Puerto %s Abierto - ' %(p) + s.recv(1024)
		s.close()
	

def escanearred(ip,puerto,tipo):
	socket.setdefaulttimeout(2)
	if tipo == 1:
		for x in range(0,255):
			for y in range(0,255):
				for z in range(1,255):
					host = ip + str(x) + '.' + str(y) + '.' + str(z)
					print '\n'
					print ' Resultado del escaneo de %s' %host
					print '--------------------------------------'
					for p in puerto:
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						if s.connect_ex((host,int(p))):
							print 'Puerto %s Cerrado' %(p)
                				else:
							print 'Puerto %s Abierto - ' %(p) + s.recv(1024)
                				s.close()
				
	if tipo == 2:
		for x in range(0,255):
			for y in range(1,255):
				host = ip + str(x) + '.' + str(y)
				print '\n'
                		print ' Resultado del escaneo de %s' %host
                		print '--------------------------------------'
                		for p in puerto:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					if s.connect_ex((host,int(p))):
						print 'Puerto %s Cerrado' %(p)
					else:
						print 'Puerto %s Abierto - ' %(p) + s.recv(1024)
					s.close()

	if tipo == 3:
		for x in range(1,255):
			host = ip + str(x)
			print '\n'
			print ' Resultado del escaneo de %s' %host
			print '----------------------------------------'
			for p in puerto:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                		if s.connect_ex((host,int(p))):
					print 'Puerto %s Cerrado' %(p)
                		else:
					print 'Puerto %s Abierto - ' %(p) + s.recv(1024)
                		s.close()
                

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
