import random
from time import sleep

#-===============> PALETA DE CORES <==================-
"""Dicionário criado para facilitar o uso de cores dentro do programa. Para adicionar
alguma cor, basta "chamar" o nome do dicionário seguido da cor desejada. EX cores[preto]"""
cores = {
    'preto' : '\033[1;30m',
    'vermelho' : '\033[1;31m',
    'verde' : '\033[1;32m',
    'vermelho claro' : '\033[1;91m',
    'verde claro' : '\033[1;92m',
    'negrito' : '\033[;1m',
    'azul' : '\033[1;34m',
    'amarelo' : '\033[1;33m',
    'semcor' : '\033[m'
}

def SimpleBD(nomeArq,tipoDado):
    """Função para criar banco de dados utilizando 1 arquivo de extensão txt e
        com uma pequena verificação para saber se o programa deve criar o arquivo ou se o mesmo já foi criado.
        Retorna uma mensagem ao usuário informando se o arquivo foi criado ou se foi carregado caso já exista.

        Tem como parâmetros:
        - nomeArq: Nome do arquivo
        - tipoDado: tipo de dado a ser salvo para informar ao usuário no momento em que criar o banco de dados.
        """

    try:
        with open(nomeArq,'r'):
            print(f'Banco de dados para {tipoDado} Carregado com {cores["verde"]}SUCESSO!{cores["semcor"]}')

    except FileNotFoundError:
        with open(nomeArq,'a+'):
            print(f'Banco de cados para {tipoDado} Criado com {cores["verde"]}SUCESSO!{cores["semcor"]}')

    except:
        print('Algum erro impossibilitou que o banco de dados fosse criado! '
              'Informe o erro ao resposnável pelo programa!')


def CriaBD(nomeArq1,nomeArq2,tipoDado1,tipoDado2):
    """Função para criar banco de dados utilizando 2 arquivos de extensão txt e
    com uma pequena verificação para saber se o programa deve criar os arquivos ou se os mesmos já foram criados.
    Retorna uma mensagem ao usuário informando se os arquivos foram criados ou se foram carregados caso já existam.

    Tem como parâmetros:
    - nomeArq1 /nomeArq2: Nome do arquivo
    -- tipoDado: tipo de dado a ser salvo para informar ao usuário no momento em que criar o banco de dados.
    """
    try:
        with open(nomeArq1,'r'):
            print(f'Banco de Dados para {tipoDado1} Carregado com {cores["verde"]}SUCESSO!{cores["semcor"]}')

        with open(nomeArq2,'r'):
            print(f'Banco de Dados para {tipoDado2}  Carregado com {cores["verde"]}SUCESSO!{cores["semcor"]}')

    except FileNotFoundError:
        with open(nomeArq1,'a+'):
            print(f'Banco de dados para {tipoDado1} Criado com {cores["verde"]}SUCESSO!{cores["semcor"]}')

        with open(nomeArq2,'a+'):
            print(f'Banco de dados para {tipoDado2} Criado com {cores["verde"]}SUCESSO!{cores["semcor"]}')
    except:
        print('Algum erro impossibilitou que o banco de dados fosse criado! '
              'Informe o erro ao resposnável pelo programa!')





def menu_princ(lista,msg):
    """Função para criar um menu, que recebe uma lista para a estrutura de opções,
    e imprime uma mensagem acima do menu."""
    print(f'{cores["negrito"]}{cores["preto"]}----=<<<<<<<<<<<<{cores["semcor"]}{cores["amarelo"]}{msg}{cores["semcor"]}{cores["negrito"]}{cores["preto"]}>>>>>>>>>>>>=--')
    for i,v in enumerate(lista):
        print(f'{cores["negrito"]}{cores["preto"]}{i + 1}{cores["semcor"]} - {v}')
    esc = int(input('Sua escolha: '))
    print("\n" * 130)  # => testar
    return esc


