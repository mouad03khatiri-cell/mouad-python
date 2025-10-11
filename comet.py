import random
import pygame

# cree une classe pour gerer cette comet
class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        # definir l'image associe a cette cometes
        self.image = pygame.image.load("python/space_shooter/assets/comet.png")
        self.image = pygame.transform.scale(self.image, (127, 127))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(5, 10)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event
        
    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')
        
        # verrifier si le nombre de comet est de 0
        if len(self.comet_event.all_comets) == 0:
            # remettre la barre a 0
            self.comet_event.reset_percent()
            # aparraitre les 2 premier monstre
            self.comet_event.game.start()
        
    def fall(self):
        self.rect.y += self.velocity
        
        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            # retirer la boule de feu
            self.remove()
            
            # si il n'ya plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                # remettre la jauge au de part
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
            
        # verrifier si la boule de feu touche le joueur
        
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            # retirer la boule de feu
            self.remove()
            self.comet_event.game.player.damage(20)