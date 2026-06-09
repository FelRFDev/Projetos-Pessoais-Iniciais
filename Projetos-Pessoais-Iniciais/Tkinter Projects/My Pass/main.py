# ---== Imports Tkinter
from tkinter import *
from tkinter import messagebox,Scrollbar,ttk

# ---== Outros imports
import json
import random
import pyperclip #import para copiar alguma informação para a área de transferência (ctrl + v)
import os


#---== Funções para criar os arquivos que servirão como banco de dados
def cria_txt(nome_do_usuario):
    """Função para gerar o arquivo txt com todos os dados cadastrados pelo usuário."""
    try:
        with open(f'./users_data/{nome_do_usuario}/dados.txt',mode='r'):
            pass
    except:
        with open(f'./users_data/{nome_do_usuario}/dados.txt',mode='w'):
            pass


def cria_websites(nome_do_usuario):
    """função para criar o arquivo onde ficará salvo todas as informações cadastradas pelo usuário."""
    try:
        with open(file=f'./users_data/{nome_do_usuario}/websites.json',mode='r'):
            pass
    except:
        with open(file=f'./users_data/{nome_do_usuario}/websites.json',mode='w') as websites:
            websites_lista = []
            json.dump(websites_lista,websites)
            pass


def usuarios_bd(nome_do_usuario):
    """função para criar arquivo com os dados do cadastro do usuário para login e uso deo programa."""
    try:
        with open(file=f'./users_data/{nome_do_usuario}/usuarios_bd.json',mode='r'):
            pass
    except:
        with open(file=f'./users_data/{nome_do_usuario}/usuarios_bd.json',mode='w') as file:
            cadastro_usuario = []
            json.dump(cadastro_usuario,file)


def cria_dir():
    """Função para verificar se já existe um determinado diretório, criando um
    caso não exista!"""
    pasta_existe = os.path.isdir('./users_data')
    if pasta_existe:
        pass
    else:
        os.mkdir('./users_data')



def cria_dir_user(nome_do_usuario):
    """Função para verificar se já existe um diretório criado para o usuário, e caso não exista,
    cria um de acordo com o nome informado."""
    pasta_existe = os.path.isdir(f'./users_data/{nome_do_usuario}')
    if pasta_existe:
        pass
    else:
        os.mkdir(f'./users_data/{nome_do_usuario}')
        cria_websites(nome_do_usuario)
        usuarios_bd(nome_do_usuario)
        cria_txt(nome_do_usuario)


 #---== criando diretório que irá conter as pastas com os dados para cada usuário

cria_dir() #Cria diretório onde ficará salvo os dados cadastrados pelos usuários


# ---------------------------- PASSWORD GENERATOR CONSTANTES ------------------------------- #
minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                         'o','p','q','r','s','t','u','v','x','y','w','z']

maiusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                     'O','P','Q','R','S','T','U','V','X','Y','W','Z',]

numeros=['0','1','2','3','4','5','6','7','8','9']

simbolos = ['!','@','#','$','%','&','*','?']

senha_ocultada = ''



# ---------------------------- PASSWORD GENERATOR ESTRUTURA PRINCIPAL ------------------------------- #

