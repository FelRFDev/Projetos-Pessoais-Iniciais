
#===================== Importações ======================
from tqdm import tqdm
from time import sleep
import json
from prettytable import PrettyTable, DOUBLE_BORDER
import matplotlib.pyplot
import random
import datetime as dt
#-=-=-=-=-= IMPORTAÇÕES PARA ENVIO DE E-MAIL AUTOMÁTICO -=-=-=-=-=-=-=-=
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#=============== < lista de funções > ==========================
def bdAnalise():
    try:
        with open('dadosMensais.json','r'):
            pass
    except FileNotFoundError:
        with open('dadosMensais.json','w') as dm:
            listaMeses = {
            'Janeiro': [0,0],
            'Fevereiro': [0,0],
            'Março': [0,0],
            'Abril': [0,0],
            'Maio': [0,0],
            'Junho': [0,0],
            'Julho': [0,0],
            'Agosto': [0,0],
            'Setembro': [0,0],
            'Outubro': [0,0],
            'Novembro': [0,0],
            'Dezembro': [0,0],
            'TotalClientes': 0,
            'LucroMensal':0,
        }
            json.dump(listaMeses,dm)
            print('Banco de dados para DADOS MENSAIS criado com sucesso!')
    else:
        print("Banco de dados para DADOS MENSAIS carregado com sucesso!")


def criaBDclientes():
    try:
        with open('clientes.json','r'):
            pass
    except FileNotFoundError:
        with open('clientes.json','w') as bd:
            empty_data = {}
            json.dump(empty_data,bd)
        print('Banco de dados Criado com Sucesso!!')
    else:
        print('Banco de dados carregado com sucesso!')

def cadastra_cliente(clientes_dados,nome_do_cliente,dados_do_cliente):
    clientes_dados.update({nome_do_cliente:dados_do_cliente})

#Função parar criar menu
def criamenu(lista, msg):
    print(f'          << {msg} >>\n')
    menu = PrettyTable()
    menu.add_column(f'CÓDIGO',[lista.index(x)+1 for x in lista])
    menu.add_column(f'OPÇÕES',lista)
    menu.set_style(DOUBLE_BORDER)
    print(menu)
    opc = int(input('Escolha uma opção: '))
    return opc


#função para exibir mensagem de erro
def mensagemerro():
    print('=============================================================================')
    print(
        f'{cores["vermelho"]}ERRO, OPÇÃO INVÁLIDA! VOCÊ DEIXOU A OPÇÃO EM BRANCO OU NÃO DIGITOU UM NÚMERO!{cores["fechacor"]}')
    print('=============================================================================')
    print('REINICIANDO...')
    print()
    sleep(1.5)


def erroopcao(opc):
    print('=============================================================================')
    print(f'{cores["vermelho"]}ERRO, OPÇÃO ["{opc}"] INVÁLIDA!{cores["fechacor"]}')
    print('=============================================================================')
    print('REINICIANDO...')
    print()
    sleep(1.5)


def EnviaEmail(nomeDoArquivo,destinatario):
    """Função para enviar um e-mail com um arquivo em anexo."""
    try:
        dataAtual = dt.date.today()
        dataAtualN = dataAtual.strftime('%d/%m/%y')  # Salva a data atual no formato dia/mês/ano
        fromaddr = "seu e-mail@gmail.com" #endereço de e-mail utilizado para enviar a mensagem com anexo.
        toaddr = destinatario #endereço de e-mail utilizadado para sinalizar quem receberá a mensagem.
        msg = MIMEMultipart()

        msg['From'] = fromaddr #Preenche o campo de remetente do e-mail com a variável fromaddr.
        msg['To'] = toaddr #Preenche o campo de destinatário com a variável toaddr.
        msg['Subject'] = "Relatório Por Períodos" #Preenche o campo de assunto com o texto inserido aqui.
        body = f"\nOlá, segue em anexo o arquivo do relatório em imagem.\n\nEnviado no dia: {dataAtualN}!" #Cria o corpo de texto da mensagem

        msg.attach(MIMEText(body, 'plain')) #Preenche o corpo de texto da mensagem com os dados da variável body

        filename = nomeDoArquivo #define qual arquivo será anexado
        attachment = open(nomeDoArquivo, 'rb') #anexa o arquivo à mensagem

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
        server.login(fromaddr, "senha do email que irá enviar a mensagem") #realiza o login preenchendo os campos com o e-mail do remetente e a senha.
        text = msg.as_string() #Convertemos as informações armazenadas na variável msg para string.
        server.sendmail(fromaddr, toaddr, text) #envia o email preenchendo com as informações definidas acima
        server.quit()
        print(f'Email enviado com sucesso!')
    except:
        print(f'Erro ao enviar email')


