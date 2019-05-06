# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:07:57 2019

@author: dorad
"""

# Importando as bibliotecas necessárias.
import pygame
import random
from os import path
from pygame import rect

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
class DOTS(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem.
        ponto_azul = pygame.image.load(path.join(img_dir, "dot_azul.png")).convert()
        ponto_rosa = pygame.image.loud(path.join(img_dir, "dot_rosa.png")).convert()
        ponto_amarelo = pygame.image.loud(path.join(img_dir, "dot_amarelo.png")).convert()
        ponto_verde = pygame.image.loud(path.join(img_dir, "dot_verde.png")).convert()

        self.azul = ponto_azul
        self.rosa = ponto_rosa
        self.amarelo = ponto_amarelo
        self.verde = ponto_verde
        
        # Diminuindoo tamanho da imagem.
        self.azul = pygame.transform.scale(ponto_azul, (50, 50))
        self.rosa = pygame.transform.scale(ponto_rosa, (50, 50))
        self.amarelo = pygame.transform.scale(ponto_amarelo, (50, 50))
        self.verde = pygame.transform.scale(ponto_verde, (50, 50))
        
        # Deixando transparente.
        self.azul.set_colorkey(WHITE)
        self.rosa.set_colorkey(WHITE)
        self.amarelo.set_colorkey(WHITE)
        self.verde.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect_azul = self.azul.get_rect()
        self.rect_rosa = self.rosa.get_rect()
        self.rect_amarelo = self.amarelo.get_rect()
        self.rect_verde = self.verde.get_rect()
        
        # Posicionando.
        self.rect_azul.centerx = WIDTH / 4
        self.rect_azul.bottom = HEIGHT - 50
        
        self.rect_rosa.centerx = WIDTH /2
        self.rect_rosa.bottom = HEIGHT - 50
        
        self.rect_amarelo.centerx = WIDTH /9
        self.rect_amarelo.bottom = HEIGHT - 50
        
        self.rect_verde.centerx = WIDTH /6
        self.rect_verde.bottom = HEIGHT - 50
        
        # Velocidade do ponto
        self.speedx = 0
        

#Classe Mob que representa o meteoro
class Mob(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        ponto_azul = pygame.image.load(path.join(img_dir, "dot_amarelo.png")).convert()
        self.image = ponto_azul
        
        # Diminuindoo tamanho da imagem.
        self.image = pygame.transform.scale(ponto_azul, (50, 50))
        
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
player = DOTS()

# Cria o meteoro.
meteoro = Mob()

# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
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