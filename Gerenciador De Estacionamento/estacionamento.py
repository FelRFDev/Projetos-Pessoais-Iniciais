from tqdm import tqdm
from time import sleep




#=============== < lista de funções > ==========================


#Função parar criar menu

def criamenu(lista, msg):
    print(f'<< {msg} >>\n')
    for i, v in enumerate(lista):
        print(f'[{i+1}] - {v}')
    print()
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


#===========================================================

#paleta de cores


cores = {
        'vermelho': '\033[1;31m',
        'verde': '\033[1;32m',
        'azul' : '\033[1;34m',
        'fechacor': '\033[m',
}


#programa principal

def programaprincipal():
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
    print(f'{cores["azul"]}I-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^=I{cores["fechacor"]}')
    print(f'{cores["azul"]}I               Controle de vagas 1.0 >>[ESTACIONAMENTO "NOME DO SEU ESTABELECIMENTO"]<<                   I{cores["fechacor"]}')
    print(f'{cores["azul"]}I     Feito por: Felipe Rodrigues Fonseca / contato: comunidadehawks@gmail.com / (55) 99724-6397           I{cores["fechacor"]}')
    print(f'{cores["azul"]}I-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^-=^=I{cores["fechacor"]}')
    while True:
        try:
            print()
            menu = criamenu(['Cadastrar horário', 'Liberar vaga', 'Liberar todas as vagas', 'Disponibilidade das Vagas', 'Sair'], 'MENU INICIAL')
        except(TypeError,ValueError):
            mensagemerro()
            continue
        if menu > 5 or menu < 1:
            erroopcao(menu)
            continue
        elif menu == 1:
            while True:
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
                placa = input('Digite a placa do veículo: ').strip()
                while not placa:
                    print(f'{cores["vermelho"]}ERRO, você precisa digitar algo{cores["fechacor"]}')
                    placa = input('Digite a placa do veículo: ').strip()
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
                else:
                    estacionamento[vaga].append(horae)
                    estacionamento[vaga].append(horas)
                    estacionamento[vaga].append(motorista)
                    estacionamento[vaga].append(placa)
                    print()
                    print(f'{cores["verde"]}Horário cadastrado com sucesso na{cores["fechacor"]} {vaga}.')
                    print()
                con = input('Deseja cadastrar outro horário? [s/n]: ')
                if con in 'Nn':
                    break

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
                    print(f'{cores["vermelho"]}Hora entrada: {values[0]} / hora saída: {values[1]}'
                          f'/ MOTORISTA: {values[2]} / PLACA: {values[3]}{cores["fechacor"]}')
                else:
                    print(f'{cores["verde"]}VAGA LIVRE!{cores["fechacor"]}')

            input('Pressione qualquer tecla para continuar:')
        elif menu == 5:
            print(f'{cores["azul"]}OBRIGADO POR USAR O GERÊNCIADOR DE VAGAS, SAINDO...{cores["fechacor"]}')
            sleep(1.4)
            break


programaprincipal()

