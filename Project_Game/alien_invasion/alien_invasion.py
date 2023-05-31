import sys
import pygame
from time import sleep


import settings
from settings import Settings
from ship import SpaceShip
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    '''Класс для управления ресурсами и поведением игры.'''

    def __init__(self):
        '''Инициализирует игру и создает игровые ресурсы.'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(self.settings.name_game)
        self.SpaceShip = SpaceShip(self)

        'Хранение игровой статистики..'
        self.stats = GameStats(self)
        self.sb_al = Scoreboard(self)

        '''Снаряды'''
        self.bullets = pygame.sprite.Group()  # Позиция снарядов будет обновляться при цикле while

        '''Иноземные корабли.'''
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        'Кнопка'
        self.play_button = Button(self, "PLAY")

    def run_game(self):
        '''Запуск основного цикла игры.'''
        while True:
            self._check_events()
            if self.stats.game_active:
                self.SpaceShip.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.bullets.update()

    def _check_events(self):
        '''Обрабатывает нажатия клавиш и события мыши.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check__keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        '''Реагирует на нажатие клавиш'''
        if event.key == pygame.K_RIGHT:
            self.SpaceShip.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.SpaceShip.moving_left = True
        elif event.key == pygame.K_q:
            f_number = open("max_number.txt", "w")
            f_number.write(str(self.stats.high_score))
            f_number.close()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.start_game()
        elif event.key == pygame.K_m:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check__keyup_events(self, event):
        '''Реагирует на отпускание клавиш.'''
        if event.key == pygame.K_RIGHT:
            self.SpaceShip.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.SpaceShip.moving_left = False

    def _check_play_button(self, mouse_p):
        ''' Запуск игры при нажатии на кнопку - "PLAY" '''
        button_clicked = self.play_button.rect_1.collidepoint(mouse_p)
        button_clicked_2 = self.play_button.rect_2.collidepoint(mouse_p)
        button_clicked_3 = self.play_button.rect_3.collidepoint(mouse_p)
        button_clicked_4 = self.play_button.rect_4.collidepoint(mouse_p)

        if button_clicked and not self.stats.game_active:
            # Сброс игровых настроек.
            self.settings.initialize_dynamic_settings()
            self.reset_param()
        elif button_clicked_2 and not self.stats.game_active:
            self.settings.increase_speed()
            self.reset_param()

        elif button_clicked_3 and not self.stats.game_active:
            self.settings.increase_speed()
            self.settings.increase_speed()
            self.reset_param()

        elif button_clicked_4 and not self.stats.game_active:
            self.settings.increase_speed()
            self.settings.increase_speed()
            self.settings.increase_speed()

            self.reset_param()

    def reset_param(self):
        # Сброс игровой статистики
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb_al.prep_score()
        self.sb_al.prep_ship()

        # Очистка списка пришельцев и bullet
        self.aliens.empty()
        self.bullets.empty()

        # Создание нового флота и размещение корабля в центре экрана
        self._create_fleet()
        self.SpaceShip.center_ship()

        # Уровень
        self.sb_al.prep_level()

        # Удаление(скрытие) указателя мыши
        pygame.mouse.set_visible(False)

    def start_game(self):
        if not self.stats.game_active:
            # Сброс игровой статистики
            self.stats.reset_stats()
            self.stats.game_active = True

            # Очистка списка пришельцев и bullet
            self.aliens.empty()
            self.bullets.empty()

            # Создание нового флота и размещение корабля в центре экрана
            self._create_fleet()
            self.SpaceShip.center_ship()

    def _fire_bullet(self):
        '''Создание нового снаряда и включение его в группу bullets.'''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''Обновляет позиции снарядов и уничтожает старые снаряды.'''
        # Обновление позиций снарядов.
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullets_aliens_convision()

    def _check_bullets_aliens_convision(self):
        # Проверка на попадание снарядов в пришельцев.
        # При обнаружении удаляет текст. пришельца.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb_al.prep_score()
            self.sb_al.check_high_score()
        if not self.aliens:
            # Создание нового флота.
            self.bullets.empty()  # Удаление снарядов
            self._create_fleet()
            self.settings.increase_speed()

            # Увеличение счета
            self.stats.level += 1
            self.sb_al.prep_level()

    def _create_fleet(self):
        '''Create флота вторжения'''
        # Создание пришельца.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        '''Определяет количество рядов помещающихся на экране.'''
        ship_height = self.SpaceShip.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        '''Создание флота вторжения.'''
        for row_number in range(number_rows):
            # Создание первого ряда пришельцев.
            for alien_number in range(number_aliens_x + 1):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        '''Созданиее пришельца и размещение его в ряду.'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте."""
        self._check_fleet_edges()
        self.aliens.update()
        # Проверка что корабль сталкивается с пришельцом.
        if pygame.sprite.spritecollideany(self.SpaceShip, self.aliens):
            self._ship_hit()

        # Проверка.Добрался ли объект до конца экрана.
        self.alien_check_screen()

    def _ship_hit(self):
        """Проверка на столкновение корабля с пришельцем.."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb_al.prep_ship()
            self.stats.reset_stats()
            self.sb_al.prep_score()

            # Очистка.
            self.aliens.empty()
            self.bullets.empty()

            # Создание нового флота и размещение корабля в центре экрана.
            self._create_fleet()
            self.SpaceShip.center_ship()

            # Pause
            sleep(0.7)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_edges(self):
        '''Реагириует на достижение пришельцем края экрана.'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def alien_check_screen(self):
        # Проверяет добрались ли пришельцы до нижнего края экрана.
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
                # Перезапуск.

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        '''Обновляет изображение на экране и отображает новый экран.'''
        # При каждом проходе цикла перерисовывается экран
        self.screen.fill(self.settings.bg_color)  ### Заполняем экран цветом
        self.SpaceShip.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb_al.show_score()
        # Отображение кнопки
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