def menu(lista, msg):
    print(f'{cores["negrito"]}{cores["preto"]}----=<<<<<<<<<<<<{cores["semcor"]}{cores["amarelo"]}{msg}{cores["semcor"]}{cores["negrito"]}{cores["preto"]}>>>>>>>>>>>>=----{cores["semcor"]}')
    for indice,itens in enumerate(lista):
        print(f'{cores["negrito"]}{cores["preto"]}{indice+1}{cores["semcor"]} - {itens}')
    esc = int(input('Sua escolha: '))
    print("\n" * 130)    # => testar
    return esc


def mensagemerro():
    """Função simples para exibir uma mensagem de erro na tela para o usuário."""
    print('=============================================================================')
    print(
        f'{cores["vermelho"]}ERRO, OPÇÃO INVÁLIDA! VOCÊ DEIXOU A OPÇÃO EM BRANCO OU NÃO DIGITOU UM NÚMERO!{cores["semcor"]}')
    print('=============================================================================')
    print('REINICIANDO...')
    print()
    sleep(1.5)



def pinta(cor,msg):
    """Função simples para pintar alguma mensagem com uma cor presente na 'paleta de cores' criada
    logo acima."""
    print(f'{cores[cor]}{msg}{cores["semcor"]}')



# ============================== <<<<< FERRAMENTAS PARA A ASSISTENTE VIRTUAL>>>>> =========================================



import time
import pyttsx3  #  => conversor de texto para fala
import speech_recognition as sr  # => utilizado para reconhecer e transcrever audios
import webbrowser   # => permite abrir qualquer tipo de navegador, geralmente abre o padrão!
import datetime
import pywhatkit   # => permite abrir e fazer pesquisas no youtube
# import os  # => Pode ser usado para pedir o assistente de voz para desligar o computador ou reiniciar
#import yfinance as yf # => trabalha com valores de preços
#import pyjokes
#primeira função: vai ouvir o que é dito no microfone e transcrever para texto
import wikipedia





def falatexto():
    while True:
        r = sr.Recognizer()  # => define qual fonte vai ser usada pra fazer a leitura  da fala
        with sr.Microphone() as fonte:  # => define qual recurso será utilizado para passar o áudio
            r.pause_threshold = 0.8  # => tempo de espera após a fala no microfone
            #print('Estou ouvindo...')
            fala = r.listen(fonte)  # => variável que vai ouvir e armazenar a fala
        try:
            q = r.recognize_google(fala, language="pt-BR")
            return q
        except sr.UnknownValueError:
            # print('Desculpe, não consegui entender!')
            continue
        except sr.RequestError:
            print('Desculpe, o serviço está offline!')
            continue
        except:
            # print('Desculpe, não consegui entender!')
            continue

def informanome():
    """Função que recebe o nome do usuário e emite uma saudação."""
    fala('Por favor, informe o seu nome')
    nometexto = falatexto()
    fala(f'Prazer em te conhecer {nometexto}!')



def fala(mensagem): # => função para converter o texto em fala recebendo uma mensagem de texto como parâmetro
    engine = pyttsx3.init()   # => inicia o mecaniscmo de conversão
    engine.say(mensagem)   # => função para iniciar a fala
    engine.runAndWait()  # => função para ler e falar o texto recebido


#função pra retornar o dia atual:

def informadia():
    data = datetime.date.today()
    dia = data.weekday() # => variável armazenando o número correspondente ao dia da semana ex: 0 = segunda, 1 = terça, etc
    mapeamento = {     # => fazendo ligação entre os números e os dias da semana com dicionário
        0:'Segunda',
        1:'Terça',
        2:'Quarta',
        3:'Quinta',
        4:'Sexta',
        5:'Sábado',
        6:'Domingo',
    }
    try:
        fala(f'Hoje é {mapeamento[dia]}!')
    except:
        pass


