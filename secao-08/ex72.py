"""
72. Considerando a estrutura:

struct Vetor{
float x;
float y;
float z;
};

para representar um vetor no R³, implemente uma função que calcule a soma de dois vetores. Essa
função deve obedecer ao protótipo:

void soma (struct Vetor* v1, struct Vetor* v2, struct Vetor* res);

onde os parâmetros v1 e v2 são ponteiros para os vetores a serem somados, e o parâmetro res é um
ponteiro para uma estrutura vetor onde o resultado da operação deve ser armazenado.

"""

def vetor(x, y, z):
    lis = list()
    lis.append(float(x))
    lis.append(float(y))
    lis.append(float(z))
    return lis
 
 
def soma(v1, v2, res):
    for i, z in zip(v1, v2):
        res.append(i + z)

    return res
 
 
vet1 = vetor(2, 3, 5)
vet2 = vetor(-3, 8, 9)
print(soma(vet1, vet2, []))
