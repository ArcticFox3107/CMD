fheader = "Name          Type       Size"
help = '''help - Opens this menu.
dir - Shows contents of current location.
cd - Moves to a location.'''
while True :
	command = input("C:/> ")
	if command == "help" :
		print(help)
	
	elif command == "cd.." :
		print("Invalid location.")

	elif command == "cd" :
		print("Invalid command.")

	elif command == "dir" :
		print(fheader + '''
Documents     Folder     67kb
Downloads     Folder     89kb''')

	elif command == "cd Documents" :
		while True :
			command = input("C:/Documents/> ")
			if command == "help" :
				print(help)
			elif command == "cd.." :
				break
			elif command == "dir" :
				print(fheader + '''
hey.txt       TXT File   67kb''')
			
			elif command == "hey.txt" :
				print("I see you've found this file.\nGood on you!")
			else :
				print("Invalid command.")
	
	elif command == "cd S:/" :
		while True :
			command = input("S:/> ")
			if command == "help" :
				print(help)

			elif command == "dir" :
				print(fheader + '''
secret.txt    TXT File   3kb''')

			elif command == "secret.txt" :
				print("Nice job!")

			elif command == "cd C:/" :
				break

			else:print("Invalid command.")

	else :
		print("Invalid command.")