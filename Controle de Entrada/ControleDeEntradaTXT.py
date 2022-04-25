#Importações de libs

import datetime as dt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from time import sleep
import json
from tqdm import tqdm

dataAtual = dt.date.today()
dataAtualN = dataAtual.strftime('%d/%m/%y') #Salva a data atual no formato dia/mês/ano


def CriaMenu(lista,msg):
    """Função para criar um menu utilizando listas"""
    while True:
        print(f'{"<" * 12} {msg} {">" * 12}\n')
        for i,v in enumerate(lista):
            print(f'[{i+1}] - {v}')
        print()
        try:
            escolha = input('Digite uma opção: ')
            if not escolha:
                raise ValueError(f'ERRO, OPÇÃO -> {escolha} <- INVÁLIDA!')
            elif escolha.isnumeric() == False:
                raise ValueError(f'ERRO, OPÇÃO -> {escolha} <- INVÁLIDA!')
        except ValueError as erro:
            print(erro)
            continue
        else:
            return int(escolha)


class BancoDados:
    """Classe responsável por criar um banco de dados através
    da manipulação de arquivos."""


    def CriaBD(self,nomedoArquivo):
        """Método para criar um banco de dados utilizando arquivos
        de extensãoi .json"""
        try:
            with open(f'{nomedoArquivo}.json', 'r'):
                pass
        except FileNotFoundError:
            with open(f'{nomedoArquivo}.json', 'w') as BD:
                lista = []
                json.dump(lista, BD)
                print('BANCO DE DADOS CRIADO COM SUCESO!')
        else:
            print('BANCO DE DADOS CARREGADO COM SUCESSO!')

    def CriaRegistro(self,NomedoArquivo):
        """Método responsável por criar um arquivo de extensão. txt
        para que seja enviado em anexo por e-mail contendo as informações cadastradas"""
        try:
            with open(f'{NomedoArquivo}.txt', 'r'):
                pass
        except FileNotFoundError:
            with open(f'{NomedoArquivo}.txt', 'w'):
                print('Registro Criado com sucesso!')
        else:
            print('Registro carregado com sucesso!')

class bdFuncoes:
    """Classe responsável por realizar as funcionalidades
    de um banco de dados"""

    def __init__(self):
        self.temp1 = []
        self.visitor = []

    def CarregaDados(self,dados):
        """Método para transferir as informações de um arquivo para uma lista,
        retornando esta mesma lista no final"""
        self.temp1.clear()
        self.temp1 = dados.copy()
        return self.temp1
    def CadastraVisitante(self, nome, placa, horaE):
        """Método responsável por criar uma lista contendo informações
        de visitantes e no final, retorna essa mesma lista"""
        self.visitor.clear()
        self.visitor.append(nome)
        self.visitor.append(placa)
        self.visitor.append(horaE)
        return self.visitor


def EnviaEmail():
    """Função para enviar um e-mail com um arquivo em anexo."""
    try:
        fromaddr = "inserir Email" #endereço de e-mail utilizado para enviar a mensagem com anexo.
        toaddr = 'inserirEmail' #endereço de e-mail utilizadado para sinalizar quem receberá a mensagem.
        msg = MIMEMultipart()

        msg['From'] = fromaddr #Preenche o campo de remetente do e-mail com a variável fromaddr.
        msg['To'] = toaddr #Preenche o campo de destinatário com a variável toaddr.
        msg['Subject'] = "Relatório do dia" #Preenche o campo de assunto com o texto inserido aqui.
        if msg['To'] == 'InserirEmail':
            body = f"\nOlá , segue o relatório do dia: {dataAtualN} !" #Cria o corpo de texto da mensagem
        else:
            body = f"\nOlá , segue o relatório do dia: {dataAtualN} !"  # Cria o corpo de texto da mensagem

        msg.attach(MIMEText(body, 'plain')) #Preenche o corpo de texto da mensagem com os dados da variável body

        filename = 'Inserir path do arquivo ou arquivo' #define qual arquivo será anexado

        attachment = open('nomedoArquivo.txt', 'rb') #anexa o arquivo à mensagem

        # a partir da linha 50 até a 57,converte o arquivo para base64, adiciona o nome dele no título do arquivo e
        # junta o arquivo à variável msg com o restante das informações do e-mail.
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('smtp.gmail.com: 587') #cria uma conexão com o servidor do gmail.
        server.starttls() #inicia a conexão com o servidor do gmail.
        server.login(fromaddr, "InserirSenhadoEmail") #realiza o login preenchendo os campos com o e-mail do remetente e a senha.
        text = msg.as_string() #Convertemos as informações armazenadas na variável msg para string.
        server.sendmail(fromaddr, toaddr, text) #envia o email preenchendo com as informações definidas acima
        server.quit()
        print('\nEmail enviado com sucesso!')
    except:
        print("\nErro ao enviar email")

