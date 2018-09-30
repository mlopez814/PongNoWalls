import pygame.font


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class Scoreboard:

    def __init__(self, ai_settings, screen, stats, ball):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.ball = ball

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.player_score()
        self.computer_score()
        self.score_indicator()

        self.win_str_player = "You Win!!!"
        self.lose_str_player = "You Lose!!!"

    # noinspection PyAttributeOutsideInit
    def player_score(self):
        score_str_player = "{:,}".format(self.stats.player_score)
        self.player_score_image = self.font.render(score_str_player, True, self.text_color)
        self.player_score_rect = self.player_score_image.get_rect()
        self.player_score_rect.right = self.screen_rect.right - 20
        self.player_score_rect.top = 10

    def computer_score(self):
        score_str_comp = "{:,}".format(self.stats.comp_score)
        self.comp_score_image = self.font.render(score_str_comp, True, self.text_color)
        self.comp_score_rect = self.comp_score_image.get_rect()
        self.comp_score_rect.left = self.screen_rect.left + 20
        self.comp_score_rect.top = 10

    def score_indicator(self):
        score_str_ind = "First to 7 wins"
        self.ind_score_image = self.font.render(score_str_ind, True, self.text_color)
        self.ind_score_rect = self.comp_score_image.get_rect()
        self.ind_score_rect.centerx = self.screen_rect.centerx - 100
        self.ind_score_rect.top = 10

    def check_winner(self):
        winning_score = self.ai_settings.score_limit
        if self.stats.player_score >= winning_score:
            return True
        elif self.stats.comp_score >= winning_score:
            return True
        else:
            return False

    def show_score(self):
        self.screen.blit(self.player_score_image, self.player_score_rect)
        self.screen.blit(self.comp_score_image, self.comp_score_rect)
        self.screen.blit(self.ind_score_image, self.ind_score_rect)

    def show_winner(self):
        winning_score = self.ai_settings.score_limit

        if self.stats.player_score == winning_score:
            self.player_win_image = self.font.render(self.win_str_player, True, self.text_color,
                                                     self.ai_settings.bg_color)
            self.player_win_rect = self.player_win_image.get_rect()
            self.player_win_rect.centerx = self.screen_rect.centerx
            self.player_win_rect.centery = self.screen_rect.centery - 100
            self.screen.blit(self.player_win_image, self.player_win_rect)

        elif self.stats.comp_score == winning_score:
            self.player_lose_image = self.font.render(self.lose_str_player, True, self.text_color,
                                                      self.ai_settings.bg_color)
            self.player_lose_rect = self.player_lose_image.get_rect()
            self.player_lose_rect.centerx = self.screen_rect.centerx
            self.player_lose_rect.centery = self.screen_rect.centery - 100
            self.screen.blit(self.player_lose_image, self.player_lose_rect)
