import pygame

# definir une classe qui va s'oquper des animation
class AnimateSprite(pygame.sprite.Sprite):
    
    # definir les choses a faire a la creation de l'entite
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'python/space_shooter/assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False
        
    # definir une methode pour de marrer l'animation
    def start_animation(self):
        self.animation = True
        
    # definir une methode pour animer le sprite
    def animate(self, loop=False):
        
        # verrifier si l'animation estb active
        if self.animation:
        
            # passer a limage suivante
            self.current_image += 1
            
            # verrifier si on atteit  la fin de lanimation
            if self.current_image >= len(self.images):
                # remettre l'animation au depart
                self.current_image = 0
                
                # verrifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False
                
            # modifier l'image presedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)
        
# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite dans le dossier correspandant
    images = []
    # recuper le chemin du dossier pour ce sprite
    path = f"python/space_shooter/assets/{sprite_name}/{sprite_name}"
    
    # boucler sur chaque image dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        
    # renvoyer le contenue de la liste
    return images


# definir un dictionnaire qui va contenire qui va contenir les images chargees de chaque sprite
# mummy -> [mmmy1.png, ...mummy2.png ...]
animations = {
    'mummy': load_animation_images('mummy'), 
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}