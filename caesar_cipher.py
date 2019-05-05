## Coded by Kareem Soliman (afternoon session) and Farshed Adib (morning session)
## MIDTERM PROJECT
## Caesar Cipher
## 11/28/17
## CSC 11300

import random
def shift(r, n, specialCharacter):

        for i in range (len(r)):

                if (r[i] == specialCharacter):
                        specialCharIndex.append(i)
                        continue
                
                if (r[i] in l):
                    
                        if ((letters[r[i]] + n) > 51):
                                diff1 = (letters[r[i]] + n) - 51
                                r[i] = l[-1 + diff1]
                                
                        else:
                                r[i] = l[letters[r[i]] + n]
        return r

def UNshift(r, n, specialCharacter):

        for i in range (len(r)):

                if (r[i] == specialCharacter and i in specialCharIndex):
                    continue

                if (r[i] in l):

                        if ((letters[r[i]] - n) < 0):
                                diff2 = abs(letters[r[i]] - n)
                                r[i] = l[52 - diff2]

                        else:
                                r[i] = l[letters[r[i]] - n]
        return r
                
def specialChar():
        import random
        specialAlphaOrd = random.choice([random.randrange(65,90), random.randrange(97,122)])
        specialAlphaChr = chr(specialAlphaOrd)
        return specialAlphaChr

def randomShift():
        n = random.randrange(-1,25)
        return n

letters = dict()
l = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
for i in range(len(l)):
        letters[l[i]] = i

specialCharIndex = list()

text = input('Enter the name and extension of the document you want to encrypt (Ex. "text.txt"): ')
print()

with open(text, 'r+') as t:
        read = t.read()
        r = list(read)
        t.close()

specialCharacter = specialChar()
n = randomShift()
shift(r,n,specialCharacter)
encrypted = ''.join(r)

with open(text, 'w+') as t:
        t.write(encrypted)
        t.close()

with open("key.txt",'w+') as k:
        k.write(str(n))
        k.write(' ')
        k.write(specialCharacter)
        k.close()

print('Document successfully encrypted!')
print()


##yes_no = False
##while (yes_no == False):
##        selection = input('Decrypt file? (y/n) ')
##
##        if (selection == 'y' or 'n'):
##                yes_no = True
##                if (selection == 'n'):
##                        print()
##                        print('Your file is secure. Goodbye!')
##                else:
##                        yes_no = True
##                        print()
##                        with open(text, 'r') as t:
##                                r = list(t.read())
##                        with open("key.txt", 'r') as k:
##                                keyText = k.read()
##                                decryptionKeys = keyText.split()
##                        n_string = decryptionKeys[0]
##                        specialCharacter = decryptionKeys[1]
##                        n = int(n_string)
##                        UNshift(r,n,specialCharacter)
##                        with open("key.txt", 'w+') as k:
##                                k.write('')
##                                k.close()
##                        decrypted = ''.join(r)

        
selection = input('Decrypt file? (y/n) ')

if (selection == 'y'):
        print()
        with open(text, 'r') as t:
                r = list(t.read())
        with open("key.txt", 'r') as k:
                keyText = k.read()
                decryptionKeys = keyText.split()
        n_string = decryptionKeys[0]
        specialCharacter = decryptionKeys[1]
        n = int(n_string)
        UNshift(r,n,specialCharacter)
        with open("key.txt", 'w+') as k:
                k.write('')
                k.close()
        decrypted = ''.join(r)
        with open(text, 'w+') as j:
                j.write(decrypted)
                j.close()

if (selection == 'n'):
        print()
        print('Your file is secure. Goodbye!')

