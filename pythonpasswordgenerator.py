#importing strings and random modules
import string, random
def generatePassword(num):
	password = ''

	for n in range(num):
		x = random.randint(0,89)
		password += string.printable[x]

	return password
print generatePassword(19)
