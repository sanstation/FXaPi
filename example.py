from fxapi import Client

user = Client()

if user.login('USERNAME', 'PASSWORD'):
	print(f'Logged in as - {user.username}')
	user.create_thread(21, 'Test', 'Test')
