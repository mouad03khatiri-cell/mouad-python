
import pygame
import random
import animation

# Crée une classe qui va gérer la notion de monstre dans le jeu
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_animation()

    # Une seule valeur de vitesse
    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, speed)

    def damage(self, amount):
        # Infliger des dégâts
        self.health -= amount

        # Vérifier si le monstre est mort
        if self.health <= 0:
            # Réapparaître comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health

            # Ajouter des points au joueur
            self.game.add_score()

            # Si la barre d'événement est pleine
            if self.game.comet_event.is_full_loaded():
                # Retirer le monstre
                self.game.all_monsters.remove(self)

                # Déclencher la pluie de comètes
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # Dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60),
                         [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (85, 255, 0),
                         [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # Déplacement seulement si pas de collision avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            # Infliger des dégâts au joueur
            self.game.player.damage(self.attack)


class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)  # vitesse max 3


class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        
        # Vérifier si le monstre est mort
        if self.health <= 0:
            # Réapparaître comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            self.game.max_add_score()
