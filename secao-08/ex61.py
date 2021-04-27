"""
61. Escreva uma função que compare e retorne verdadeiro, caso uma string seja anagrama
da outra, e falso, caso contrario.

"""

def anagrama(str1, str2):
    if str1.lower() == str2.lower()[::-1]:
        return True
    return False

s1 = 'amor'
s2 = 'Roma'

print(anagrama(s1, s2))
