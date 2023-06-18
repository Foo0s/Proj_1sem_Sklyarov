'''Создание кнопок'''
import pygame.font


class Button():
    def __init__(self, ai_gm, msg):
        '''Инициализирует атрибуты кнопки.'''
        self.screen = ai_gm.screen
        self.screen_rect = self.screen.get_rect()

        # Св-ва кнопки.
        self.width_1, self.height_1 = 150, 70
        self.width_2, self.height_2 = 150, 70
        self.width_3, self.height_3 = 150, 70
        self.width_4, self.height_4 = 150, 70

        self.button_color_1 = (70, 50, 250)
        self.button_color_2 = (250, 250, 250)
        self.button_color_3 = (250, 250, 250)
        self.button_color_4 = (250, 250, 250)

        self.text_color_1 = (0, 0, 0)
        self.text_color_2 = (0, 0, 0)
        self.text_color_3 = (0, 0, 0)
        self.text_color_4 = (0, 0, 0)

        self.font_1 = pygame.font.SysFont(None, 30)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect_1 = pygame.Rect(0, 0, self.width_1, self.height_1)
        self.rect_2 = pygame.Rect(0, 0, self.width_2, self.height_2)
        self.rect_3 = pygame.Rect(0, 0, self.width_3, self.height_3)
        self.rect_4 = pygame.Rect(0, 0, self.width_4, self.height_4)

        self.rect_1.center = self.screen_rect.center
        self.rect_2.center = (600, 505)
        self.rect_3.center = (600, 605)
        self.rect_4.center = (600, 710)

        # Передача сообщения - 1 раз.
        self.us_message(msg)

    def us_message(self, mess):
        '''Выравнивание текста по прямоугольнику, размещение.'''
        self.mess_image = self.font_1.render(mess, True, self.text_color_1, self.button_color_1)
        self.mess_image_rect = self.mess_image.get_rect()
        self.mess_image_rect.center = self.rect_1.center

        self.mess_image_2 = self.font_1.render("Легкая", True, self.text_color_2,
                                               self.button_color_2)
        self.mess_image_rect_2 = self.mess_image_2.get_rect()
        self.mess_image_rect_2.center = self.rect_2.center

        self.mess_image_3 = self.font_1.render("Средняя", True, self.text_color_3, self.button_color_3)
        self.mess_image_rect_3 = self.mess_image_3.get_rect()
        self.mess_image_rect_3.center = self.rect_3.center

        self.mess_image_4 = self.font_1.render("Тяжелая", True, self.text_color_4, self.button_color_4)
        self.mess_image_rect_4 = self.mess_image_4.get_rect()
        self.mess_image_rect_4.center = self.rect_4.center

    def draw_button(self):
        '''Отображает кнопку на экране'''
        pygame.draw.rect(self.screen, self.button_color_1, self.rect_1, border_radius=24)
        self.screen.blit(self.mess_image, self.mess_image_rect)

        pygame.draw.rect(self.screen, self.button_color_2, self.rect_2, border_radius=24)
        self.screen.blit(self.mess_image_2, self.mess_image_rect_2)

        pygame.draw.rect(self.screen, self.button_color_3, self.rect_3, border_radius=24)
        self.screen.blit(self.mess_image_3, self.mess_image_rect_3)

        pygame.draw.rect(self.screen, self.button_color_4, self.rect_4, border_radius=24)
        self.screen.blit(self.mess_image_4, self.mess_image_rect_4)

