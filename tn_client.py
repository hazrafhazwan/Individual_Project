import socket
import sys
import os
import time

def typewritter(data): #animation
	for char in data:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)

def option(): #menu
	print("\n\t -----------------------------------------------------------")
	print("\t ||   Please choose an option you would like to choose!   ||")
	print("\t -----------------------------------------------------------")
	print("\t ||\t [1] See current directory   [cmd: pwd]           ||")
	print("\t ||\t [2] See list of directory   [cmd: ls]            ||")
	print("\t ||\t [3] Create a new directory  [cmd: mkdir]         ||")
	print("\t ||\t [4] Remove a file           [cmd: rm]            ||")
	print("\t ||\t [5] Remove a directory      [cmd: rmdir]         ||")
	print("\t ||\t [6] Rename a file           [cmd: mv]            ||")
	print("\t ||\t [7] Watch a movie in ascii (Star Wars)\t          ||")
	print("\t ||\t [c] Clear Screen            [cmd: clear]         ||")
	print("\t ||\t [0] Exit system \t\t                  ||")
	print("\t -----------------------------------------------------------\n")

os.system('clear') #clear screen
hostnum = input("\tEnter the ip address you wanted to connect: ")

#creating socket
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = hostnum
port = 8787

#connecting to server socket
typewritter(f'\t>> Connecting with host {host}:{port} \n')
clientSock.connect((host,port))
typewritter("\t[+] Connected successfully!\n")

#message for server
msg = "\tHello Server,its me, The Client, i am already connected to you!\n"
clientSock.send(msg.encode()) #1

#receive opening message from server
msgFromServer = clientSock.recv(1024)
print(msgFromServer.decode()) #2

while True:
	option()
	msg=input("\tOption number: ")
	clientSock.send(str.encode(msg)) #3

	#see directory or list all directory
	if msg == '1' or msg == '2' or msg == 'ls' or msg == 'pwd':
		response = clientSock.recv(1024)
		print(response.decode()) #4

	#make new directory
	elif msg == '3' or msg == 'mkdir':
		cmd = input("Name of directory that you wanted to create: ")
		clientSock.send(str.encode(cmd)) #3a

	#remove file
	elif msg == '4' or msg == 'rm':
		cmd = input("Name of file you want to remove: ")
		clientSock.send(str.encode(cmd)) #3a

	#delete directory
	elif msg == '5' or msg == 'rmdir':
		cmd = input("Name of directory you want to remove: ")
		clientSock.send(str.encode(cmd)) #3

	#rename file
	elif msg == '6' or msg == 'mv':
		cmd = input("Name of file you want to rename: ")
		cmd2 = input("Name that you want to rename the file: ")
		clientSock.send(str.encode(cmd))
		clientSock.send(str.encode(cmd2))

	#watch movie
	elif msg == '7':
		print("Enter <telnet towel.blinkenlights.nl> command to watch the movie \n")
		cmd = input("Enter command: ")
		clientSock.send(str.encode(cmd))

	#quit system
	elif msg == '0':
		print("The System will exit now, Thank You!")
		clientSock.close()
		sys.exit()

	#clear screen
	elif msg == 'c' or msg == 'clear':
		os.system('clear')

	else: #Unrecognize command
		print("Command/option not recognize!")