#função para o botão cadastrar
def gerar_cadastro():
    #configs da janela de cadastro

    tela_de_cadastro = Toplevel()
    tela_de_cadastro.grab_set()
    tela_de_cadastro.focus_set()
    tela_de_cadastro.geometry('600x600')
    tela_de_cadastro.title('CADASTRO DE USUÁRIO')
    tela_de_cadastro.config(bg='light cyan')
    tela_de_cadastro.resizable(width=False,height=False)

    cadastro_logo = PhotoImage(master=tela_de_cadastro,file='cadastro.png')
    cadastro_logo_canvas = Canvas(master=tela_de_cadastro,width=200,height=200,highlightthickness=0,bg='light cyan')
    cadastro_logo_canvas.create_image((100,100),image=cadastro_logo)
    cadastro_logo_canvas.place(x=205,y=30)

    user_cadastro_label=Label(master=tela_de_cadastro,text='Escolha um nome para o seu usuário!',
                              font=('Verdana',12,'bold'),fg='gray',bg='light cyan',highlightthickness=0)
    user_cadastro_label.place(x=140,y=290)

    user_cadastro = Entry(master=tela_de_cadastro,width=50,borderwidth=3,relief='groove')
    user_cadastro.place(x=150,y=350)


    user_senha_label = Label(master=tela_de_cadastro,text='Digite uma senha!',
                             font=('Verdana',12,'bold'),fg='gray',bg='light cyan',highlightthickness=0)
    user_senha_label.place(x=220,y=400)

    senha_cadastro = Entry(master=tela_de_cadastro,width=50,borderwidth=3,relief='groove')
    senha_cadastro.place(x=150,y=450)

    #função para o botão confirmar cadastro
    def confirma_cadastro():
        usuario = str(user_cadastro.get())
        senha = str(senha_cadastro.get())

        cria_dir_user(usuario)

        with open(file=f'./users_data/{usuario}/usuarios_bd.json',mode='r') as users_file:
            usuarios_cadastrados = json.load(users_file)
            try:
                if not usuario or not senha or not usuario and not senha:
                    raise ValueError('Você não preencheu todos os campos! Tente novamente.')
            except ValueError as erro:
                messagebox.showerror('ERRO!',f'{erro}')
            else:
                if len(usuarios_cadastrados) == 0:
                    user_data = [usuario,senha]
                    usuarios_cadastrados.append(user_data)
                    with open(file=f'./users_data/{usuario}/usuarios_bd.json',mode='w') as users_file:
                        json.dump(usuarios_cadastrados,users_file)
                        messagebox.showinfo('SUCESSO','Cadastro realizado! Faça login para acessar o menu principal')
                        tela_de_cadastro.destroy()
                else:
                    for user_cadastrado in usuarios_cadastrados:
                        try:
                            if usuario == user_cadastrado[0]:
                                raise ValueError('Usuário já cadastrado!')
                        except ValueError as erro:
                            messagebox.showerror('ERRO',f'{erro}')
                        else:
                            user_data = [usuario, senha]
                            usuarios_cadastrados.append(user_data)
                            with open(file=f'./users_data/{usuario}/usuarios_bd.json', mode='w') as users_file:
                                json.dump(usuarios_cadastrados, users_file)
                                messagebox.showinfo('SUCESSO',
                                                    'Cadastro realizado! Faça login para acessar o menu principal!')
                                tela_de_cadastro.destroy()
                                break

    botao_confirmar_cadastro = Button(master=tela_de_cadastro,text='CADASTRAR!',font=('Verdana',10,'bold'),border=2,fg='gray',
                          borderwidth=4,command=confirma_cadastro)
    botao_confirmar_cadastro.place(x=245,y=530)


    tela_de_cadastro.mainloop()


