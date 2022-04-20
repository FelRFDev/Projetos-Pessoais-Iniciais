import json
import datetime as dt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
from time import sleep

dataAtual = dt.date.today()
dataAtualN = dataAtual.strftime('%d/%m/%y') #Salva a data atual no formato dia/mês/ano


def criaMenu(msg,lista:list):
    print(f'>>>>>>>  {msg} <<<<<<<<\n')
    for i,v in enumerate(lista):
        print(f'[{i+1}] - {v}')
    print()
    while True:
        try:
            escolha = int(input('Sua escolha: '))
        except ValueError:
            print('OPÇÃO INVÁLIDA!')
            continue
        else:
            return escolha

def CriaBD():
    try:
        with open('usuarios.json','r'):
            pass
    except FileNotFoundError:
        users = []
        with open('usuarios.json','w') as bd:
            json.dump(users,bd)
        print('BANCO DE DADOS CRIADO COM SUCESSO!')
    else:
        print('BANCO DE DADOS CARREGADO COM SUCESSO!')




def EnviaEmail(destinatario,lista:list):
    """Função para enviar um e-mail com um arquivo em anexo."""
    try:
        fromaddr = "autosender31@gmail.com" #endereço de e-mail utilizado para enviar a mensagem com anexo.
        toaddr = f'{destinatario}' #endereço de e-mail utilizadado para sinalizar quem receberá a mensagem.
        msg = MIMEMultipart()

        msg['From'] = fromaddr #Preenche o campo de remetente do e-mail com a variável fromaddr.
        msg['To'] = toaddr #Preenche o campo de destinatário com a variável toaddr.
        msg['Subject'] = "RESGATE DE LOGIN" #Preenche o campo de assunto com o texto inserido aqui.
        for dados in lista:
            body = f"\nOlá {destinatario}, segue abaixo os seus dados para acesso. Data de Envio:{dataAtualN}!\n\n" \
                   f"Usuário: {dados[1]} / senha: {dados[2]}" #Cria o corpo de texto da mensagem
            msg.attach(MIMEText(body, 'plain')) #Preenche o corpo de texto da mensagem com os dados da variável body

        server = smtplib.SMTP('smtp.gmail.com: 587') #cria uma conexão com o servidor do gmail.
        server.starttls() #inicia a conexão com o servidor do gmail.
        server.login(fromaddr, "envioauto") #realiza o login preenchendo os campos com o e-mail do remetente e a senha.
        text = msg.as_string() #Convertemos as informações armazenadas na variável msg para string.
        server.sendmail(fromaddr, toaddr, text) #envia o email preenchendo com as informações definidas acima
        server.quit()
        print('\nEmail enviado com sucesso!')
    except:
        print("\nErro ao enviar email")





CriaBD()



users = []
user = []
while True:
    visitante = criaMenu('ÁREA DE ACESSO',['Cadastrar','Fazer login','Recuperar Acesso'])
    if visitante == 1:
        print('PAINEL DE CADASTRO\n')
        users.clear()
        user.clear()
        with open('usuarios.json', 'r') as bd:
            dados = json.load(bd)
            users = dados.copy()
            print(users)

        nome = input('Informe o seu nome completo: ')
        email = input('Informe o seu e-mail (Servirá como usuário): ')
        senha = input('Informe uma senha: ')
        user.append(nome)
        user.append(email)
        user.append(senha)
        users.append(user)
        with open('usuarios.json','w') as bd:
            json.dump(users,bd)
        print('CADASTRO EFETUADO COM SUCESSO!')
        sleep(1.8)


    elif visitante == 2:
        while True:
            users.clear()
            with open('usuarios.json','r') as bd:
                dados = json.load(bd)
                users = dados.copy()
                print(users)

            nome = input('Digite o seu nome: ')
            if len(users) == 0:
                print('ERRO, VOCÊ NÃO ESTÁ CADASTRADO! ACESSE O MENU [CADASTRAR] PARA PROSSEGUIR!')
                break
            else:
                for usuarios in users:
                    if nome in usuarios:
                        print('>>>> PAINEL DE LOGIN <<<<<')
                        tentativas = 0
                        while True:
                            sair = False
                            if sair == True:
                                break
                            try:
                                if sair == True:
                                    break
                                usuario = input('Digite o usuário (Seu e-mail): ')
                                if usuario not in usuarios:
                                    raise ValueError('USUÁRIO INCORRETO! TENTE NOVAMENTE!')
                                elif not usuario:
                                    raise ValueError('USUÁRIO INCORRETO! TENTE NOVAMENTE!')
                            except ValueError as erro:
                                print(erro)
                                tentativas += 1
                                if tentativas > 4:
                                    print('Número de tentativas esgotado! Acesse [Recuperar Acesso] para resgatar o usuário!')
                                    break
                                else:
                                    print(f'Numero de Tentativas: {tentativas}')
                                    continue
                            else:
                                senhaTentativas = 0
                                while True:
                                    if sair == True:
                                        break
                                    try:
                                        password = input('Digite a senha: ')
                                        if not password:
                                            raise ValueError('SENHA INCORRETA, TENTE NOVAMENTE!')
                                        elif password not in usuarios:
                                            raise ValueError('SENHA INCORRETA, TENTE NOVAMENTE!')
                                    except ValueError as erro:
                                        print(erro)
                                        senhaTentativas += 1
                                        if senhaTentativas > 4:
                                            print('Número de tentativas esgotado! Acesse [Recuperar Acesso] para resgatar o usuário!')
                                            sair = True
                                            break
                                        else:
                                            print(f'Número de tentativas: {senhaTentativas}')
                                            continue
                                    else:
                                        print('LOGIN EFETUADO COM SUCESSO!')
                                        sair = True
                            if sair == True:
                                break
                    else:
                        print('ERRO, VOCÊ NÃO ESTÁ CADASTRADO! ACESSE O MENU [CADASTRAR] PARA PROSSEGUIR!')
                break
    elif visitante == 3:

        users.clear()

        with open('usuarios.json','r') as dados:
            usu = json.load(dados)
            users = usu.copy()

        nome = input('Informe o seu nome: ')
        for usuarios in users:
            if nome in usuarios:
                EnviaEmail(usuarios[1],users)
                print('USUÁRIO RESGATADO COM SUCESSO!')
                print('CONFIRA O SEU E-MAIL CADASTRADO!')
                with open('DadosCadastrais.txt', 'w') as Cadastro:
                    Cadastro.write("")
                sleep(1.8)