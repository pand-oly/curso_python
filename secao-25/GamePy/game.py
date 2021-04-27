from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível da dificuldade desejada: '))

    calc: Calcular = Calcular(dificuldade)
    
    print('Diga a resposta da seguinte operação: ')
    calc.mostrar_operacao()

    resultado = int(input('R: '))

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Pontuação: {pontos} ponto(s)')
    
    player: int = int(input("Deseja continuar ? ['1' - sim, '0' - não] "))

    if player:
        jogar(pontos)
    else:
        print(f'Fim: Você marcou {pontos} ponto(s)')
        print('Ate a próxima!')

if __name__ == '__main__':
    main()