#---== função para o botão fazer login
def user_logado():

    global user_on

    try:
        user_typed = str(user_entry.get())
        pass_typed = str(password_entry.get())

        #verifica se os campos de usuário e senha não foram preenchidos
        if not user_typed or not pass_typed or not user_typed and pass_typed:
            user_on = False
            raise ValueError('Você não preencheu todos os campos de login!')
    except ValueError as erro:
        messagebox.showerror('ERRO',f'{erro}')

    else:
        #verifica se a pasta com o nome do usuário digitado existe
        verifica_pasta = os.path.isdir(f'./users_data/{user_typed}/')

        #lista todos os diretórios dentro de uma determinada pasta de acordo com o path informado e realiza a contagem
        diretorio = len(os.listdir('./users_data/'))

        if diretorio == 0 and verifica_pasta == False:
            messagebox.showerror('ERRO',"Não foi encontrado nenhum usuário cadastrado no sistema!\nCadastre-se para"
                                        " ter acesso ao menu principal!")
        elif diretorio > 0 and verifica_pasta == False:
            messagebox.showerror('ERRO', 'Informações inválidas, tente novamente!')

        else:
            with open(file=f'./users_data/{user_typed}/usuarios_bd.json',mode='r') as user_file:
                cadastrados = json.load(user_file)
                for cadastro in cadastrados:
                    if user_typed == cadastro[0] and pass_typed == cadastro[1]:
                        user_on = True
                        break #é preciso usar este break para que o valor de user_on não seja alterado nos próximos loops
                    else:
                        user_on = False
                if user_on == False:
                    messagebox.showerror('ERRO','Informações inválidas, tente novamente!')
                else:
                    messagebox.showinfo('SUCESSO', f'Login efeutado com sucesso!\nBem vindo -=>[{user_typed}]<=-')
                    def janela_cadastro():

                        #função para o botão de gerar senha
                        def gera_senha():
                            global minusculas, maiusculas, numeros, simbolos

                            # --===configurando a janela de personalização da senha
                            gerando_senha=Toplevel()
                            gerando_senha.focus_set()
                            gerando_senha.grab_set()
                            gerando_senha.geometry('300x260')
                            gerando_senha.resizable(width=False,height=False)
                            gerando_senha.title('Personalizando a senha')

                            gerando_senha_frame = Frame(master=gerando_senha,width=320,height=50,borderwidth=1,
                                                        bg='light gray',relief='solid')
                            gerando_senha_frame.place(x=-4,y=10)

                            gerando_senha_label = Label(master=gerando_senha,text='Personalize sua senha com as opções '
                                                                                  'abaixo!',
                                                        font=('arial',10,'bold'),bg='light gray',highlightthickness=0)
                            gerando_senha_label.place(x=-1,y=20)

                            # --=Adicionando checkbuttons para personalizar a senha

                            minusculas_var = IntVar()
                            maiusculas_var = IntVar()
                            numeros_var = IntVar()
                            simbolos_var = IntVar()

                            # ---= cada checkbutton irá retornar 0 se não for marcado ou 1 caso seja marcado
                            minusculas_chkm = Checkbutton(master=gerando_senha,text='Incluir letras minúsculas',
                                                          variable=minusculas_var)

                            minusculas_chkm.place(x=80,y=70)
                            maiusculas_chkm = Checkbutton(master=gerando_senha,text='Incluir letras MAIÚSCULAS',
                                                          variable=maiusculas_var)

                            maiusculas_chkm.place(x=80,y=90)
                            numeros_chkm = Checkbutton(master=gerando_senha,text='Incluir números',
                                                       variable=numeros_var)

                            numeros_chkm.place(x=80,y=110)
                            simbolos_chkm = Checkbutton(master=gerando_senha,text='Incluir símbolos',
                                                        variable=simbolos_var)
                            simbolos_chkm.place(x=80,y=130)

                            # --= Função para gerar a senha
                            def nova_senha():
                                global minusculas, maiusculas, numeros, simbolos

                                # ---= obtendo os valores dos checkbuttons
                                minusculas_opc = minusculas_var.get()
                                maiusculas_opc = maiusculas_var.get()
                                numeros_opc = numeros_var.get()
                                simbolos_opc = simbolos_var.get()

                                if minusculas_opc == 0 and maiusculas_opc == 0 and numeros_opc == 0 and \
                                        simbolos_opc == 0:
                                    numeros_sorteados = "".join(random.sample(numeros,random.randint(1,3)))
                                    minusculas_sorteados = "".join(random.sample(minusculas,random.randint(2,7)))
                                    maiusculas_sorteados = "".join(random.sample(maiusculas,random.randint(2,5)))
                                    simbolos_sorteados = "".join(random.sample(simbolos,random.randint(1,3)))

                                    senha = [numeros_sorteados + minusculas_sorteados + maiusculas_sorteados
                                             + simbolos_sorteados]
                                    random.shuffle(senha) #---= Embaralhando os elementos sorteados

                                    senha_final=''.join(senha)

                                    password_entry.delete(0, END) # ---= Limpa a entry do password
                                    password_entry.insert(INSERT,senha_final) # ---= insere na entry a senha gerada
                                    pyperclip.copy(senha_final)
                                    messagebox.showinfo('Senha copiada','A senha gerada foi copiada para a área de '
                                                                        'transferência!\n'
                                                                        '          Utilize Control + V para colar onde '
                                                                        'quiser.')
                                    gerando_senha.destroy()

                                    # ---= retoma o foco na janela de cadastro
                                    tela_de_cadastro.grab_set()
                                    tela_de_cadastro.focus_set()
                                else:
                                    opcs_validas = [minusculas_opc,maiusculas_opc,numeros_opc,simbolos_opc]

                                    # os números dentro das listas correspondem a quantidade de elementos a
                                    # serem sorteados(minimo,maximo)
                                    opcoes = [[minusculas,2,7],[maiusculas,2,5],[numeros,1,3],[simbolos,1,3]]

                                    senha=''

                                    # este laço for retornará uma tupla com números no índice 0 e o valor 0 ou 1
                                    # resultante das variáveis.get()
                                    for escolhas in enumerate(opcs_validas):

                                        if escolhas[1] == 1:
                                            # opcoes[escolhas[0]][1]) ou[0][2] correspondem aos números das listas dentro da lista opções
                                            # opções [escolhas[0]][0] corresponde ao tipo de elemento a ser sorteado na lista opções
                                            # se o valor no índice de escolhas[0] for == 1.
                                            senha+=(''.join(random.sample(opcoes[escolhas[0]][0],random.randint(
                                                opcoes[escolhas[0]][1],opcoes[escolhas[0]][2])))
                                                    )
                                    password_entry.delete(0,END)
                                    password_entry.insert(INSERT,string=senha)
                                    pyperclip.copy(senha)
                                    messagebox.showinfo('Senha copiada','A senha gerada foi copiada para a área de '
                                                                        'transferência!\n'
                                                                        '          Utilize Control + V para colar '
                                                                        'onde quiser.')
                                    gerando_senha.destroy()

                                    tela_de_cadastro.grab_set()
                                    tela_de_cadastro.focus_set()


                            botao_confirmar = Button(master= gerando_senha,text='Confirmar!',command=nova_senha,
                                                     borderwidth=2)

                            botao_confirmar.place(x=115,y=180)
                            gerando_senha.mainloop()


                        # ---------------------------- SAVE PASSWORD ------------------------------- #
                        def save_dados():

                            nome_user = user_entry.get()

                            website = website_entry.get()
                            user = email_username_entry.get()
                            password = password_entry.get()

                            with open(file=f'./users_data/{nome_user}/websites.json',mode='r') as websites:
                                listas = json.load(websites)
                                try:
                                    for lista in listas:
                                        if website in lista[0]:
                                            raise ValueError('Este site já foi cadastrado!')
                                        elif not website or not user or not password:
                                            raise ValueError('Você não preencheu todos os campos, tente novamente!')
                                except ValueError as erro:
                                    messagebox.showerror('Informação inválida!',f'{erro}')
                                else:
                                    #retorna True se o usuário escolher OK ou False se escolher cancel
                                    confirma_cadastro = messagebox.askokcancel('Confirmar cadastro',f'Estas são as informações inseridas:\n\n'
                                                                                                    f'Website: {website}\nUsuário: {user}\n'
                                                                                                    f'Senha: {password}\n\n'
                                                                                                    f'Cadastrar informações?')
                                    if confirma_cadastro:
                                        dados = [website,user,password]
                                        listas.append(dados)
                                        print(listas)
                                        with open(file=f'./users_data/{nome_user}/websites.json',mode='w') as websites:
                                            json.dump(listas,websites)

                                        website_entry.delete(0,END)
                                        email_username_entry.delete(0,END)
                                        password_entry.delete(0,END)
                                        messagebox.showinfo('SUCESSO','As Informações foram cadastradas no banco de dados!!')
                                    else:
                                        pass


                        # ---------------------------- UI SETUP ------------------------------- #
                        # --===== Configurações da janela de cadastro
                        tela_de_cadastro = Toplevel()
                        tela_de_cadastro.geometry('500x550')
                        tela_de_cadastro.title('My Pass By: FelRFDev')
                        tela_de_cadastro.config(padx=20,pady=20)
                        tela_de_cadastro.resizable(width=False,height=False)
                        #---Configurações do programa

                        #inserindo logo
                        logo_img = PhotoImage(master=tela_de_cadastro,file='logo.png')
                        logo_canvas=Canvas(master=tela_de_cadastro,width=200,height=200)
                        logo_canvas.create_image((100,100),image=logo_img)
                        logo_canvas.place(x=130,y=-10)

                        #--------inserindo Labels/Entrys
                        frame = Frame(master=tela_de_cadastro,borderwidth=0.5,width=436,height=300,relief='solid',
                                      bg='light gray')

                        website_title = Label(master=tela_de_cadastro,text='Website:',font=('Arial',10, 'bold'),
                                              bg='light gray',highlightthickness=0)
                        website_title.place(x=74,y=200)

                        website_entry = Entry(master=tela_de_cadastro,width=35,borderwidth=2)
                        website_entry.place(x=140,y=200)
                        website_entry.focus()

                        email_username_label= Label(master=tela_de_cadastro,text='Email/Username:',font=('Arial',10,'bold'),
                                                    bg='light gray',highlightthickness=0)
                        email_username_label.place(x=22, y=242)

                        email_username_entry = Entry(master=tela_de_cadastro,width=35,borderwidth=2)
                        email_username_entry.place(x=140,y=244)

                        #------- Criando uma subjanela para a seleção de domínios de e-mail
                        def listar_dominios():
                            dominios_list = Toplevel()
                            dominios_list.focus_set()
                            dominios_list.grab_set()
                            dominios_list.geometry('300x200')
                            dominios_list.resizable(width=False,height=False)

                            dominios_frame = Frame(master=dominios_list,width=320,height=50,borderwidth=1,
                                                   bg='light gray',relief='solid')
                            escolha_dominio_label = Label(master=dominios_list,
                                                          text='Escolha um domínio abaixo clicando em\n cima da opção '
                                                                                    'desejada.',font=('arial',10,'bold'),
                                                          bg='light gray')
                            escolha_dominio_label.place(x=14,y=10)
                            dominios_frame.place(x=-2,y=5)

                            #----criando um listbox com as opções de domínios
                            lista_de_dominios=[
                                '@gmail.com',
                                '@yahoo.com.br',
                                '@outlook.com',
                                '@hotmail.com',
                            ]

                            #------ Função da listbox que retorna o domínio selecionado
                            def selecionar_dominio(event):
                                dominio_selecionado = dominios_listbox.get(dominios_listbox.curselection())

                                # --- faz uma validação abaixo e caso a entry esteja vazia, preenche com a opção escolhida
                                # --- se a entry já estiver preenchida, apaga e preenche com a nova opção escolhida
                                if not email_username_entry.get() or email_username_entry.get() not in lista_de_dominios:
                                    email_username_entry.insert(END,string=dominio_selecionado)
                                else:
                                    email_username_entry.delete(0,END)
                                    email_username_entry.insert(END, string=dominio_selecionado)

                                dominios_list.destroy()
                                tela_de_cadastro.grab_set()
                                tela_de_cadastro.focus_set()

                            #------ Início da estrutura da listbox
                            dominios_listbox = Listbox(master=dominios_list,height=4,borderwidth=3) #---definindo as dimensões da listbox
                            for dominio in lista_de_dominios: #----inserindo as opções da lista na listbox pelo indice, elemento
                                dominios_listbox.insert(lista_de_dominios.index(dominio),dominio)
                            dominios_listbox.bind('<<ListboxSelect>>',selecionar_dominio) #----Indicando a funcionalidade da listbox
                            dominios_listbox.place(x=90,y=80)

                            dominios_list.mainloop()


                        escolher_dominio_button = Button(master=tela_de_cadastro,text='Escolher\nDomínio',
                                                         font=('arial',8,'bold'),command=listar_dominios)
                        escolher_dominio_button.place(x=368,y=238)


                        password_label = Label(master=tela_de_cadastro,text='Password / Senha:',font=('arial',10,'bold'),
                                               bg='light gray',highlightthickness=0)
                        password_label.place(x=14,y=296)

                        password_entry=Entry(master=tela_de_cadastro,width=21,borderwidth=2)
                        password_entry.place(x=140,y=296)

                        generate_password_button = Button(master=tela_de_cadastro,text='Gerar Password',
                                                          font=('arial',9,'bold'),borderwidth=2,command=gera_senha)
                        generate_password_button.place(x=280,y=294)

                        add_button = Button(master=tela_de_cadastro,text='ADICIONAR',font=('arial',8,'bold'),borderwidth=2,
                                            width=36,command=save_dados)
                        add_button.place(x=138,y=360)

                        frame.place(x=12,y=190)
                        tela_de_cadastro.grab_set()
                        tela_de_cadastro.focus_set()
                        tela_de_cadastro.mainloop()


                    #--========= Funções dos botões da janela principal

                    def janela_gerenciamento():
                        janela_gerenciar = Toplevel()
                        janela_gerenciar.grab_set()
                        janela_gerenciar.focus_set()
                        janela_gerenciar.title('Gerenciando informações')
                        janela_gerenciar.geometry('500x460')
                        janela_gerenciar.resizable(width=False,height=False)

                        vertical_frame_gerenciar = Frame(master=janela_gerenciar, width=100, height=600, borderwidth=2,
                                                         bg='light blue')

                        vertical_frame_gerenciar.place(x=0, y=5)


                        horizontal_frame_gerenciar = Frame(master=janela_gerenciar, width=600, height=70, borderwidth=2,
                                                           bg='light blue')

                        horizontal_frame_gerenciar.place(x=100, y=5)
                        lg2_imagem = PhotoImage(master=janela_gerenciar,file='lg2.png')
                        lg2_canvas = Canvas(master=janela_gerenciar,width=366,height=300)
                        lg2_canvas.create_image((150,150),image=lg2_imagem)
                        lg2_canvas.place(x=150,y=120)

                        def remover_senha():
                            removendo_senha = Toplevel()
                            removendo_senha.geometry('600x500')
                            removendo_senha.resizable(width=False, height=False)
                            removendo_senha.title('Remover senha')

                            remover_frame = Frame(master=removendo_senha,width=600,height=60,bg='light blue')
                            remover_frame.place(x=0,y=5)

                            remover_label = Label(master=removendo_senha,text='Digite no campo abaixo o Website\n'
                                                                              ' para remover a senha.',
                                                  bg='light blue',font=('arial',10,'bold'))
                            remover_label.place(x=190,y=15)

                            escolher_senha = Entry(master=removendo_senha,width=30,borderwidth=3)
                            escolher_senha.focus()
                            escolher_senha.place(x=190,y=420)

                            style = ttk.Style()
                            style.theme_use("clam")
                            style.configure("Treeview",
                                            background='light gray',
                                            foreground='black',
                                            rowheight=25,
                                            fieldbackground='light gray'
                                            )


                            tv = ttk.Treeview(master=removendo_senha, height=3,
                                              columns=('Col1', 'Col2', 'Col3'))  # especificando o número de colunas

                            # ---==== nomeando os cabeçalhos
                            tv.heading('#0', text='')
                            tv.heading('#1', text='WEBSITE', anchor=CENTER)
                            tv.heading('#2', text='USUÁRIO', anchor=CENTER)
                            tv.heading('#3', text='SENHA', anchor=CENTER)

                            # ---==== definindo o tamanho das colunas
                            tv.column('#0', width=1, stretch=NO)
                            tv.column('#1', width=150)
                            tv.column('#2', width=200)
                            tv.column('#3', width=200)

                            # ---==== criando a barra de rolagem

                            # definindo a orientação da barra de rolagem seguido do comando da treeview
                            # para visualizar verticalmente usando as setas da barra de rolagem
                            barra_de_rolagem = Scrollbar(master=removendo_senha, orient='vertical',
                                                         command=tv.yview)
                            tv.configure(
                                yscrollcommand=barra_de_rolagem.set)  # vinculando a barra de rolagem na treeview
                            barra_de_rolagem.place(relx=0.96, rely=0.1, relwidth=0.04,
                                                   relheight=0.70)  # posicionando a barra de rolagem
                            user_nome = user_entry.get()
                            with open(file=f'./users_data/{user_nome}/websites.json', mode='r') as senhas:
                                cadastro = json.load(senhas)
                                for (website, user, senha) in cadastro:
                                    senha_ocultada = ('*' * len(senha))
                                    tv.insert("", 'end', values=(website, user, senha_ocultada))
                            # ---==== posicionando a treeview
                            tv.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.70)

                            def confirmar():
                                user_nome = user_entry.get()
                                tv.delete(*tv.get_children())
                                with open(file=f'./users_data/{user_nome}/websites.json',mode='r') as arquivo:
                                    cadastrados=json.load(arquivo)

                                    if not cadastrados:
                                        messagebox.showinfo('Informação inválida', 'Nenhuma informação foi cadastrada até'
                                                                            ' o momento!')
                                    else:
                                        remocao_concluida= ''
                                        for web in cadastrados:
                                            if escolher_senha.get() not in web:
                                                remocao_concluida=False
                                            else:
                                                with open(file=f'./users_data/{user_nome}/websites.json', mode='r') \
                                                        as arquivo:
                                                    cadastrados = json.load(arquivo)
                                                    indice = cadastrados.index(web)
                                                    cadastrados.pop(indice)
                                                with open(file=f'./users_data/{user_nome}/websites.json', mode='w') \
                                                        as arquivo:
                                                    json.dump(cadastrados,arquivo)
                                                remocao_concluida = True

                                                for (website,usuario,senha) in cadastrados:
                                                    tv.insert("","end",values=(website,usuario,senha))
                                                break

                                        if remocao_concluida == False:
                                            messagebox.showerror('Informação inválida','Este site não foi cadastrado'
                                                                                               ' ou foi removido!')
                                        else:
                                            messagebox.showinfo('SUCESSO!',f'Você removeu {escolher_senha.get()}'
                                                                           f' com sucesso!')


                            confirmar_remover = Button(master=removendo_senha,text='REMOVER',borderwidth=3,command=confirmar)
                            confirmar_remover.place(x=400,y=414)



                            removendo_senha.grab_set()
                            removendo_senha.focus_set()
                            removendo_senha.mainloop()


                        botao_remover_senha = Button(master=janela_gerenciar,text='Remover\nSenha',borderwidth=3,
                                                     highlightthickness=0,
                                                     width=10,height=5,command=remover_senha)
                        botao_remover_senha.place(x=10,y=80)

                        def gera_txt():
                            user_entry.get()

                            with open(file=f'./users_data/{user_entry.get()}/websites.json',mode='r') as user_file:
                                user_data = json.load(user_file)
                                with open(f'./users_data/{user_entry.get()}/dados.txt', mode='w+') as dados:
                                    for cadastro in user_data:
                                        dados.write(f'Website: {cadastro[0]} / Username: {cadastro[1]} / Senha: {cadastro[2]}\n')
                                messagebox.showinfo('SUCESSO!', 'Informações salvas com sucesso no arquivo de texto.')

                        botao_criar_txt = Button(master=janela_gerenciar,text='Criar arquivo\nTXT',borderwidth=3,
                                                    highlightthickness=0,
                                                    width=10,height=5,command=gera_txt)
                        botao_criar_txt.place(x=10,y=320)

                        def limpar_cadastro():
                            continuar = messagebox.askokcancel("AVISO!!","Você está prestes a apagar todos os dados.\n"
                                                               "Se continuar, não será possível resgatar as informações"
                                                               " cadastradas.\n\nDeseja continuar?")
                            if continuar:
                                with open(file=f'./users_data/{user_entry.get()}/websites.json',mode='r') as file:
                                    cadastro=json.load(file)
                                    cadastro.clear()
                                    with open(file=f'./users_data/{user_entry.get()}/websites.json',mode='w') as file:
                                        json.dump(cadastro,file)
                                messagebox.showinfo('SUCESSO!',"CADASTRO APAGADO COM SUCESSO!")


                        botao_limpar_cadastro = Button(master=janela_gerenciar,text='Limpar\nCadastro',borderwidth=3,
                                                    highlightthickness=0,width=10,height=5,command=limpar_cadastro)
                        botao_limpar_cadastro.place(x=10,y=200)


                        janela_gerenciar.mainloop()

                    def ver_cadastro():
                        janela_ver_cadastro = Toplevel()
                        janela_ver_cadastro.focus_set()
                        janela_ver_cadastro.grab_set()
                        janela_ver_cadastro.geometry('600x400')
                        janela_ver_cadastro.title('Informações cadastradas')
                        janela_ver_cadastro.resizable(width=False,height=False)

                        # ---== Foi preciso inserir o valor True neste escopo pois ao fechar a janela de visualizar senha
                        #  com a senha visível, era necessário clicar no botão duas vezes para exibir a senha oculta ao reabrir a janela
                        global senha_ocultada
                        senha_ocultada=True # variável de controle para exibir ou ocultar a senha

                        #configurando o estilo da Treeview
                        style = ttk.Style()
                        style.theme_use("clam")
                        style.configure("Treeview",
                                        background='light gray',
                                        foreground='black',
                                        rowheight=25,
                                        fieldbackground='light gray'
                                        )



                        ver_cadastro_frame = Frame(master=janela_ver_cadastro,width=572,height=40,bg='light blue')
                        ver_cadastro_label = Label(master=janela_ver_cadastro,text='INFORMAÇÕES CADASTRADAS',
                                                   foreground='LightBlue4',
                                                   bg='light blue',
                                                   font=('Impact',16))
                        ver_cadastro_frame.place(x=5,y=0)
                        ver_cadastro_label.place(x=180,y=10)



                        #---==== criando uma Treeview
                        tv = ttk.Treeview(master=janela_ver_cadastro,height=3,columns=('Col1','Col2','Col3')) #especificando o número de colunas

                        #---==== nomeando os cabeçalhos
                        tv.heading('#0',text='')
                        tv.heading('#1',text='WEBSITE',anchor=CENTER)
                        tv.heading('#2',text='USUÁRIO',anchor=CENTER)
                        tv.heading('#3',text='SENHA',anchor=CENTER)

                        #---==== definindo o tamanho das colunas
                        tv.column('#0',width=1,stretch=NO)
                        tv.column('#1',width=150)
                        tv.column('#2',width=200)
                        tv.column('#3',width=200)

                        #---==== criando a barra de rolagem

                        # definindo a orientação da barra de rolagem seguido do comando da treeview
                        # para visualizar verticalmente usando as setas da barra de rolagem
                        barra_de_rolagem = Scrollbar(master=janela_ver_cadastro,orient='vertical',command=tv.yview)
                        tv.configure(yscrollcommand=barra_de_rolagem.set)#vinculando a barra de rolagem na treeview
                        barra_de_rolagem.place(relx=0.96, rely=0.1,relwidth=0.04,relheight=0.70)#posicionando a barra de rolagem

                        def exibir_senha():
                            tv.delete(*tv.get_children()) #limpa todos os dados da treeview

                            user_nome = user_entry.get()

                            global senha_ocultada

                            if senha_ocultada:
                                with open(file=f'./users_data/{user_nome}/websites.json', mode='r') as senhas:
                                    cadastro = json.load(senhas)
                                    for (website, user, senha) in cadastro:
                                        tv.insert("", 'end', values=(website, user, senha))
                                senha_ocultada=False

                            else:
                                with open(file=f'./users_data/{user_nome}/websites.json', mode='r') as senhas:
                                    cadastro = json.load(senhas)
                                    for (website, user, senha) in cadastro:
                                        senha_ocultada = ('*' * len(senha))
                                        tv.insert("", 'end', values=(website, user,senha_ocultada))
                                senha_ocultada=True



                        user_nome= user_entry.get()
                        with open(file=f'./users_data/{user_nome}/websites.json',mode='r') as senhas:
                            cadastro = json.load(senhas)
                            for (website,user,senha) in cadastro:
                                senha_ocultada = ('*'* len(senha))
                                tv.insert("",'end',values=(website,user,senha_ocultada))
                        #---==== posicionando a treeview
                        tv.place(relx=0.01,rely=0.1,relwidth=0.95,relheight=0.70)

                        eye_img = PhotoImage(master=janela_ver_cadastro,file='blueeye_resized.png')
                        botao_ocultar_exibir_senhas = Button(master=janela_ver_cadastro, text='OCULTAR / EXIBIR\nSENHAS',
                                                             font=('arial',8,'bold'),
                                                             command=exibir_senha,image=eye_img,compound=LEFT)
                        botao_ocultar_exibir_senhas.place(x=200,y=350)


                        janela_ver_cadastro.mainloop()



                    # --========= Criando e Configurando janela principal
                    root_window = Toplevel()
                    root_window.focus_set()
                    root_window.grab_set()
                    root_window.title('My Pass By: FelRFDev')
                    root_window.geometry('700x600')
                    root_window.resizable(width=False,height=False)


                    vertical_frame = Frame(master=root_window,width=100,height=600,borderwidth=2,bg='light blue')
                    vertical_frame.place(x=0,y=5)

                    horizontal_frame = Frame(master=root_window,width=600,height=70,borderwidth=2,bg='light blue')
                    horizontal_frame.place(x=100,y=5)

                    botao_cadastrar = Button(master=root_window,text='Cadastrar\nSenhas',width=10,height=5,borderwidth=4,
                                             command=janela_cadastro)
                    botao_cadastrar.place(x=10,y=160)


                    botao_visualizar = Button(master=root_window,text='Visualizar\nSenhas',width=10,height=5,borderwidth=4,
                                              command=ver_cadastro)
                    botao_visualizar.place(x=10,y=280)



                    botao_gerenciar = Button(master=root_window,text='Gerenciar\nSenhas',width=10,height=5,borderwidth=4,
                                             command=janela_gerenciamento)
                    botao_gerenciar.place(x=10,y=400)

                    mini_logo=PhotoImage(master=root_window,file='lp.png')
                    mini_canvas = Canvas(master=root_window,width=100,height=100,bg='black',highlightthickness=1)
                    mini_canvas.create_image((50,50),image=mini_logo)
                    mini_canvas.place(x=180,y=1)

                    fel_label = Label(master=root_window,text='MY PASS / Desenvolvido por FelRFDev',
                                      font=('Courier',12,'bold'),
                                      bg='light blue')
                    fel_label.place(x=290,y=30)

                    main_logo = PhotoImage(master=root_window,file='main_logo.png')

                    main_logo_canvas = Canvas(master=root_window,width=400,height=400)
                    main_logo_canvas.create_image((200,200),image=main_logo)
                    main_logo_canvas.place(x=200,y=140)

                    root_window.mainloop()



