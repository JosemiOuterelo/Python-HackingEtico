#!/usr/bin/python

# Importamos el modulo paramiko con el que establecer conexions ssh facilmente
import paramiko
#import sys


def conexionssh(host):
# Abrimos nuestro fichero con las cuentas de usuarios en modo lectura
	file = open('cuentas.txt','r')
# Recorremos las lineas del fichero
	for linea in file.readlines():
		linea = linea.strip('\n')
# Separamos el nombre del usuario y el password
		cuenta = linea.split('/')
# Iniciamos un cliente SSH
		ssh = paramiko.SSHClient()
# Agregamos el host al listado de hosts conocidos
		ssh.load_system_host_keys()
# Establecemos la politica por defecto para localizar la llave del host localmente
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
# Nos conectamos al host usando el nombre de usuario y password obtenidos del fichero
			ssh.connect(host,username=cuenta[0],password=cuenta[1])
			print 'Conexion ssh establecida con la cuenta ' + linea
			ejecutar_comandos(ssh)
			print 'Conexion ssh finalizada.'
			break
		except:
			print '***Conexion ssh fallida con ' + linea
			print '\n'
			continue
# Cerramos el fichero una vez abierto y recorrido
	file.close()

def ejecutar_comandos(ssh):
	i = 1
	while(i == 1):
		print '1- Ejecutar comando.'
		print '2- Salir y cerrar conexion.'
		opcion = int(raw_input('> '))
		if opcion ==1 or opcion==2:
			if opcion == 1:
				comando = str(raw_input('Introduce comando: '))
# Ejecutamos el comando de forma remota y capturamos la entrada, salida y error estandar del host
				stdin, stdout,stderr = ssh.exec_command(comando)
# Imprimimos por pantalla la salida del comando y el error estandar, en el caso de que suceda
				print stdout.read()
				print stderr.read()
			if opcion == 2:
				i=0
		else:
			continue
# Cerramos la conexion SSH
	ssh.close()


def main():
	print ' SCRIPT PARA CONEXION SSH'
	print '--------------------------'
	host = raw_input('Introduce host: ')
	conexionssh(host)


if __name__ == '__main__':
        main()

