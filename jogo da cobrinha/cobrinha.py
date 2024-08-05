#Primeiro vamos realizar as configurações inicais.
import pygame
import random

pygame.init() #Inicializar o pygame
pygame.display.set_caption('Jogo Cobrinha') #Nome que vai ficar o jogo
largura, altura = 1200, 800 #Tamanho da tela do jogo. Largura e altura.
tela = pygame.display.set_mode((largura, altura))#armazena a tela
relogio = pygame.time.Clock()

#Cores-RGB
verde = (0, 255, 0)#Fundo
verdeescuro = (47, 79, 47)#Cobra
vermelha = (255, 0, 0)#Comida
preta = (0, 0, 0)#Pontuação

#parametros da cobrinha
tamanho_quadrado = 20 #Tamanho dos lados do quadrado
velocidade_jogo = 15 #Velociade do jogo/cobra

def gerar_comida(): #Vai gerar a comida
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) /float(tamanho_quadrado)) * float(tamanho_quadrado)
    #Feitos para que nenhum quadradinho (comida) apareça pra fora da tela. O round, é feito para arrendondar, para que a comida não fique desalinhada.
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) /float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y): #Deu e não deu certo kkk
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho_quadrado, tamanho_quadrado]) #pra comida aparecer de fato na tela

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, verdeescuro, [pixel[0], pixel[1], tamanho, tamanho]) 

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Arial", 25) #tamanho da pontuação
    texto = fonte.render(f'Pontos: {pontuacao}', True, preta)#Cor, o True é pra não ver o pixelado da escrita.
    tela.blit(texto, [1, 1]) #pra mostrar na tela, o 1 e 1 é pra não ficar grudado.

#Mostrar a menssagem que erdeu
def mostrar_mensagem(mensagem):
    fonte = pygame.font.SysFont("Arial", 50)
    texto = fonte.render(mensagem, True, preta)
    tela.blit(texto, [largura / 2.5, altura / 2])
    pygame.display.update()
    pygame.time.delay(2000)


def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_dojogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0 #Velociade em plano carteziano
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = [] 

    comida_x, comida_y = gerar_comida()

    while not fim_dojogo:
        tela.fill(verde) 

        for evento in pygame.event.get(): #Evento que o usuaria fez a cada instante.
            if evento.type == pygame.QUIT:
                fim_dojogo = True #Acaba o jogo.
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        desenhar_pontuacao(tamanho_cobra - 1)

        #Atualizar a posiçaõ da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_dojogo = True


        x += velocidade_x
        y += velocidade_y

        #desenhar_cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra: 
            del pixels[0] #pra deletar o ultimo pixel, rabo da cobra. 

        #Se a cobra bateu no prpprio corpo.
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_dojogo = True

        desenhar_cobra(tamanho_quadrado, pixels)

        #Atualização de tela
        pygame.display.update()#pra atualizar o jogo

        #Criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)
    tela.fill(verde)
    mostrar_mensagem('Você Perdeu!')

rodar_jogo()
