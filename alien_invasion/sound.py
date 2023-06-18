import pygame
from os import path

class Sound():
    def __init__(self):
        self.sound_bullet = path.join(path.dirname("alien_invasion/sound/laser-blast-descend_gy7c5deo"))
        self.sound_crush_alien = path.join(path.dirname("alien_invasion/sound/crush.mp3"))
        
    

    def move_sound_bullet(self):
        self.sound_voice_bullet = pygame.mixer.Sound(path.join(self.sound_bullet, "laser-blast-descend_gy7c5deo.mp3"))
        self.sound_voice_bullet.play()
    
    def move_sound_crush_alien(self):
        self.sound_voice_crush = pygame.mixer.Sound(path.join(self.sound_crush_alien, "crush.mp3"))
        self.sound_voice_crush.play()