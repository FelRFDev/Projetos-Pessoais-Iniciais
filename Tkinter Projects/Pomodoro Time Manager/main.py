from tkinter import *
import webbrowser #importação para abrir links no navegador
import math
from pygame import mixer


# ---------------------------- AUDIO / VIDEO FUNCTIONS ------------------------------- #



def play_music(music):
    mixer.init()
    mixer.music.load(music)
    mixer.music.set_volume(0.3)
    mixer.music.play()


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#31F552"
YELLOW = "#f7f5dd"
BEGE = '#e6e6e1'
DARK = '#363634'

FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
repetition = 0 #quantidade de repetições
timer = None
reseted = False
start_on = False



# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_program():

    def start_timer():
        play_music('apito.mp3')
        global repetition
        global reseted


        reseted = True
        repetition+=1
        work_section = WORK_MIN * 60  # calculando os minutos para a seção de trabalho
        short_break_section = SHORT_BREAK_MIN * 60  # calculando os minutos para a seção de pausa curta
        long_break_section = LONG_BREAK_MIN * 60  # calculando os minutos para a seção de pausa longa

        if repetition % 8 == 0:
            play_music('apito.mp3')
            canvas = Canvas(master=window, width=300, height=300, bg=BEGE, highlightthickness=0)
            canvas.create_image((150, 150), image=long_break_image)
            canvas.create_text((148, 250), text='      LONG BREAK TIME!\nDESCANSO LONGO!',font=('arial',15,'bold'), fill=RED)
            canvas.grid(column=1, row=5)
            count_down(long_break_section)


        elif repetition % 2 ==0:
            play_music('apito.mp3')
            canvas = Canvas(master=window, width=300, height=300, bg=BEGE, highlightthickness=0)
            canvas.create_image((150,150), image=short_break_img)
            canvas.create_text((148, 250), text='      SHORT BREAK TIME!\nDESCANSO BREVE!',font=('arial',15,'bold'),fill=RED)
            canvas.grid(column=1, row=5)
            count_down(short_break_section)

        elif repetition % 9 == 0:
            play_music('jobdone.mp3')
            reset_timer()

        else:
            canvas = Canvas(master=window, width=300, height=300, bg=BEGE, highlightthickness=0)
            canvas.create_image((150,150), image=work_time_img)
            canvas.create_text((148, 250), text='       WORK TIME!\nHORA DE TRABALHAR!',font=('arial',15,'bold'),fill=GREEN)
            canvas.grid(column=1, row=5)
            count_down(work_section)

        if repetition >=1:
            start_button_window.config(state=DISABLED)
        elif repetition >5:
            start_button_window.config(state=NORMAL)



    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def count_down(count):
        count_min = math.floor(count / 60) #calculando o valor para minutos dividindo os segundos por 1 minuto
        count_sec = count % 60 #calculando o valor para segundos obtendo o resto da divisão dos segundos por minuto
        if count_sec < 10:
            count_sec = f'0{count_sec}'

        #reconfigurando o texto da tela(variavel_com_o_texto, define o novo texto de acordo com os cálculos acima)
        canvas.itemconfig(canv_text,text=f"{count_min}:{count_sec}")
        #executa uma ação depois de um determinado tempo(milisegundos, função a ser executada, parametros(*args))
        if count > 0:
            global timer
            timer = window.after(1000, count_down, count-1)
        else:
            #a partir daqui o contador já estará com o valor = 0 (zerado)
            start_timer()
            marks = " "
            #cada seccção equivale a um turno trabalhado e um intervalo, representado no cálculo abaixo
            work_sessions = math.floor(repetition/2)
            #calcula quantos turnos já se passaram e acrescentam as marcas de acordo com os turnos abaixo
            for _ in range(work_sessions):
                marks+=cm
            chkmk.config(text=marks)

    # ---------------------------- UI SETUP ------------------------------- #
    window = Toplevel()# Permite criar uma janela secundária/adicional


    play_music('start tema.wav')
    global root


    # ---------------------------- TIMER RESET ------------------------------- #

    def reset_timer():
        play_music('reset.mp3')
        global reseted
        global start_on

        if reseted == False and start_on == False:
            pass
        else:
            start_button_window.config(state=NORMAL)
            reseted = True
            window.after_cancel(timer)
            canvas.itemconfig(canv_text, text=f"00:00")  # configura um ítem específico de alguma varíavel de canvas
            chkmk.config(text=' ')
            global repetition
            repetition = 0

            blank_canvas = Canvas(master=window,width=300, height=300, bg=BEGE, highlightthickness=0)
            blank_canvas.grid(column=1, row=5)
            start_on = False

    # ---------------------------- TIMER RESET END ------------------------------- #

    window.title('Pomodoro Time Manager')
    window.config(padx=100,pady=50, bg=BEGE)


    clock_banner = PhotoImage(master=window,file='clkbanner.png')
    canvas_clk = Canvas(master=window,width=533,height=190,highlightthickness=0,bg=BEGE)
    canvas_clk.create_image((266,95),image=clock_banner)
    canvas_clk.grid(column=1,row=0)




    #imagens
    work_time_img=PhotoImage(master=window,file='worktime_resized.png')
    short_break_img=PhotoImage(master=window,file='shortbreak_resized.png')
    long_break_image=PhotoImage(master=window,file='longbreak_resized.png')




    cm = '✅'

    #criando uma subtela para adicionar a imagem
    img = PhotoImage(master=window,file='tomato.png') #armazenar a imagem em uma variável
    canvas = Canvas(master=window,width=200,height=224,bg=BEGE,highlightthickness=0) #criar uma tela com as dimensões da imagem / remove a borda da tela
    canvas.create_image((100,112),image=img) #indicar o posicionamento da imagem na tela e depois indicar qual é a imagem
    canv_text=canvas.create_text((100,130),text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
    canvas.grid(column=1,row=1) #usar um método de posicionamento




    start_button_window = Button(master=window,text='Start',highlightthickness=0,command=start_timer,width=14,height=2)
    start_button_window.grid(column=0,row=2)


    reset_button_window = Button(master=window,text='Reset',highlightthickness=0,width=14,height=2,command=reset_timer)
    reset_button_window.grid(column=2,row=2)

    chkmk = Label(master=window,text='',foreground=GREEN,highlightthickness=0,bg=BEGE)
    chkmk.grid(column=1,row=3)
    window.focus_force()#faz com que o programa foque nesta janela
    window.grab_set()#Trava a interação da janela principal até que o usuário feche a janela secundária
    window.mainloop()


def show_instructions():
    instructions_screen=Toplevel()
    play_music('instrucoes tema.wav')
    instructions_img = PhotoImage(master=instructions_screen,file='pomoinstruction.png')
    inscv = Canvas(master=instructions_screen,width=800, height=566)
    inscv.create_image((400, 240), image=instructions_img)
    inscv.grid()

    def sair():
        instructions_screen.destroy()

    back_button=Button(master=instructions_screen,text='VOLTAR',width=20,height=2,command=sair)
    back_button.place(x=320,y=490)
    instructions_screen.focus_force()#faz com que o programa foque nesta janela
    instructions_screen.grab_set()#Trava a interação da janela principal até que o usuário feche a janela secundária
    instructions_screen.mainloop()




def about_program():
    about = Toplevel()
    about.title('Sobre o programa')
    about.minsize(width=800,height=800)
    about.config(bg=BEGE)

    my_pic = PhotoImage(master=about,file='eu_resized.png')
    my_banner = PhotoImage(master=about,file='logopronta_resized.png')


    my_banner_canvas = Canvas(master=about,width=250,height=250,highlightthickness=0,bg=DARK)
    my_banner_canvas.create_image((125,125), image=my_banner)
    my_banner_canvas.place(x=360,y=0)

    my_pic_canvas = Canvas(master=about,width=153,height=250,highlightthickness=0)
    my_pic_canvas.create_image((76,125),image=my_pic)
    my_pic_canvas.place(x=230,y=0)

    text="""
    Pomodoro Time Manager é um software Open Source (Código Aberto)\n
    e gratuito, livre para uso! Este projeto foi criado para fins de\n
    estudo e se encontra em e Alfa Stage, sendo possível se deparar\n
    com algum bug, ou erro. Caso encontre, entre em contato com o \n
    desenvolvedor através do e-mail: comunidadehawks@gmail.com.\n
    Futuramente, penso em incluir mais ferramentas e funcionalidades\n
    sendo assim, fique ligado nas minhas redes sociais.\n
    Sugestões, dicas, feedback, e etc, envie mensagem para o e-mail acima!\n 
    MUITO OBRIGADO POR FAZER USO DO MEU PROGRAMA, EM BREVE MAIS NOVIDADES!
    """

    about_text = Label(master=about,text=text)
    about_text.place(x=160,y=300)


    def open_facebook():
        """Função para abrir um link externo no navegador"""
        webbrowser.open('https://www.facebook.com/FRFDev')

    face_icon = PhotoImage(file='faceicon.png')
    linkedin_icon = PhotoImage(file='kediniconr.png')
    instagram_icon = PhotoImage(file='insta2r.jpg')

    face_button = Button(master=about,text='FACEBOOK',command=open_facebook,image=face_icon,compound=LEFT)
    face_button.place(x=230,y=690)

    def open_linkedin():
        """Função para abrir um link externo no navegador"""
        webbrowser.open('https://www.linkedin.com/in/felrfdev/')

    linkedin_button = Button(master=about,text='LINKEDIN',command=open_linkedin,image=linkedin_icon,compound=LEFT)
    linkedin_button.place(x=380,y=690)

    def open_insta():
        """Função para abrir um link externo no navegador"""
        webbrowser.open('https://www.instagram.com/invites/contact/?i=1kbh42evchgjb&utm_content=n76897y')

    instagram_button = Button(master=about,text='INSTAGRAM',command=open_insta,image=instagram_icon,compound=LEFT)
    instagram_button.place(x=520,y=690)



    about.focus_force()
    about.grab_set()
    about.mainloop()



root = Tk()



play_music("tema abertura.wav")

root.title('Pomodoro Time Manager App / Feito por: Felipe Rodrigues Fonseca 31/10/2022')


bg_img = PhotoImage(master=root,file='cape_resized.png')
bgcv = Canvas(width=842, height=482)
bgcv.create_image((421,241),image=bg_img)
bgcv.grid()


start_button = Button(master=root,text='START',width=14,height=2,command=start_program)
start_button.place(x=610,y=180)


instruction_button = Button(master=root,text='INSTRUÇÕES',width=14,height=2,command=show_instructions)
instruction_button.place(x=610,y=250)

about_button = Button(master=root,text='SOBRE O PROGRAMA',width=20,height=2,command=about_program)
about_button.place(x=590,y=350)


root.mainloop()
