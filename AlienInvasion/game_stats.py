class GameStats:
    '''Track statistics for ALien Invasion '''

    def __init__(self, ai_game):
        '''Initialize statistics'''
        self.settings = ai_game.settings
        self.reset_stats()
        # Start alien invasion in inactive state
        self.game_active = False

    def reset_stats(self):
        '''Initialize sattistics that can change during the game'''
        self.ships_left = self.settings.ship_limit
