# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:27:41 2019

@author: dorad
"""

VERDE = (160, 231, 190)
VERMELHO = (205, 44, 65)
AZUL = (139, 165, 235)
AMARELO = (204, 173, 26)
LISTA_CORES = [VERDE, VERMELHO, AZUL, AMARELO]


# Importando as bibliotecas necessárias.
import pygame
import random
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'Imagens')

# Dados gerais do jogo.
WIDTH = 1200 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "dot_azul.png")).convert()

        self.image = player_img
        
        # Diminuindoo tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 50))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 50
        
        # Velocidade da nave
        self.speedx = 0
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
 
#------------------------------------------------------------------------------------
class Bolinhas(pygame.sprite.Sprite):
    
    
    #Construtor da classe
    def __init__(self, x, y):
        arq_cor = ["dot_rosa.png", "dot_amarelo.png", "dot_verde.png", "dot_azul.png"]
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.cor = random.randint(0,3)
        player_img = pygame.image.load(path.join(img_dir, arq_cor[self.cor])).convert()

        self.image = player_img
        
        # Diminuindoo tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (60, 60))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.x = x
        self.rect.y = y
        
        # Velocidade da nave
        self.speedx = 0
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
#------------------------------------------------------------------------------------
       
class Rosa(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "dot_rosa.png")).convert()

        self.image = player_img
        
        # Diminuindoo tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 50))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 4
        self.rect.bottom = HEIGHT - 50
        
        # Velocidade da nave
        self.speedx = 0
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Amarelo(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "dot_amarelo.png")).convert()

        self.image = player_img
        
        # Diminuindoo tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 50))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 150
        self.rect.bottom = HEIGHT - 50
        
        # Velocidade da nave
        self.speedx = 0
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
class Verde(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "dot_verde.png")).convert()

        self.image = player_img
        
        # Diminuindoo tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 50))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 6
        self.rect.bottom = HEIGHT - 50
        
        # Velocidade da nave
        self.speedx = 0
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


#Classe Mob que representa o meteoro
class Mob(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "dot_amarelo.png")).convert()
        self.image = player_img
        
        # Diminuindoo tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 50))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = random.randrange(0, WIDTH)
        self.rect.centery = random.randrange(-100,-40)
                
        # Velocidade do meteoro
        self.speedx = random.randrange(-3,3)
        self.speedy = random.randrange(2,9)
        
# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Pygame")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'fundo_cinza.png')).convert()
background = pygame.transform.scale(background,(WIDTH, HEIGHT))
background_rect = background.get_rect()

#Carrega imagem quadrado
quadrado = pygame.image.load(path.join(img_dir, 'quadrado_marrom.png')).convert()
quadrado.set_colorkey(WHITE)
quadrado = pygame.transform.scale(quadrado,(600, 600))

# Cria uma nave.  construtor será chamado automaticamente.
player = Player()

#cria dot rosa
#rosa = Rosa()

#Cria DOT verde
#verde = Verde()

#Cria DOT amarelo
#amarelo = Amarelo()

# Cria o meteoro.
meteoro = Mob()

# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()

xinit = 345 
yinit = HEIGHT-7*79

x = xinit
y = yinit
tam_bolinha = 76
tabuleiro_bolinha = []
for e in range(7):
    linha_bolinha = []
    for i in range(7):
        a1 = Bolinhas(x, y)
        all_sprites.add(a1)
        linha_bolinha.append(a1)
        x += tam_bolinha
    tabuleiro_bolinha.append(linha_bolinha)
    y += tam_bolinha
    x = xinit
    
    
    
"""
all_sprites.add(player)
all_sprites.add(rosa)
all_sprites.add(verde)
all_sprites.add(amarelo)
all_sprites.add(meteoro)
"""

# Cria um gruppo Mobs e Adiciona o meteoro.
mobs = pygame.sprite.Group()
mobs.add(meteoro)

lista_bolinhas = []
lista_sprites = []

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                xpos = event.pos[0]
                ypos = event.pos[1]
                j_bolinha = int((xpos - xinit)/tam_bolinha)
                i_bolinha = int((ypos - yinit)/tam_bolinha)
                
                if i_bolinha >= 0 and i_bolinha < 7 \
                    and j_bolinha >= 0 and j_bolinha < 7:
                    cor = tabuleiro_bolinha[i_bolinha][j_bolinha].cor
                    if len(lista_bolinhas) == 0:
                        lista_bolinhas.append((i_bolinha, j_bolinha, cor, xpos,ypos))
                        
                        
                    else:
                        ultima_bolinha = lista_bolinhas[-1]
                        nova_bolinha = (i_bolinha, j_bolinha, cor,xpos,ypos)
                        diferenca = (abs(ultima_bolinha[0] - i_bolinha), abs(ultima_bolinha[1] - j_bolinha))
                        if diferenca in [(1, 0), (0, 1)] and ultima_bolinha[2] == cor and not nova_bolinha in lista_bolinhas:
                            lista_bolinhas.append(nova_bolinha)
                            
                        
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
                
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
            
            # Verifica se soltou alguma tecla
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0

        # Depois de processar os eventos.
        # Atualiza a ação de cada sprite.
        all_sprites.update()
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        screen.blit(quadrado, [300, 100])
        all_sprites.draw(screen)
        
        for i in range(1, len(lista_bolinhas)):
            ba = lista_bolinhas[i - 1]
            bb = lista_bolinhas[i]
            
            xa = ba[1] * tam_bolinha + xinit
            ya = ba[0] * tam_bolinha + yinit
            
            xb = bb[1] * tam_bolinha + xinit
            yb = bb[0] * tam_bolinha + yinit
            
            for g in LISTA_CORES:
                if cor == 0:
                   cor_usada = VERMELHO
                elif cor == 1:
                    cor_usada = AMARELO
                elif cor == 2:
                    cor_usada = VERDE
                else:
                    cor_usada = AZUL
                    #teste
            
            pygame.draw.line(screen, cor_usada, (xa, ya), (xb, yb), 5)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()