# PROGRAMA PRINCIPAL =================================

BancoDeDados = BancoDados()
BancoFuncoes = bdFuncoes()

BancoDeDados.CriaBD('bd')
BancoDeDados.CriaRegistro('registro')

while True:
    user = CriaMenu(['Registro de Visitantes','Registro de Motoristas','Registro de Caminhões de Entrega','SAIR'],'MENU INICIAL')
    if user == 1:
        #CÓDIGO PARA A PARTE DE CADASTRO DE VISITANTES =====================
        while True:
            user_1 = CriaMenu(['Registrar entrada','Registrar saida','Consultar Registro','Editar Nome','Limpar Registro','Enviar dados para e-mail','VOLTAR AO MENU INICIAL'],'MENU VISITANTES')
            # CÓDIGO PARA REGISTRO DE: NOME, PLACA, HORA DE ENTRADA ================
            if user_1 == 1:
                while True:
                    with open('bd.json','r') as BD:
                        Bdados = json.load(BD)
                        dados = BancoFuncoes.CarregaDados(Bdados)

                    nome = input('Digite o nome: ')
                    if nome == 'sair':
                        break
                    placa = input('Digite a placa: ')
                    horae = input('Digite o horário de entrada: ')
                    print(f'Entrada de {nome} cadastrada com sucesso!')
                    visitante = BancoFuncoes.CadastraVisitante(nome, placa,horae)
                    dados.append(visitante.copy())
                    with open('bd.json','w') as bDados:
                        json.dump(dados,bDados)

            elif user_1 == 2:
                #CÓDIGO PARA REGISTRO DE: HORA DE SAÍDA =====================
                while True:
                    with open('bd.json','r') as BD:
                        Bdados = json.load(BD)
                    dados = BancoFuncoes.CarregaDados(Bdados)

                    VisitanteSaida = input('Digite o nome para cadastrar a saída: ')
                    if VisitanteSaida == 'sair':
                        break
                    for listas in dados:
                        if VisitanteSaida in listas:
                            horas = input('Digite a hora de saída: ')
                            if len(listas) == 3:
                                listas.append(horas)
                            else:
                                listas[3] = horas

                    with open('bd.json','w') as BD:
                        json.dump(dados,BD)
                    print(f'HORA DE SAÍDA PARA {VisitanteSaida} REGISTRADA COM SUCESSO!')
            elif user_1 == 3:
                #CÓDIGO PARA VISUALIZAR DADOS CADASTRADOS =================================
                print('Lista de Entradas Registradas:\n')
                with open('bd.json','r') as BD:
                    dados = json.load(BD)
                for visitante in dados:
                    if len(visitante) == 3:
                        print(f'Nome: {visitante[0]:<10} / Placa do Veículo: {visitante[1]:^10} / Hora Entrada: {visitante[2]:>10}')
                    elif len(visitante) == 4:
                        print(f'Nome: {visitante[0]:<10} / Placa do Veículo: {visitante[1]:^10} / Hora Entrada: {visitante[2]:>5} / Hora Saída: {visitante[3]:>5}')
            elif user_1 == 4:
                #CÓDIGO PARA EDITAR NOME
                print('>>>>>> EDITAR NOME <<<<<<<')
                with open('bd.json', 'r') as BD:
                    cadastro = json.load(BD)
                    dados = BancoFuncoes.CarregaDados(cadastro)
                    print(dados)
                while True:
                    try:
                        Nome = input('Digite o nome a ser alterado: ')
                        if Nome == 'sair':
                            break
                        elif not Nome:
                            raise ValueError('ERRO! Você deixou a opção em branco!')
                        for lista in dados:
                            if Nome not in lista:
                                raise ValueError('ERRO! Nome não encontrado!')
                    except ValueError as Erro:
                        print(Erro)
                        continue
                    else:
                        for lista in dados:
                            if Nome in lista:
                                nomepos = lista.index(Nome)
                                while True:
                                    try:
                                        novoNome = input('Edite o nome conforme deseja: ').strip()
                                        if not novoNome or len(novoNome) == 0:
                                            raise ValueError('ERRO! Você deixou a opção em branco!')
                                        elif novoNome == Nome:
                                            raise ValueError('ERRO!, Você digitou o mesmo nome sem fazer alterações!')
                                    except ValueError as Erro:
                                        print(Erro)
                                        continue
                                    else:
                                        lista[nomepos] = novoNome
                                        print('ALTERAÇÃO EFETUADA COM SUCESSO!')
                                        with open('bd.json','w') as bd:
                                            json.dump(dados,bd)
                                        sleep(2.0)
                                    break

            elif user_1 == 5:
                print('\nATENÇÃO, VOCÊ ESTÁ PRESTES A LIMPAR TODOS OS DADOS CADASTRADOS!!!\n')
                cont = input('DESEJA REALMENTE APAGAR??\n\n'
                             'CASO PROSSIGA NÃO SERÁ POSSÍVEL DESFAZER O PROCEDIMENTO[s/n]: ')
                if cont == 's':
                    print('ESVAZIANDO BANCO DE DADOS...')
                    with open('bd.json','r') as bd:
                        dados = json.load(bd)
                        for dado in tqdm(dados):
                            sleep(1.5)

                    with open('bd.json','w') as bd:
                        lista = []
                        json.dump(lista,bd)

                    print('BANCO DE DADOS ESVAZIADO COM SUCESSO!')
                    sleep(1.5)
                else:
                    print('VOLTANDO AO MENU DE VISITANTES...')
                    sleep(1.6)
            elif user_1 == 6:
                #CÓDIGO PARA ENVIO DE E-MAIL COM OS DADOS ======================
                with open('bd.json','r') as BD:
                    dados = json.load(BD)


                if len(dados) == 0:
                    print('ERRO! O ARQUIVO NÃO POSSUI NENHUM CADASTRO!!')
                    print('RETORNANDO AO MENU DE VISITANTES!!!')
                    sleep(2.0)
                else:
                    with open('NomedoArquivo.txt','w') as Registro:
                        for listas in dados:
                            Registro.write(f'Nome: {listas[0]} / Placa: {listas[1]} / Hora de Entrada: {listas[2]} / Hora de Saída: {listas[3]}')
                            Registro.write('\n\n')
                    print('ENVIANDO E-MAIL...')
                    for dados in tqdm(dados):
                        sleep(0.6)

                    EnviaEmail()

                    with open('bd.json','w') as BD:
                        lista = []
                        json.dump(lista,BD)

                    with open('NomedoArquivo','w'):
                        pass
                    sleep(1.6)

            elif user_1 == 7:
                print('Voltando ao menu inicial...')
                sleep(1.8)
                break


    elif user == 4:
        print('OBRIGADO POR USAR O AUTO SENDER!! SAINDO...')
        sleep(1.8)
        break





