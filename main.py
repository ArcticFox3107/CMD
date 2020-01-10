drive = "C:"
current = "/"
fheader = "Name          Type       Size"
while True :
	command = input("C:" + current + "> ")
	if command == "help" :
		print('''help - Opens this menu.
dir - Shows contents of current location.
cd - Moves to a location.
''')

	if command == "dir" :
		if current == "/" :
			print(fheader + '''
Documents     Folder     63kb
Downloads     Folder     82kb''')
		elif current == "/Documents/" :
			print(fheader + '''
essay.txt     File       63kb''')
		
	elif command == "cd Documents" or "cd C:/Documents/" :
		if current == "/" :
			current = "/Documents/"
		else :
			print("Invalid location.")

	elif command == "cd.." :
		if current == "/" :
			print("Invalid command.")
		else :
			current = "/"
	else :
		print("Invalid command.")
		#s