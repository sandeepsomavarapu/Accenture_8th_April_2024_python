class InvalidUserException(Exception):#Code Reusability
	def __init__(self,message1):
   		print(message1)

username = input('Enter Username:')
password = input('Enter password:')

if username=='accenture' and password=='india@123':
    print('welcome mr!  ',username)
else:
	raise InvalidUserException('enter valid credentials')	

