#Exception handling 
try:
    f = open('somefile.txt', 'r')
    print(f.read())
    f.close()#never execute
except FileNotFoundError:
    print('file not found')
print("remaining lines of code")
	