"""Module to represent a hero."""

import time

class Hero:
    """Represents a character piece."""

    def __init__(self, rpg_game):
        """Initialize attributes to represent a ches piece."""
        self.image = None
        self.name = ''
        self.color = ''
        self.speed = 2

        self.screen = rpg_game.screen

        self.movements = []
        self.movement_rate = 0
        self.tick_count = 0

        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0

    def move(self, action):
        if not self.movements:
            if action == 'up':
                self.movements = [{'y': self.y - i} for i in range(1,51,self.speed)]
            if action == 'down':
                self.movements = [{'y': self.y + i} for i in range(1,51,self.speed)]
            if action == 'right':
                self.movements = [{'x': self.x + i} for i in range(1,51,self.speed)]
            if action == 'left':
                self.movements = [{'x': self.x - i} for i in range(1,51,self.speed)]


    def animate(self):
        if self.movements:
            move = self.movements.pop(0)
            self.x = move.get('x') or self.x
            self.y = move.get('y') or self.y


    def blitme(self):
        """Draw the piece at its current location."""
        self.animate()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)




"""Module to represent a hero set, and individual heroes."""

from spritesheet import SpriteSheet

class HeroSet:
    """Represents a set of hero pieces.
    Each piece is an object of the Hero class.
    """

    def __init__(self, rpg_game):
        """Initialize attributes to represent the overall set of pieces."""

        self.rpg_game = rpg_game
        self.pieces = []
        self._load_pieces()

    def _load_pieces(self):
        """Builds the overall set:
        - Loads images from the sprite sheet.
        - Creates a Hero object, and sets appropriate attributes
          for that piece.
        - Adds each piece to the list self.pieces.
        """
        filename = '../assets/character and tileset/Dungeon_Character_2.png'
        piece_ss = SpriteSheet(filename)

        # Create a black king.
        b_king_rect = (0, 0, 100, 100)
        b_king_image = piece_ss.image_at(b_king_rect)

        b_king = Hero(self.rpg_game)
        b_king.image = b_king_image
        b_king.name = 'king'
        b_king.color = 'black'
        b_king.x = 100
        b_king.y = 200

        self.pieces.append(b_king)

        # Create a white king.
        w_king_rect = (110, 130, 80, 150)
        w_king_image = piece_ss.image_at(w_king_rect)

        w_king = Hero(self.rpg_game)
        w_king.image = w_king_image
        w_king.name = 'king'
        w_king.color = 'white'
        w_king.x = 500
        w_king.y = 600

        self.pieces.append(w_king)
