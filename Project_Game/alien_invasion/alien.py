import pygame
from pygame.sprite import Sprite
import settings

class Alien(Sprite):
    '''Класс, который создает 1 пришельца.'''

    def __init__(self, ai_game):
        '''Инициализирует пришельца и назначение атрибута rect.'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load("images/pngwing.com (2).png")
        self.image = pygame.transform.scale(self.image, (87, 50))
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)

    def check_edges(self):
        '''Возвращает True, если пришелец находится у края экрана.'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    #Перемещение корабля-пришельца вправо...
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x