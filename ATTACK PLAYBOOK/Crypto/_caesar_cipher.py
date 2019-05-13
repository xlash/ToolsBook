import string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    alphabetUP = string.ascii_uppercase
    shifted_alphabetUP = alphabetUP[shift:] + alphabetUP[:shift]
    table = string.maketrans(alphabet + alphabetUP, shifted_alphabet + shifted_alphabetUP)
    return plaintext.translate(table)
