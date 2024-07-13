import pygame
from settings import *

class UI:
    def __init__(self):
        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # bar setup
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.stamina_bar_rect = pygame.Rect(10, 34, STAMINA_BAR_WIDTH, BAR_HEIGHT)
        self.exp_bar_rect = pygame.Rect(10, 58, EXP_BAR_WIDTH, BAR_HEIGHT)

    def show_bar(self, current_amount, max_amount, bg_rect, color):
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # convert stats
        ratio = current_amount / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # draw bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self, exp):
        text_surf = self.font.render(f'Score: {str(int(exp))}', False, 'white')
        x = SCREEN_WIDTH - 20
        y = SCREEN_HEIGHT - 20
        text_rect = text_surf.get_rect(bottomright = (x, y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(15, 15))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(15, 15), 3)

    def selection_box(self, left, top):
        bg_rect = pygame.Rect(left, top, ITEM_SIZE, ITEM_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

    def item_overlay(self, item_index):
        pass

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.stamina, player.stats['stamina'], self.stamina_bar_rect, STAMINA_COLOR)
        self.show_bar(player.exp, player.stats['exp'], self.exp_bar_rect, EXP_COLOR)

        self.show_exp(player.exp)
        self.selection_box(10, 650)