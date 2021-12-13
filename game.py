from models.calcular import Calcular


def calculator_master() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:

    dificuldade: int = int(input('Informe o nivel de dificuldade desejado [1, 2, 3, 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado par a seguinte operaçao: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo? [1 = sim, 0 - não] '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).\nAté mais')


if __name__ == '__main__':
    calculator_master()
