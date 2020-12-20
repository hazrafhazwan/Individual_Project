import socket
import sys
import time
import os

def typewritter(data):
	for char in data:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)


os.system('clear') #clear screen

#creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
typewritter('\t[+] Socket has been successfully created!\n')

port = 8787
host = ''
s.bind((host,port))
typewritter('\t[+] Socket has been successfully binded at port: ' + str(port) + '\n')

#listening to port
s.listen(5)
typewritter('\t>> Socket is listening.. \n\n')

#accepting connection
conn,addr = s.accept()
typewritter("\tSuccessfully Connected to " + str(addr) + "\n")

#Receive opening message from client
ms = conn.recv(1024) 
print(ms.decode('utf-8'))

#Send message to client
conn.send(("\n\t\t ||| Hello welcome to Telnet server! |||").encode('utf=8')) #2

while True:
	data = conn.recv(1024)
	print("[Logs]: Client Choosed option: " + str(data.decode())) #3
	op = str(data.decode())

	if op == '1' or op == 'pwd': #see directory
		print("  Option 1 / pwd : Directory")
		print("  Showing current directory\n")
		reply = str(os.getcwd())
		conn.send(reply.encode()) #4

	elif op == '2' or op == 'ls': #list all directory
		print("  Option 2 / ls : List Directory")
		print("  Showing list of directory\n")
		reply = str(os.listdir())
		conn.send(reply.encode()) #4

	elif op == '3' or op == "mkdir": #make new directory
		print("  Option 3 / mkdir : New Directory")
		data = conn.recv(1024)
		os.mkdir(str(data.decode()))
		typewritter("  Making new directory .................. \n")
		print('  Directory has been created\n')

	elif op == '4' or op == "rm": #remove file
		print("  Option 4 / rm : Remove file")
		data = conn.recv(1024)
		os.remove(str(data.decode()))
		typewritter("  Deleteing file .................. \n")
		print("  File has been deleted!\n")

	elif op == '5' or op == "rmdir": #delete directory
		print("  Option 5 / rmdir : Delete Directory")
		data = conn.recv(1024)
		os.rmdir(str(data.decode()))
		typewritter("  Deleteing directory .................. \n ")
		print("  Directory has been successfully deleted!\n")

	elif op =='6': #rename file
		data = conn.recv(1024)
		data2 = conn.recv(1024)
		os.rename(str(data.decode()) , str(data2.decode()))
		print("  Option 6 / mv : Rename file")
		typewritter("  Renaming file ..................  ")
		print("  File has been successfully rename!\n")

	elif op == '7': #watch movie
		data = conn.recv(1024)
		print("  Option 7 : Watch movie in ascii ")
		typewritter("  Enjoy the movie!......................\n")
		os.system(str(data.decode()))

	elif op == 'c' or op == 'clear': #clear screen
		typewritter("Clearing screen..................")
		os.system('clear')

	elif op == '0': #quit system
		print("  Server is exiting, See you again!\n")
		conn.close()
		sys.exit()

	else: #unrecognize command
		print("  Command not recognize!\n")
