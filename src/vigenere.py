def main(args):
	if len(args) != 3:
		printUsage
	elif args[0] == '-e':
		encrypt(args[1], args[2])
	elif args[0] == '-d':
		decrypt(args[1], args[2])
	else:
		printUsage
def printUsage:
	print """
	Usage: main -e <srouce string> <cipher> //Encrypt source string with the cipher by vigenere algorithm;
	       main -d <encrypted string> <cipher> //Decrypt encrypted string with the cipher by vigenere algorithm;
	"""
def encrypt(srcStr, cipher):
	result = ''
	j = 0
	for i in range(len(srcStr)):
		c = srcStr.upper()[i]
		if isUpperLetter(c):
			result += encryptChar(c, cipher.upper()[j%len(cipher)])
		else:
			result += ' '
		j+=1
		return result
def encryptChar(sc, cc):
	chr((((sc - 'A'[0]) + (cc - 'A'[0])) % 26) + 'A'[0])
	
def decrypt(encStr, cipher):
	result = ''
	j = 0
	for i in range(len(encStr)):
		c = encStr.upper()[i]
		if isUpperLetter(c):
			result += decryptChar(c, cipher.upper()[j%len(cipher)])
		else:
			result += ' '
		j+=1
		return result
def decryptChar(ec, cc):
	chr((((ec + 26) - cc) % 26) + 'A'[0])
def isUpperLetter(c):
	if c >= 'A'[0] and c<= 'Z'[0]:
		true
	else:
		false
if __name__ == "__main__"
	import sys
	main(sys.argv)