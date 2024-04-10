
try:
	f = open('somefile.txt', 'r')
	print(f.read())
	f.close()
	a=int(input('enter the value for a'))
	b=int(input('enter the value for b'))
	print('statement 1')
	res=a/b
	print(res)
except ZeroDivisionError: 
	print('denominator cannot be zero')
except ValueError: 
	print('Enter Only Numbers....')
except FileNotFoundError:
	print("there is no file...")
except Exception:
	print("some other exception")
print('remaining 1000 statements')