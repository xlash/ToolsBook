import string
import base64

# Will apply a transposition filter to letters. 
# Will also try every 26 letters matching on the filter to determine which one is A, B, C, etc.
ciphertext = 'OUVFQURpXl5BMkRFNjM6P100QD5eZkNxYkVzcnI='
transmap = 'avknqpdwycuoesglbizhjmftrx'

alphabet = string.ascii_lowercase
alphabetUP = string.ascii_uppercase


def permutation(plaintext, permuted_lowercase):
    permuted_lower_and_upper = permuted_lowercase + permuted_lowercase.upper()
    table = str.maketrans(string.ascii_letters, permuted_lower_and_upper)
    return plaintext.translate(table)

print(ciphertext)
for i in range(0, 26):
    permuted = permutation(ciphertext, transmap[i:] + transmap[:i])
    print("%s::%s  => %s" % (i, permuted, base64.b64decode(permuted)))
    for encoding in ['ascii', 'utf-8', 'utf-16', 'utf-32', 'ISO-8859-1','Windows-1251','Shift JIS','Windows-1252']:
        try:
            decoded = base64.b64decode(permuted).decode(encoding)
            print('           %s ==> %s' % (encoding, decoded))
        except UnicodeDecodeError as e:
            pass



# from pyDes import *

# data = "Please encrypt my data"
# k = des(transmap, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
# print("Decrypted: %r" % k.decrypt(ciphertext, padmode=PAD_PKCS5))