# ---------------------------- ESTRUTURA DA JANELA DE LOGIN ------------------------------- #

login_window=Tk()
login_window.geometry('1180x720')
login_window.resizable(width=False,height=False)
login_window.title('My Pass By FelRFDev Login')

user_on = ''

login_logo_image = PhotoImage(master=login_window,file='loginlogo.png')

login_logo_canvas=Canvas(master=login_window,width=590,height=720)
login_logo_canvas.create_image((295,360),image=login_logo_image)
login_logo_canvas.place(x=0,y=0)


login_field_frame=Frame(master=login_window,width=590,height=720,bg='light blue')
login_field_frame.place(x=590,y=0)

login_icon = PhotoImage(master=login_window,file='welc1.png')

login_icon_canvas=Canvas(master=login_window,width=250,height=250,bg='light blue',highlightthickness=0)
login_icon_canvas.create_image((125,125),image=login_icon)
login_icon_canvas.place(x=760,y=50)

entrys_field_frame=Frame(master=login_window,width=400,height=430,bg='light cyan',borderwidth=0.5,relief=SOLID)
entrys_field_frame.place(x=690,y=300)


user_entry = Entry(master=login_window,width=50,borderwidth=3,relief='groove')
password_entry = Entry(master=login_window,width=50,borderwidth=3,relief='groove')

