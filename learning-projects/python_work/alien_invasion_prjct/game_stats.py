class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialise statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False
    
    def reset_stats(self):
        """Initialize stats that can change throughout the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
    