def geraGrafico(meses,valores,dadosmensais):
    """Função para gerar um gráfico através dos dados recebidos. Tem como parâmetros:
    -> mes: Parâmetro responsável por receber o argumento contendo o nome do mês. Geralmente uma lista.
    -> valor: Parâmetro responsável por receber o arqumento contendo o valor total mensal. Geralmente uma lista.
    -> DadosMensais: Parâmetro responsável por conter os dados relacionados a cada mês.(Dict)
    """
    colors = ['red','green','yellow','purple','blue']
    totalIndices = len(valores)
    for mes,valor in zip(meses,valores):
        matplotlib.pyplot.bar(mes,int(valor),color=random.choice(colors))#recebe as estruturas contendo o nome dos meses e respectivos valores
    matplotlib.pyplot.xticks(rotation=45)
    matplotlib.pyplot.title('Quantidade Total de Clientes por mês\n') #título do grafico
    matplotlib.pyplot.xlabel(f'Meses\n\n\n\n\n\n') #título do eixo x
    matplotlib.pyplot.ylabel('Clientes por mês') #título do eixo Y
    matplotlib.pyplot.ylim(0,max(valores)+10) #Estrutura para atenuar a curva do gráfico
    maiorValor = max(valores) #encontra o maior valor
    posMaiorValor = valores.index(maiorValor) #encontra a posição na lista do maior valor
    matplotlib.pyplot.annotate("Maior valor",
                xy=(posMaiorValor,maiorValor),#indicando as coordenadas do maior valor
                xytext=(posMaiorValor, maiorValor + 4),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
    matplotlib.pyplot.text(totalIndices, 6, f'       LUCRO MENSAL\n ')
    y = 5
    for mes,luc in dadosmensais.items():
        y -=3
        matplotlib.pyplot.text(totalIndices,y,f'  Mês: {mes} - R${luc:.2f}')
        matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.grid(axis='y')

    user_Save = input('Deseja salvar o gráfico em arquivo de imagem e PDF? [s/n]: ')
    if user_Save == 'n':
        pass
    else:
        fileName = input('Digite o nome desejado para o arquivo: ')
        print('SALVANDO RELATÓRIO, AGUARDE...')
        sleep(1.3)
        matplotlib.pyplot.savefig(fileName + '.png')
        matplotlib.pyplot.savefig(fileName + '.pdf')
        input('RELATÓRIO SALVO COM SUCESSO NA PASTA DO PROGRAMA!!!')
        enviaEmail = input('Deseja enviar este relatório via anexo por e-mail? [s/n]: ')
        if enviaEmail == 'n':
            pass
        else:
            eAdress = input("Digite o endereço de e-mail do destinatário: ")
            EnviaEmail(fileName+'.png',eAdress)
    matplotlib.pyplot.show()


#===========================================================

def geraGraficoAdmin(meses,valores):
    """Função para gerar um gráfico através dos dados recebidos. Tem como parâmetros:
    -> mes: Parâmetro responsável por receber o argumento contendo o nome do mês. Geralmente uma lista.
    -> valor: Parâmetro responsável por receber o arqumento contendo o valor total mensal. Geralmente uma lista.
    -> DadosMensais: Parâmetro responsável por conter os dados relacionados a cada mês.(Dict)
    """
    lucroMensal = {'Janeiro':15000.00,'Maio':12000.00,'Abril':15000.00,'Dezembro':15000.00,'Fevereiro':15000.00,
                   'Março':15000.00,'Junho':15000.00,'Julho':15000.00,'Agosto':15000.00,}
    colors = ['red','green','yellow','purple','blue']
    totalIndices = len(valores)
    for mes,valor in zip(meses,valores):
        matplotlib.pyplot.bar(mes,int(valor),color=random.choice(colors))#recebe as estruturas contendo o nome dos meses e respectivos valores
    matplotlib.pyplot.xticks(rotation=45)
    matplotlib.pyplot.title('Quantidade Total de Clientes por mês\n') #título do grafico
    matplotlib.pyplot.xlabel(f'Meses\n\n\n\n\n\n') #título do eixo x
    matplotlib.pyplot.ylabel('Clientes por mês') #título do eixo Y
    matplotlib.pyplot.ylim(0,max(valores)+10) #Estrutura para atenuar a curva do gráfico
    maiorValor = max(valores) #encontra o maior valor
    posMaiorValor = valores.index(maiorValor) #encontra a posição na lista do maior valor
    matplotlib.pyplot.annotate("Maior valor",
                xy=(posMaiorValor,maiorValor),#indicando as coordenadas do maior valor
                xytext=(posMaiorValor, maiorValor + 4),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
    matplotlib.pyplot.text(totalIndices, 6, f'       LUCRO MENSAL\n ')
    y = 5
    for mes,lucro in lucroMensal.items():
        y -=3
        matplotlib.pyplot.text(totalIndices,y,f'  Mês: {mes} - R${lucro:.2f}') ####################### >PAREI AQUI
        matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.grid(axis='y')

    user_Save = input('Deseja salvar o gráfico em arquivo de imagem e PDF? [s/n]: ')
    if user_Save == 'n':
        pass
    else:
        fileName = input('Digite o nome desejado para o arquivo: ')
        print('SALVANDO RELATÓRIO, AGUARDE...')
        sleep(1.3)
        matplotlib.pyplot.savefig(fileName + '.png')
        matplotlib.pyplot.savefig(fileName + '.pdf')
        input('RELATÓRIO SALVO COM SUCESSO NA PASTA DO PROGRAMA!!!')
        enviaEmail = input('Deseja enviar este relatório via anexo por e-mail? [s/n]: ')
        if enviaEmail == 'n':
            pass
        else:
            eAdress = input("Digite o endereço de e-mail do destinatário: ")
            EnviaEmail(fileName+'.png',eAdress)
    matplotlib.pyplot.show()

#===========================================================
#paleta de cores


car_logo = """
               ______
             /|_||_\`.__
            (   _    _ _/
            =`-(_)--(_)-'
"""


customers = {}
customers_info = []

cores = {
        'vermelho': '\033[1;31m',
        'verde': '\033[1;32m',
        'azul': '\033[1;34m',
        'fechacor': '\033[m',
}


#programa principal

criaBDclientes() #criando banco de dados para cadastro dos clientes
bdAnalise() #criando banco de dados para as informações mensais

precos = {
    30:10,
    60:20,
}

totalmin= 0
totpagar=0


def programaprincipal():
    monthList = {
            'Janeiro': [0,0],
            'Fevereiro': [0,0],
            'Março': [0,0],
            'Abril': [0,0],
            'Maio': [0,0],
            'Junho': [0,0],
            'Julho': [0,0],
            'Agosto': [0,0],
            'Setembro': [0,0],
            'Outubro': [0,0],
            'Novembro': [0,0],
            'Dezembro': [0,0],
            'TotalClientes': 0,
            'LucroMensal':0,
        }
    periodos = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                'Novembro', 'Dezembro']
    #estacionamento composto por um dicionário e listas
    estacionamento = {
            'vaga 1': [],
            'vaga 2': [],
            'vaga 3': [],
            'vaga 4': [],
            'vaga 5': [],
            'vaga 6': [],
            'vaga 7': [],
            'vaga 8': [],
            'vaga 9': [],
            'vaga 10': [],
    }
    #inicio do programa principal
    print(f'{cores["azul"]}Controle de vagas 1.0 >>[ESTACIONAMENTO "ISTOP"]<<{cores["fechacor"]} {car_logo}')
    print(f'{cores["azul"]}Feito por: Felipe Rodrigues Fonseca / contato: comunidadehawks@gmail.com / (55) 99724-6397{cores["fechacor"]}')
    while True:
        try:
            print()
            menu = criamenu(['Cadastrar horário','Liberar vaga','Liberar todas as vagas','Disponibilidade das Vagas','Finalizar Diária','Gerar Relatório','Sair','Gerar Relatório (VERSÃO ADMIN)'], 'MENU INICIAL')
        except(TypeError,ValueError):
            mensagemerro()
            continue
        if menu > 8 or menu < 1:
            erroopcao(menu)
            continue
        elif menu == 1:
            while True:
                #carrega o banco de dados em modo de leitura para clientes e para dados mensais
                with open('clientes.json','r') as bdDados:
                    bd = json.load(bdDados)
                    customers = bd

                #dicionário com listas no qual o índice 0 é o total de clientes e o índice 1 o lucro mensal
                with open('dadosMensais.json','r') as menDados:
                    mdados = json.load(menDados)
                    monthList = mdados

                #Adiciona horario das vagas:
                horae = input('Digite a hora de entrada no formato (Hora:Minuto): ')
                if len(horae) < 4 or len(horae) > 5:
                    print()
                    print(f'{cores["vermelho"]}ERRO, digite a hora no formato correto!{cores["fechacor"]}')
                    print()
                    continue
                horas = input('Digite a hora de saída no formato (Hora:Minuto): ')
                while len(horas) < 4 or len(horas) > 5:
                    print()
                    print(f'{cores["vermelho"]}ERRO, digite a hora no forma correto!{cores["fechacor"]}')
                    print()
                    horas = input('Digite a hora de saída no formato (Hora:Minuto): ')

                motorista = input('Digite o nome do motorista: ').strip()
                while not motorista:
                    print(f'{cores["vermelho"]}ERRO, você precisa digitar algo{cores["fechacor"]}')
                    motorista = input('Digite o nome do motorista: ').strip()
                if motorista not in customers:
                    customers_info.clear()
                    placa = input('Digite a placa do veículo: ').strip()
                    while not placa:
                        print(f'{cores["vermelho"]}ERRO, você precisa digitar algo{cores["fechacor"]}')
                        placa = input('Digite a placa do veículo: ').strip()
                    carro = input('Digite o modelo do veículo: ').strip()
                    while not carro:
                        print(f'{cores["vermelho"]}ERRO, você precisa digitar algo{cores["fechacor"]}')
                        carro = input('Digite o modelo do veículo: ').strip()
                    cpf = input('Digite o cpf do cliente: ').strip()
                    while not cpf:
                        print(f'{cores["vermelho"]}ERRO, você precisa digitar algo{cores["fechacor"]}')
                        cpf = input('Digite o cpf do cliente: ').strip()
                    customers_info.append(placa)
                    customers_info.append(carro)
                    customers_info.append(cpf)
                    cadastra_cliente(customers,motorista,customers_info)

                    #salva no banco de dados a lista de clientes
                    with open('clientes.json','w') as bdDados:
                        json.dump(customers,bdDados)

                vaga = input('Digite a vaga a ser ocupada: ')
                while vaga not in estacionamento.keys() or len(estacionamento[vaga]) > 0:
                    if vaga not in estacionamento.keys():
                        print()
                        print(f'{cores["vermelho"]}ERRO, vaga não encontrada!{cores["fechacor"]}')
                        print()
                        vaga = input('Digite a vaga a ser ocupada: ')
                    else:
                        print()
                        print(f'{cores["vermelho"]}ERRO, a vaga já está ocupada!{cores["fechacor"]}')
                        print()
                        vaga = input('Digite a vaga a ser ocupada: ')

                #Parte do código responsável pelos cálculos
                estacionamento[vaga].append(motorista)
                for dados in customers[motorista]:
                    estacionamento[vaga].append(dados)
                estacionamento[vaga].append(horae)
                estacionamento[vaga].append(horas)

                #Calculando total a pagar
                totalH = int(horas[:2]) - int(horae[:2])

                global totpagar
                global totalmin
                if int(horas[3:]) > int(horae[3:]):
                    totalmin = int(horas[3:]) - int(horae[3:])
                elif int(horas[3:]) < int(horae[3:]):
                    totalmin = int(horae[3:]) - int(horas[3:])
                if totalmin != 0 and totalmin != 30:
                    totalmin = 30
                if totalmin == 0:
                    totpagar = precos[60] * totalH
                else:
                    totpagar = (precos[60] * totalH) + precos[30]
                totpagar = float(totpagar)
                monthList["TotalClientes"] +=1
                monthList["LucroMensal"] += totpagar
                print(f'TOTAL A PAGAR: R$ {totpagar:.2f}')  # total a pagar
                # ========== salva a quantidade de clientes do dia ===========
                with open('dadosMensais.json','w') as mDados:
                    json.dump(monthList,mDados)
                totpagar = str(totpagar).replace(".0", ",00")
                print(f'Lucro mensal -> {monthList["LucroMensal"]}')
                con = input('Deseja cadastrar outro horário? [s/n]: ')
                if con in 'Nn':
                    break
# =================================== PAREI AQUI (adicionar hora de entrada e saída na vaga) ===========================
        elif menu == 2:
            while True:
            #limpa a lista e libera a vaga
                vaga = input('Digite a vaga a ser liberada ou "s" para voltar ao menu: ')
                if not vaga:
                    print(f'{cores["vermelho"]}ERRO, você deixou a opção em branco!{cores["fechacor"]}')
                    continue
                if vaga in 'sS':
                    break
                elif vaga not in estacionamento.keys():
                    print(f'{cores["vermelho"]}VAGA NÃO ENCONTRADA!{cores["fechacor"]}')
                elif len(estacionamento[vaga]) == 0:
                    print(f'{cores["vermelho"]}ERRO, esta vaga já está livre{cores["fechacor"]}')
                else:
                    estacionamento[vaga].clear()
                    print(f'{vaga} {cores["verde"]}liberada com sucesso!{cores["fechacor"]}')
                    con = input('Deseja continuar? [s/n]: ')
                    if con in 'nN':
                        break

        elif menu == 3:
            #libera todas as vagas
            empty = True
            for k,v in estacionamento.items():
                if len(v) == 0:
                    pass
                else:
                    empty = False

            if empty == True:
                print(f'{cores["verde"]}AS VAGAS JÁ ESTÃO VAZIAS!{cores["fechacor"]}')
                input('Aperte qualquer tecla para continuar:')
                sleep(1.0)
            else:
                print('Liberando todas as vagas, aguarde...')
                sleep(1.5)
                for vagas in tqdm(estacionamento.values()):
                    sleep(0.5)
                    vagas.clear()
                print(f'{cores["verde"]}Vagas liberadas com SUCESSO!{cores["fechacor"]}')
                input('Aperte qualquer tecla para continuar:')
                sleep(1.0)

        elif menu == 4:
            #imprime a disponibilidade das vagas e seus horários
            print()
            print('<<<DISPONIBILIDADE DAS VAGAS>>>\n')
            for key, values in estacionamento.items():
                print()
                print(f'Disponibilidade da {key}:')
                if len(values) > 0:
                    print(f'{cores["vermelho"]}Motorista: {values[0]} / Placa do Veículo: {values[1]}'
                          f'/ Modelo do Veículo: {values[2]} / CPF do motorista: {values[3]}\n-> Hora de Entrada: {values[4]} / Hora de Saída: {values[5]} <-{cores["fechacor"]}')
                else:
                    print(f'{cores["verde"]}VAGA LIVRE!{cores["fechacor"]}')

            input('Pressione qualquer tecla para continuar:')

        elif menu == 5:
            #FINALIZA A DIÁRIA
            print('Informe o período atual conforme a lista abaixo:')
            periodosOPC = PrettyTable()
            periodosOPC.add_column('MESES',periodos)
            periodosOPC.set_style(DOUBLE_BORDER)
            periodosOPC.align='c'
            print(periodosOPC)
            with open('dadosMensais.json','r') as dMen:
                Dmen = json.load(dMen)
                monthList = Dmen
            while True:
                try:
                    periodo_user = input('Informe o periodo: ')
                    if not periodo_user:
                        raise ValueError('ERRO, VOCÊ PRECISA DIGITAR ALGO!')
                    elif periodo_user not in monthList.keys():
                        raise ValueError('ERRO, PERÍODO NÃO ENCONTRADO!')
                    elif monthList[periodo_user][0] > 0:
                        raise ValueError('ERRO, ESTE PERÍODO JÁ CONTÉM DADOS CADASTRADOS!')
                except ValueError as Erro:
                    print(Erro)
                else:
                    monthList[periodo_user][0] = monthList["TotalClientes"]
                    monthList[periodo_user][1] = monthList["LucroMensal"]
                    monthList["TotalClientes"] = 0
                    monthList["LucroMensal"] = 0

                with open('dadosMensais.json','w')as dMen:
                    json.dump(monthList,dMen)
                    print('DIÁRIA FINALIZADA COM SUCESSO!')
                input('\nAPERTE UMA TECLA PARA CONTINUAR...')
                break

        elif menu == 6:
            with open('dadosMensais.json','r') as dMen:
                DadosMeses = json.load(dMen)
            print('\n\nGerando relatório!')
            periodoMenu = PrettyTable()
            periodoMenu.add_column(f'CÓDIGO DO MÊS', [periodos.index(x) + 1 for x in periodos])
            periodoMenu.add_column(f'MÊSES', periodos)
            periodoMenu.set_style(DOUBLE_BORDER)
            print(periodoMenu)
            inicio = int(input('Digite o código do mês que corresponde ao inicio do período: '))
            fim = int(input('Digite o código do mês que corresponde ao final do período: '))

            #Estrutura para obter os valores referentes ao período escolhido pelo usuário
            mesesAnalise = []
            for c in range(inicio-1, fim):
                # percorre a lista criada somente com os meses adicionando cada mês correspondente ao índice
                mesesAnalise.append(periodos[c])
            valores = []
            for mes in mesesAnalise:
                valores.append(DadosMeses[mes][0])
            lucro_mensal = []
            for meses in mesesAnalise:
                lucro_mensal.append(DadosMeses[meses][1])
            dados_lucro = {}
            for mes,lucros in zip(mesesAnalise,lucro_mensal):
                dados_lucro.update({mes:lucros})
            geraGrafico(mesesAnalise,valores,dados_lucro)

        elif menu == 7:
            print(f'{cores["azul"]}OBRIGADO POR USAR O GERÊNCIADOR DE VAGAS, SAINDO...{cores["fechacor"]}')
            sleep(1.4)
            break

        elif menu == 8:
            with open('dadosMensais.json', 'r') as dMen:
                DadosMeses = json.load(dMen)
                for mes in DadosMeses.keys():
                    DadosMeses[mes] = random.randint(10,30)

            print('Gerando relatório (=======> VERSÃO ADMIN.! <======)')
            print("Esta versão gera 'DADOS FAKE' de forma aleatória somente para a demonstração da funcionalidade.")
            inicio = int(input('Digite o mês que corresponde ao inicio do período: '))
            fim = int(input('Digite o mês que corresponde ao final do período: '))

            # Estrutura para obter os valores referentes ao período escolhido pelo usuário
            mesesAnalise = []
            for c in range(inicio - 1, fim):
                # percorre a lista criada somente com os meses adicionando cada meês correspondente ao índice
                mesesAnalise.append(periodos[c])
            print(mesesAnalise)

            valores = []
            for mes in mesesAnalise:
                valores.append(DadosMeses[mes])
            print(valores)
            geraGraficoAdmin(periodos,valores)


programaprincipal()
