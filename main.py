from game import Game
import pygame
import math
pygame.init()

# cree une clock
clock = pygame.time.Clock()
FPS = 200

pygame.display.set_caption("Shooter & Comet Fall game")
screen = pygame.display.set_mode((1080, 720))

# importer charger l'arriere plan de notre jeu
background = pygame.image.load('python/space_shooter/assets/bg.jpg')


# importer charger notre banniere
banner = pygame.image.load('python/space_shooter/assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer charger notre bouton pour lancer la partie
play_button = pygame.image.load('python/space_shooter/assets/button.png')
play_button = pygame.transform.scale(play_button,(400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# chareger notre jeu
game = Game()

running = True

# boucla tant que cette condition est vrai
while running:
    
    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))
    
    # verrifier si notre jeu a commence ou non
    if game.is_playing:
        # declancher les instruction de la partie
        game.update(screen)
    # verrifier si notre jeu n'a pas commence
    else:
        # ajouter mon ecran de vienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
    
    # mettre a jour l'ecran
    pygame.display.flip()
    
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermuture du jeu
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            # detecter si la touche espace est enclanche pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                
                
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verrifier si la souris est en collision avec le bouton "jouer"
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lance"
                game.start()
                # jouer le son
                game.sound_manager.play('click')
    clock.tick(FPS)
