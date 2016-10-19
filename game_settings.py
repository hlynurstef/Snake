class Settings():
    """A class to store all settings for Snake."""

    def __init__(self):
        """Initialize game settings."""
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        self.width = 800
        self.height = 600
        self.caption = "Snake"

        self.fps = 15

        self.scale = 20