#função para informar a hora
def informahora():
    hora = datetime.datetime.now().strftime('%I:%M:%S')  # => função que captura as horas e converte em formato de horas padrão
    fala(f'Agora são {hora}!')  # => chama a função fala para falar as horas


#função para cumprimentar o usuário

def cumprimento():
    fala('''
    Iniciando sistemas! Aguarde.
    ''')
    time.sleep(1.0)
    fala('''
    Olá, eu sou a Vírtua, sua assistente virtual. Em que posso ajudar? 
    ''')


#Programa principal / Recebe perguntas e retorna respostas

def AssisVirtual():
    ligado = False
    opcoes = ['s','n']
    while True:
        try:
            MicOnn = input('Seu microfone está ligado?[s/n]: ').lower()
            if MicOnn not in opcoes:
                raise ValueError('OPÇÃO INVÁLIDA!!')
            elif not MicOnn:
                raise ValueError('OPÇÃO INVÁLIDA!!')
        except ValueError as erro:
            print(erro)
        else:
            if MicOnn[0] == 'n':
                print('Para usar esta opção você deve ligar um microfone!!!')
                print('Retornando ao menu principal...')
                sleep(3.0)
                return ligado
            elif MicOnn == 's':
                ligado = True
                break


    if ligado == True:
        cumprimento()  # => Inicia o programa com um cumprimento!
        start = True
        comandos = ['iniciar youtube','abrir navegador','que dia é hoje','que horas são','finalizar',
                    'qual o seu nome','pesquisar no google','tocar','contar piada','wiki','consultar ramal','consultar chave']


        piadas = ['Porque o menino estava falando ao telefone deitado?  Para não cair a ligação! kkkkk','Qual é a fórmula da água benta? H Deus Ó! kkkkk',
                  'Qual é a cidade brasileira que não tem táxi?  Uberlândia.', """Um rapaz vai à padaria e pergunta se o salgado era de hoje. O padeiro diz: Não, é de ontem.
                    O rapaz pergunta: E como faço para comer o de hoje?
                    O padeiro diz: Volte amanhã! huasuahsuashuash""","""Qual é o alimento mais sagrado que existe? O amém doím.""",
                  """Por que o policial não usa sabão?
                    Porque ele prefere deter gente!
                    ""","""O que é um pontinho preto no avião? Uma aeromosca. KKKK""","""Como o Batman faz para entrar na Bat-caverna? Ele bate palma!""",
                  """Um menino tinha um cachorro chamado Tido e ele dormia em um cesto. Um dia, o cachorrinho fugiu, qual é o nome do filme? O Cesto sem Tido!""",
                """Você conhece a piada do fotógrafo? Não? É porque ainda não foi revelada!""","""Que raça de cachorro pula mais alto que um prédio?Qualquer uma, porque prédio não pula.""",
                """Como que o Batman dorme? De bruce!""","""Por que na Argentina as vacas vivem olhando para o céu? Porque tem boi nos ares!"""



                  ]


        print('LISTA DE COMANDOS')
        print('='*30)
        for i, comando in enumerate(comandos):
            print(f'{i+1} - {comando}')
        print('=' * 30)
        print()
        while (start):
            fila = falatexto().lower()  # aqui recebe o pedido do usuário e deixa na fila.
            if 'iniciar youtube' in fila:
                fala(""" 
                Entendi, iniciando o youtube para você! Aguarde.
                """)
                webbrowser.open('https://www.youtube.com.br')
                continue
            elif 'abrir navegador' in fila:
                fala("""
                Certo, iniciando o navegador, aguarde!
                """)
                webbrowser.open('https://www.google.com.br')
                continue
            elif 'que dia é hoje' in fila:
                informadia()
                continue

            elif 'que horas são' in fila:
                informahora()
                continue
            elif 'finalizar' in fila:
                fala("""
                Entendi, desligando sistemas. Até breve!
                """)
                break
            elif 'qual o seu nome' in fila:
                fala("""
                Eu me chamo Vírtua. Sou sua assistente virtual e estou aqui para te ajudar!
                """)
                continue
            elif 'pesquisar no google' in fila:
                    fila = fila.replace('pesquisar no google', '')
                    pywhatkit.search(fila)
                    fala("""
                    Isso foi o que eu encontrei até o momento.
                    """)
                    continue
            elif 'tocar' in fila:
                fila = fila.replace('tocar', '')
                fala(f'Tocando {fila}')
                pywhatkit.playonyt(fila)
                continue
            elif 'contar piada' in fila:
                while True:
                    fala("""
                    Ai vai uma boa!
                    """)
                    time.sleep(0.8)
                    sorteada = []
                    piada = random.choice(piadas)
                    if len(sorteada) == 0:
                        sorteada.append(piada)
                    if piada in sorteada:
                        sorteada.pop()
                        piada = random.choice(piadas)
                        fala(piada)
                        sorteada.append(piada)
                    elif piada not in sorteada:
                        fala(piada)
                        sorteada.append(piada)
                    sleep(1)
                    fala('Deseja ouvir outra?')
                    fila = falatexto()
                    if fila == 'não':
                        fala('Entendi, após alguns segundos me dê um novo comando!')
                        break
                    elif fila == 'sim':
                        continue
            elif 'wiki' in fila:
                wikipedia.set_lang("pt")
                fala('Realizando pesquisa')
                fila = fila.replace('wiki', '')
                resultado = wikipedia.summary(fila, sentences=2)
                fala('Encontrei isto na wikipedia')
                fala(resultado)
                sleep(1.5)
                fala('pesquisa realizada com sucesso! Após alguns segundos me dê um novo comando.')
                continue
            elif 'consultar ramal' in fila:

                temp1 = []
                temp2 = []

                temp1.clear()
                temp2.clear()

                with open('NomeRamal.txt','r') as DadosRam:
                    ramais = DadosRam.readlines()
                    for ramal in ramais:
                        temp1.append(ramal.strip().lower())

                with open('NumRamal.txt','r') as RamNums:
                    NumsRamais = RamNums.readlines()
                    for num in NumsRamais:
                        temp2.append(num.strip())
                while True:
                    fala('Informe o ramal a ser pesquisado!')
                    ramal = falatexto().lower()  # aqui recebe o pedido do usuário e deixa na fila.
                    if ramal in temp1:
                        posicao = temp1.index(ramal)
                        fala(f'O ramal {ramal} corresponde ao número {temp2[posicao]}!')
                        continue
                    elif ramal == 'sair':
                        fala('Entendi, estou saindo. Após alguns segundos, me dê um novo comando!')
                        break
                    elif ramal not in ramais:
                        fala('Este ramal ainda não foi cadastrado!')
                        continue
            elif 'consultar chave' in fila:


                temp1 = []
                temp2 = []

                temp1.clear()
                temp2.clear()

                with open('chaves.txt','r') as dadosChaves:
                    chaves = dadosChaves.readlines()
                    for chave in chaves:
                        temp1.append(chave.strip().lower())

                with open('nums.txt','r') as bdNums:
                    numeros = bdNums.readlines()
                    for numero in numeros:
                        temp2.append(numero.strip())
                while True:
                    fala('Informe o nome da chave para saber o número!')
                    chave = falatexto().lower()
                    if chave in temp1:
                        pos = temp1.index(chave)
                        fala(f"A chave {chave} está localizada no número {temp2[pos]}")
                        continue
                    elif chave == 'sair':
                        fala('Entendi, estou saindo. Após alguns segundos, me dê um novo comando!')
                        break
                    elif chave not in temp1:
                        fala('Esta chave ainda não foi cadastrada!')
                        continue
            elif fila not in comandos:
                fala('Desculpe, ainda não aprendi este comando, tente outra coisa!')
                continue