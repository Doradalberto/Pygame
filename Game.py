# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:27:41 2019

@author: dorad
"""

# Importando as bibliotecas necessárias.
import pygame
import random
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'Imagens')

# Dados gerais do jogo.
WIDTH = 1400 # Largura da tela
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
background_rect = background.get_rect()

# Cria uma nave.  construtor será chamado automaticamente.
player = Player()

#cria dot rosa
rosa = Rosa()

#Cria DOT verde
verde = Verde()

#Cria DOT amarelo
amarelo = Amarelo()

# Cria o meteoro.
meteoro = Mob()

# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(rosa)
all_sprites.add(verde)
all_sprites.add(amarelo)
all_sprites.add(meteoro)

# Cria um gruppo Mobs e Adiciona o meteoro.
mobs = pygame.sprite.Group()
mobs.add(meteoro)

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
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
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()