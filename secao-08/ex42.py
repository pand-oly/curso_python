"""
42. Faça uma função que receba um vetor de reais e retorne a média dele.

"""

vetor = [1.5, 5.3, 6.7, 9.2, 5.0, 3.9, 9.5]

def media(vetor):
    m = sum(vetor) / len(vetor)
    return "%.2f" % m
    
print(media(vetor))