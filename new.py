from sys import argv
pwd = str(argv[1])
p = ''
for a in range(len(pwd)):
	z = ''
	if pwd[a] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLKMNOPQRSTUVWXYZ':
		p+= str(ord(pwd[a])).encode('utf-8').hex()[-1:-3:-2]#dechex utf8_encode() decbin() decoct()  in php
	elif pwd[a] in '1234567890':
		z=pwd[a]
		for s in range(int(pwd[a])):
			z+=str(s)
		p+= str(oct(int(z))).encode('utf-8').hex()[:2]
	else:
		p+= str(bin(ord(pwd[a]))).encode('utf-8').hex()[2:5]
password = ''
spec1="Q W E R T Y U I O P Z X C V B N M A S D F G H J K L ; ' \ , . / [ ] < > ? : | { } ' ".split(' ')
spec2=[chr(a) for a in range(33,48)]
for a in p:
	z=''
	try:
		if int(a)%2==0:
			password+=chr(int(a)+97)
			for i in range(0,27):
				if password[-1] not in ('ABCDEFGHIJKLKMNOPQRSTUVWXYZ,.1234567890'):
					z=spec2[i]
				else:
					z=spec1[i]
				if z not in password:
					password+=z
				else:
					continue
			else:
				if spec1[p.index(a)] not in password:
					password+=spec1[p.index(a)]
		else:
			password+=str(int(a)+p.index(a))
			for i in range(0,14):
				if password[-1] in ('ABCDEFGHIJKLKMNOPQRSTUVWXYZ,.1234567890'):
					z=spec2[i]
				else:
					z=spec1[i]
				if z not in password:
					password+=z
				else:
					continue
			else:
				if spec2[p.index(a)] not in password:
					password+=spec2[p.index(a)]
	except:
		if a in '13579':
			if spec2[int(a)] not in password:
				password+=spec2[int(a)]
		if a in '02468':
			if spec1[int(a)] not in password:
				password+=spec1[int(a)]
		else:
			if a not in password:
				password+=a
print(password)
