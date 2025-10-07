from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager
import pygame


# cree une seconde classe qui va gerer notre jeu
class Game:
    
    def __init__(self):
        # definir si notre jeu a commence ou non
        self.is_playing = False
        # charger le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # generer le son
        self.sound_manager = SoundManager()
        self.font = pygame.font.Font("python/space_shooter/assets/fonts/OakSans-Regular.ttf", 25)
        self.pressed = {}
        self.score = 0
        self.beste_score = self.score
        self.font_beste = pygame.font.Font("python/space_shooter/assets/fonts/OakSans-Regular.ttf")
        
    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        # remettre le score a 0
        self.score = 0
        
    # def add_score(self, point=1):
    #     self.score += point
        
    def add_score(self):
        self.score += 1
    
    def max_add_score(self):
        self.score += 4
        
    def game_over(self):
        # remettre le jeu a neuf, retirer les monstre , remettre le joueur a  de vie, remettre le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.sound_manager.play('game_over')
    def update(self, screen):
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)
        
        # actualiset la barre de vie du joueur
        self.player.update_health_bar(screen)
        
        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)
        
        # actualiser l'animation du joueur
        self.player.update_animtion()

        # recuperer les projectile du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstre de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
            
        # recuperer les cometes de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()
        
        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)
        
        # appliquer l'ensemble des images  de mon groupe de cometes
        self.comet_event.all_comets.draw(screen)
        
        # verrifier si le joueur shouhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x:
            self.player.move_left()
        elif self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
