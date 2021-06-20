import subprocess
import random
import sys
import os
import socket


def _start():

	if(len(sys.argv)<2):
		_help()
		print('Error : too few parameters')

	elif(sys.argv[1] in ['-help','-?']):
		_help()

	elif(sys.argv[1]=='-create'):
		try:
			foldername = sys.argv[2]
		except:
			rand = random.randint(1,999999)
			foldername = 'flo'+str(rand)
		print('Creating a new Wallet...')
		try:
			os.mkdir(foldername)
		except Exception as e: 
			print('Wallet Creation Failed : '+str(e))
			exit(0)
		print('Created wallet '+foldername)
		print('To use wallet : '+sys.argv[0]+' '+foldername)

	elif(len(sys.argv)<3):
		_help()
		print('Error : too few parameters (command missing)')

	elif(sys.argv[2] in ['flo-qt','flo-cli','flod']):
		
		#use this for find ip n available port using socket instead of random port
		localip=socket.gethostbyname(socket.gethostname())
		'''
		for p in range(0, 65535):
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
				if(!sock.connect_ex(('localhost', p)))
					port = p
					break;
		'''
		#localip = '0.0.0.0'
		port = str(random.randint(2000,10000))
		path=os.getcwd()
		cmd = ['./'+sys.argv[2]] + ['-conf='+path+'/'+sys.argv[1]+'/flo.conf','-datadir='+sys.argv[1],'-bind='+localip+':'+port] + sys.argv[3:]
		#print(cmd)
		subprocess.run(cmd)
	else:
		_help()
		print('Error : command '+sys.argv[2]+' not recognised')

def _help():
	help_data=f"""
FLO Core MultiWallet

Usage:

	{sys.argv[0]} -create [walletName]
		creates a wallet under 'walletName' if specified
		else creates wallet with name 'floxxxxxx'
	
	{sys.argv[0]} <walletName> <command> [option]
		executes the command in wallet 'walletName'

commands:

	flo-qt		-	open FLO Core Wallet
	flo-cli		-	run cli commands
	flod		-	run FLO daemon

for more info on each commands use option -help (or) -?

"""
	print(help_data)

_start()
