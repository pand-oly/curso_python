"""
68. Faça uma função que receba duas strings e retorne a intercalação letra a letra da primeira
com a segunda string. A string intercalada deve ser retornada na primeira string.

"""

def intercala(s1, s2):
    s = ''    
    if len(s1) < len(s2):
        for i in range(len(s1)):
            s += s1[i] + s2[i]
        
        for i in range(len(s1), len(s2)):
            s += s2[i]
    
    elif len(s2) < len(s1):
        for i in range(len(s2)):
            s += s1[i] + s2[i]
        
        for i in range(len(s2), len(s1)):
            s += s1[i]
    
    else:
        for i in range(len(s1)):
            s += s1[i] + s2[i]
        
    s1 = s
    return s1
    

s1 = '13579'
s2 = '24681012'
print(intercala(s1, s2))