welcome_label = Label(master=login_window,text='Bem vindo',fg='LightBlue4',font=('impact',50),bg='light blue',relief='flat')
welcome_label.place(x=742,y=10)


user_label_image = PhotoImage(master=login_window,file='user.png')
user_label_image_canvas = Canvas(master=login_window,width=40,height=40,highlightthickness=0)
user_label_image_canvas.create_image((20,20),image=user_label_image)
user_label_image_canvas.place(x=790,y=390)


user_entry_label = Label(master=login_window,text='USUÁRIO',font=('Verdana',12,'bold'),fg='gray',bg='light cyan',
                         highlightthickness=0)
user_entry_label.place(x=845,y=400)



password_label_image=PhotoImage(master=login_window,file='password.png')
password_label_image_canvas = Canvas(master=login_window,width=40,height=40,highlightthickness=0)
password_label_image_canvas.create_image((20,20),image=password_label_image)
password_label_image_canvas.place(x=790,y=500)


senha_entry_label= Label(master=login_window,text='SENHA',font=('Verdana',12,'bold'),fg='gray',bg='light cyan',
                         highlightthickness=0)
senha_entry_label.place(x=855,y=510)

user_entry.place(x=735,y=450)
password_entry.place(x=740,y=550)


login_button = Button(master=login_window,text='FAZER LOGIN',font=('Verdana',10,'bold'),border=2,fg='gray',
                      borderwidth=4,command=user_logado)
login_button.place(x=750,y=650)


cadastrar_button = Button(master=login_window,text='CADASTRAR-SE',font=('Verdana',10,'bold'),border=2,fg='gray',
                          borderwidth=4,command=gerar_cadastro)
cadastrar_button.place(x=900,y=650)


login_window.mainloop()
