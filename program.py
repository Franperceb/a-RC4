import fileinput

#2 digits hexadecimal
def ToHexadecimal(n): 
	hexadecimal = hex(n).split('x')[1]
	if len(hexadecimal) < 2:
		hexadecimal = "0" + hexadecimal
	return hexadecimal.upper()

#Key Scheduling Algorithm.
def KSA(k): 
	key = [ord(c) for c in k]
	permutation = [] #S
	j = 0

	for i in range(0,256):
		permutation.append(i)

	for i in range(0,256):
		j = (j + permutation[i] + key[i % len(k)]) % 256
   #Swapping values 
		aux = permutation[i] 
		permutation[i] = permutation[j]
		permutation[j] = aux
	return permutation

#Pseudorandom generation algorithm
def PRGA(S,size): 
	i  = 0
	j = 0
	for s in range (0,size):
		i = (i + 1) % 256
		j = (j + S[i]) % 256
    #swapping values
		aux = S[i]
		S[i] = S[j]
		S[j] = aux
		KeyEncrypted = S[(S[i] + S[j]) % 256]
		yield KeyEncrypted

def RC4(key,msg):
    encryptedMsg = ''
    S=KSA(key)
    counter = 0 #to get every character of the text.
    keyStream = PRGA(S,len(msg))
    #creating the encrypted output
    for i in keyStream:
        encryptedMsg += ToHexadecimal(ord(msg[counter])^i)
        counter += 1
    return encryptedMsg

#Alphagrader testing
lines = []
for line in fileinput.input():
    line = line.replace('\n','')
    lines.append(line)
    if(len(lines) == 2):
        print(RC4(lines[0],lines[1]))


