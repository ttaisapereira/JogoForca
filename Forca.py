import random
from Biblioteca import animais, estados, comidas, roupas

print('BEM VINDO AO JOGO DA FORCA')
print()
print('Seu principal objetivo é acertar a palavra antes do bonequinho ser completado.\nPrepara-se para o desafio! \nQUE OS JOGOS COMECEM!')
print()
loop = True
usuario = input("Digite seu nome jogador: ").upper()
print(f'BEM VINDO, {usuario} ')
print('VAMOS LÁ!')
vitorias = 0
derrotas = 0
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def boneco(chances):
    if chances == 6:
        return f'___\n'
    if chances == 5:
        return f'___\n   @\n\n'
    if chances == 4:
        return f'___\n   @ \n   |\n'
    if chances == 3:
        return f'___\n   @ \n  /|\n'
    if chances == 2:
        return f'___\n   @ \n  /|\ \n'
    if chances == 1:
        return f'___\n   @ \n  /|\\\n  / \n'
    if chances == 0:
        return f'___\n   @ \n  /|\\\n  /\ \n'
def palavrasecreta(palavra, acertos):
    resultado = ''
    for letra in palavra:
        if letra in acertos:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado
while loop:
    palavras = animais + estados + comidas + roupas
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    if palavra in animais:
        dica = 'Dica: é um animal.'
    if palavra in estados:
        dica = 'Dica: é um estado.'
    if palavra in comidas:
        dica = 'Dica: é uma comida.'
    if palavra in roupas:
        dica = 'Dica: é uma roupa.'
    chances = 6
    acertos = []
    erros = []
    while chances > 0:
        print(dica)
        print(f'{palavrasecreta(palavra, acertos)}')
        print(f"Letras erradas: {', '.join(erros)}")
        while True:
            tentativa = input("• Digite uma letra: ").upper()
            c = 0
            for x in tentativa:
                if x not in alfabeto:
                    c += 2
                c += 1
            if c > 1:
                print('Você digitou uma letra ou um caractere inválido. Tente mais uma vez!')
            elif tentativa in acertos or tentativa in erros:
                print(f'A letra {tentativa} já foi digitada, tente novamente!')
            else:
                break
        if tentativa in palavra:
            acertos.append(tentativa)
            if all(letra in acertos for letra in palavra):
                print(' ')
                print(f'Parabéns {usuario}, você acertou!\nA palavra era: {palavra}.')
                vitorias += 1
                break
        else:
            erros.append(tentativa)
            chances -= 1
            print(f'Letra incorreta.\n')
        print(boneco(chances))
    if chances == 0:

        print(f'Você errou ! A palavra era: {palavra}.')
        derrotas += 1
    questao = input('Deseja jogar novamente? (s/n): ')
    if questao.lower() == 'n':
        loop = False
print(' ')
print(f'Jogo finalizado com sucesso!\nObrigado por jogar {usuario} ☻')
print(' ')
print(f'Sua pontuação final foi de:\nVitórias: {vitorias}\nDerrotas: {derrotas}\nATÉ MAIS ☻☻☻')