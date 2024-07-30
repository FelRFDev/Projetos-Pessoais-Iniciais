import sys
from bw_funcoes import *
from b64_imgs import *


img_claro="""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"""

img_escuro = """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"""

img="""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"""





class Main_program(Bw_funcoes):
    def __init__(self):
        self.main_start = CTkToplevel()
        self.main_start.geometry("800x850+300+200")
        self.main_start.title('Janela de consultas')
        self.main_start.resizable(width=False, height=False)
        self.main_start_widgets()

        def on_closing():  # <====== Criando a função para definir o que irá acontecer com a janela.
            if messagebox.askokcancel("Sair", "Deseja voltar a tela inicial?"):
                self.main_start.destroy()
                #-=-=-=-=-=-= Inicio do comando para resetar o programa!
                menu = sys.executable # <= variável referente a janela princial
                os.execl(menu, menu, * sys.argv) # <= comando para executar a tela inicial do programa

        self.main_start.protocol("WM_DELETE_WINDOW",
                      on_closing)  # <===== Utilizando o protocol com wm_delete_window seguido da função criada.



        self.main_start.grab_set()
        self.main_start.focus_set()
        self.main_start.mainloop()

    def main_start_widgets(self):
        #-=-===-=-=-=-= Widgets =-=-=-=-=-=-=-==
        self.bee_img = PhotoImage(master=self.main_start, data=base64.b64decode(img2))

        self.bee_bg_img = Canvas(master=self.main_start, width=self.bee_img.width(), height=self.bee_img.height())
        self.bee_bg_img.create_image((self.bee_img.width()/2, self.bee_img.height()/2), image=self.bee_img)
        self.bee_bg_img.place(x=-1, y=-8)

        self.titulo1 = CTkLabel(master=self.main_start, text='Digite o que deseja saber no campo abaixo!')

        self.consulta_entry = CTkEntry(master=self.main_start, width=460,
                                       placeholder_text='Digite aqui a sua pesquisa...', bg_color='#cfa442',
                                       border_width=2)
        
        self.resposta_box = CTkTextbox(master=self.main_start,  width=460, height=310)


        self.botoes_bar = CTkFrame(master=self.main_start, width=860, height=300, fg_color='#2b2a27')



        self.botao_pesquisar = CTkButton(master=self.main_start, text='Pesquisar', bg_color='#2b2a27',
                                         command = self.obter_pesquisa)

        self.botao_gerar_audio = CTkButton(master=self.main_start, text='Gerar Audio', bg_color='#2b2a27',
                                           command=self.gera_audio)

        self.botao_gerar_pdf = CTkButton(master=self.main_start, text='Gerar Arquivo Word', bg_color='#2b2a27'
                                         ,command=self.gera_docx)

        self.botao_criar_pasta = CTkButton(master=self.main_start, text='Criar Pasta', bg_color='#2b2a27',
                                           command=self.cria_diretorio)

        self.img_to_txt_button = CTkButton(master=self.main_start, text='Converter Imagem em Texto', bg_color='#2b2a27',
                                           command=self.img_to_text)

        #-=-=-=-=-==-= Widgets Places =-=-=-=-=-
        self.resposta_box.place(x=20, y=186)
        self.consulta_entry.place(x=20, y=520)
        self.botoes_bar.place(x=-2, y=660)
        self.botao_pesquisar.place(x=40, y=690)
        self.botao_gerar_audio.place(x=240, y=690)
        self.botao_gerar_pdf.place(x=440, y=690)
        self.botao_criar_pasta.place(x=636, y=690)
        self.img_to_txt_button.place(x=200, y=750)


class Showing(Main_program):
    def __init__(self):
        self.presenting_window = CTk()
        self.presenting_window.geometry("760x610+360+200")
        self.presenting_window.title('Be Wise By: FelRFDev - V.1.0')
        self.presenting_imagem = PhotoImage(master=self.presenting_window, data=(base64.b64decode(presenting)))
        self.presenting_canvas = Canvas(master=self.presenting_window, width=self.presenting_imagem.width(),
                                        height=self.presenting_imagem.height())
        self.presenting_canvas.create_image((self.presenting_imagem.width()/2, self.presenting_imagem.height()/2),
                                            image=self.presenting_imagem)
        self.presenting_canvas.place(x=-3, y=0)

        self.top_frame = CTkFrame(master=self.presenting_window, width=800, height=90, fg_color='#1b1c1b')
        self.top_frame.place(x=-3, y=0)



        self.start_button_img = PhotoImage(master=self.presenting_window, data=base64.b64decode(start_b_img))
        self.st_canvas = Canvas(master=self.presenting_window, width=100,
                                height=80,
                                bg='#1b1c1b', highlightthickness=0)
        self.st_canvas.create_image((30, 17), image=self.start_button_img)
        self.st_canvas.place(x=332, y=7)

        self.st_botao = CTkButton(master=self.presenting_window, text='INICIAR!',font=('impact', 20), bg_color='#1b1c1b',
                                  command=self.fechar_apresentacao, width=100, height=26,text_color='black',
                                  fg_color='#f5da45')
        self.st_botao.place(x=332, y=32)


        self.presenting_window.mainloop()

    def fechar_apresentacao(self):
        self.presenting_window.withdraw()
        Main_program()


Showing()

