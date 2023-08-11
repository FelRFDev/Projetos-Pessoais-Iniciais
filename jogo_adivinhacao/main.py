from random import randint



vidas_banner = """
██╗   ██╗██╗██████╗  █████╗ ███████╗
██║   ██║██║██╔══██╗██╔══██╗██╔════╝
██║   ██║██║██║  ██║███████║███████╗
╚██╗ ██╔╝██║██║  ██║██╔══██║╚════██║
 ╚████╔╝ ██║██████╔╝██║  ██║███████║
  ╚═══╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝
"""


player_lifes_stages = {

3:f"""
{vidas_banner}
,-.-. ,-.-. ,-.-. 
`. ,' `. ,' `. ,'
  `     `     `
""", 


2 :f"""
{vidas_banner}
,-.-. ,-.-.
`. ,' `. ,'
  `     `
""",

1 : f"""
{vidas_banner}
,-.-.
`. ,'
  `
"""

}


numero_sorteado = randint(1, 10)

jogador = input('Informe o seu nome: ').strip().title()

vidas = 3

print(player_lifes_stages[vidas])

print(f'Bem vindo ao jogo de adivinhação {jogador}!' 
      '\nMostre que você é fera e adivinhe o número sorteado pelo computador.')

while True:
    escolha_jogador = int(input(f'\nDigite um número: '))
    if vidas == 1 and escolha_jogador != numero_sorteado:
        vidas -=1
        print(f'Total de vidas = {vidas}')
        print(' -=-=-=-=-=-=-= GAME OVER! -=-=-=-=-=-=-=')
        break

    elif escolha_jogador != numero_sorteado and vidas > 0:
        print()
        vidas -=1
        print(player_lifes_stages[vidas])
        print('(っ˘̩ ╭╮˘̩)っ Que pena você errou! Tente novamente °՞(ᗒᗣᗕ)՞°')

   
    elif escolha_jogador == numero_sorteado:
        print(""" 
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
           `"""""""` """)
        print(f'Número sorteado: [{numero_sorteado}] - Número digitado por {jogador}: [{escolha_jogador}] - PARABENS VOCÊ ACERTOU!')
        break
    
