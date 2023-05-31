class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion'''

    def __init__(self):
        '''Инициализирует настройки игры.'''
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 200, 30)
        self.name_game = "Alien Invasion"
        self.alien_speed = 2.3
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево
        self.fleet_direction = 1

        # Настройка корабля
        self.ship_speed = 4.2
        self.ship_limit = 3

        # Св-ва и настройки снарядов
        self.bullet_speed = 1.7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (10, 32, 198)

        # Макс кол-во снарядов
        self.bullet_allowed = 4

        # Темп ускорения игры
        self.speed_game = 9.2
        self.initialize_dynamic_settings()

        # Темп роста poin_alien
        self.score_point = 4.8

    def initialize_dynamic_settings(self):
        '''Инициализирует настройки, изменяющиеся в ходе игры.'''
        self.ship_speed_factor = 1.7
        self.bullet_speed_factor = 3.2
        self.alien_speed_factor = 9.2

        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 23

        # Рекорд игрока
        self.high_score = 0

    def increase_speed(self):
        '''Увеличивает настройки скорости.'''
        self.ship_speed_factor *= self.speed_game
        self.bullet_speed_factor *= self.speed_game
        self.alien_speed_factor *= self.speed_game

        # Увеличение point's
        self.alien_points = int(self.alien_points * self.score_point)
