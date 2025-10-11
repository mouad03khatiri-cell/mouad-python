from comet import Comet
import pygame

# cree une classe pour gerer cet evenement
class CometFallEvent:
    
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False
        
        # definir un groupe de sprite pour stocker nos comets
        self.all_comets = pygame.sprite.Group()
        
    def add_percent(self):
        self.percent += self.percent_speed / 100
        
    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0
        
    def meteor_fall(self):
        # boucle pour les valeurs entre 1 20
        for i in range(1, 20):
            # apparaitre une 1 boule de feu
            self.all_comets.add(Comet(self))
    
    def attempt_fall(self):
        # la juge d'evenement est totalement   charge
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True
        
    def update_bar(self, surface):
        
        # ajouter du porcentage
        self.add_percent()
        
        # barre noire (arrière-plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 20,  # un peu au-dessus du bas de l'écran
            surface.get_width(),
            10
        ])
        # barre rouge (jauge d'évènement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 20,
            (surface.get_width() / 100) * self.percent,
            10
        ])