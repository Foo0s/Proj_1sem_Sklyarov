class GameStats:
    def __init__(self, ai_sup_game):
        "Статистика..."
        self.settings = ai_sup_game.settings
        self.reset_stats()
        self.game_active = False
        open_file_number = open("I:/Манакова/Proj_1sem_Sklyarov/Project_Game/alien_invasion/max_number.txt", "r")
        a = open_file_number.read()
        self.high_score = int(a)

    def reset_stats(self):
        'Инициализация статистики..'
        self.ships_left = self.settings.ship_limit
        self.level = 1
        self.score = 0
