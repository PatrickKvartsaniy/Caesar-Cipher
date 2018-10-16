def cipher(s,n):
	if s>26:
		s=s%26
	caesar=''
	for i in n:
		if ord(i)>=ord('a') and ord(i)<=ord('z'):
			if ord(i)+s>ord('z'):
				caesar=caesar+chr((ord(i)+s)-26)
			else:
				caesar=caesar+chr(ord(i)+s)
		elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
			if ord(i)+s>ord('Z'):
				caesar=caesar+chr((ord(i)+s)-26)
			else:
				caesar=caesar+chr(ord(i)+s)
		else:
			caesar=caesar+i
	return caesar

def write_result(result):
	with open('msg.txt', 'w') as f:
		f.write(result)

s=input("Key - ")
n=input("Text - ")

result = cipher(int(s),n)
write_result(result)
print(result)