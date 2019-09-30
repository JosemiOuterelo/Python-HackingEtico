#!/usr/bin/python

import paramiko
import sys

PROMPT = ['# ','> ','\$ ','>>> ']


def conexionssh(host):
	file = open('cuentas.txt','r')
	for linea in file.readlines():
		linea = linea.strip('\n')
		cuenta = linea.split('/')
		conn = 'ssh ' + cuenta[0] + '@' + host
		ssh = paramiko.SSHClient()
		ssh.load_system_host_keys()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			ssh.connect(host,username=cuenta[0],password=cuenta[1])
			print 'Conexison ssh exitosa con la cuenta ' + linea
			print '\n'
			ejecutar_comandos(ssh)
		except:
			print '*** Conexion fallida con la cuenta ' + linea
			print '\n'
			continue

def ejecutar_comandos(ssh):
	opcion = 3
	while(opcion != 1 and opcion !=2):
		print '1- Ejecutar comando.'
		print '2- Salir y cerrar conexion.'
		opcion = int(raw_input('> '))
	if opcion == 1:
		comando = str(raw_input('Introduce comando: '))
		stdin, stdout,stderr = ssh.exec_command(comando)
		print stdout.read()
		ssh.close()
		sys.exit(0)
	if opcion == 2:
		ssh.close()
		sys.exit(0)


def main():
	print ' SCRIPT PARA CONEXION SSH'
	print '--------------------------'
	host = raw_input('Introduce host: ')
	conexionssh(host)


if __name__ == '__main__':
        main()

