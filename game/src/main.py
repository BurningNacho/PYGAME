
import sys

import pygame

from settings import Settings
from hero_set import HeroSet




class AutoRPG:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and create resources."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()


        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("FIRST RPG")


        self.last_click = 0
        self.hero_set = HeroSet(self)


    def run_game(self):
        """Starts the main loop for the game."""
        while True:
            self.clock.tick(self.settings.refresh_rate)
            self._check_actions()
            self._check_events()
            self._update_screen()

    def _check_actions(self):
        """Handles Key press"""
        self.last_click += 1
        if self.last_click >= 50:
            self.last_click = 50

            if self.hero_set.pieces[0].x - self.hero_set.pieces[1].x > 50:
                self.hero_set.pieces[1].move('right')
            elif self.hero_set.pieces[0].x - self.hero_set.pieces[1].x < 50:
                self.hero_set.pieces[1].move('left')
            elif self.hero_set.pieces[0].y - self.hero_set.pieces[1].y < 50:
                self.hero_set.pieces[1].move('up')
            elif self.hero_set.pieces[0].y - self.hero_set.pieces[1].y > 50:
                self.hero_set.pieces[1].move('down')

            self.keys_pressed = pygame.key.get_pressed()
            if self.keys_pressed[pygame.K_UP]:
                self.hero_set.pieces[0].move('up')
            elif self.keys_pressed[pygame.K_RIGHT]:
                self.hero_set.pieces[0].move('right')
            elif self.keys_pressed[pygame.K_DOWN]:
                self.hero_set.pieces[0].move('down')
            elif self.keys_pressed[pygame.K_LEFT]:
                self.hero_set.pieces[0].move('left')



    def _update_screen(self):
        """Handles Display updates"""
        self.screen.fill(self.settings.bg_color)
        self.hero_set.pieces[0].blitme()
        self.hero_set.pieces[1].blitme()
        pygame.display.flip()
        # pygame.display.update()


    def _check_events(self):
        """Handles events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()




## Launch the game
if __name__ == '__main__':
    auto_rpg = AutoRPG()
    auto_rpg.run_game()
