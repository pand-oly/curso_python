"""
71. Considerando a estrutura:

struct Ponto{
int x;
int y;
};

para representar um ponto em uma grade 2D, implemente uma função que indique se um ponto p está
localizado dentro ou fora de um retângulo. O retângulo é definido por seus vértices inferior
esquerdo v1 e superior direito V2. A função deve retornar 1 caso o ponto esteja localizado dentro
do retângulo e O caso contrário. Essa função deve obedecer ao protótipo:

int dentroRet (struct Ponto* vi, struct Ponto* v2, struct Ponto* p);

"""

def ponto(x, y):
    return int(x), int(y)
 
 
def verifcar(v1=(0,0), v2=(0,0), p =(0, 0)):
    if v1[0] < p[0] < v2[0]:
        if v1[1] < p[1] < v2[1]:
            return 1
    return 0
 
 
v01 = ponto(3, 2)
v02 = ponto(6, 8)
p01 = ponto(4, 5)
 
print(verifcar(v01, v02, p01))
