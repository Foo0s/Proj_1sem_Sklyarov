import pygame

from pygame.sprite import Sprite


class SpaceShip(Sprite):
    '''Класс для управления кораблем.'''

    def __init__(self, ai_game):
        '''Инициализирует корабль и задает его начальную позицию.'''
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        '''Загружает изображение корабля и получает прямоугольник.'''
        self.image = pygame.image.load('images/spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (95, 95))  ## Изменение размера корабля
        self.rect = self.image.get_rect()

        '''Сохранение вещественной координаты центра корабля.'''
        self.x = float(self.rect.x)

        '''Флаг перемещения.'''
        self.moving_right = False
        self.moving_left = False

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom  ### Выравнивание позиции

    def update(self):
        '''Обновляет позицию корабля с учётом флага.'''
        # Обновляется атрибут x, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        '''Рисует корабль в текущей позиции.'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Размещение корабля в центре экрана..'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
