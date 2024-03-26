class GameStats:
    """track stats"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # high score should never be reset
        self.high_score = 0

        # start alien invasion in an active state
        self.game_active = False

    def reset_stats(self):
        """initialize stats that can change during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
