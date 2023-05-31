import pygame.font

from pygame.sprite import Group
from ship import SpaceShip


class Scoreboard():
    '''Класс для вывода игровой информации'''

    def __init__(self, a_g):
        '''Инициализирует атрибуты подсчета очков'''
        self.a_g = a_g
        self.screen = a_g.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = a_g.settings
        self.stats = a_g.stats

        # Настройка шрифта для вывода счета
        self.text_color = (20, 10, 213)
        self.font = pygame.font.SysFont(None, 48)

        # Подготовка исходного изображения
        self.prep_score()
        self.prep_score_high()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        '''Преобразует счет в графическое представление'''
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_score_high(self):
        '''Вывод рекордного счета игрока'''
        high_score = round(self.stats.high_score, -1)
        score_str_user = "{:,}".format(high_score)
        self.score_image_max = self.font.render(score_str_user, True, self.text_color, self.settings.bg_color)

        # Вывод счета посередине экрана
        self.score_rect_user = self.score_image_max.get_rect()
        self.score_rect_user.centerx = self.screen_rect.centerx
        self.score_rect_user.top = self.score_rect.top

    def check_high_score(self):
        '''Обновление рекорда.'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_score_high()

    def prep_level(self):
        '''Вывод текущего уровня.'''
        level_str = str(self.stats.level)
        self.score_image_level = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Вывод счета в левом верхнем углу
        self.level_rect = self.score_image_level.get_rect()
        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.top = 20

    def prep_ship(self):
        '''Сообщает об оставшихся кораблях'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = SpaceShip(self.a_g)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 50
            self.ships.add(ship)

    def show_score(self):
        '''Вывод счета на экран'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score_image_max, self.score_rect_user)
        self.screen.blit(self.score_image_level, self.level_rect)
        self.ships.draw(self.screen)


