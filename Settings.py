
class Settings:
    def __init__(self):
        self.settings = {
            "game_state": 0,
            "name": 'None',
            "score": 0,
            "sound": True,
            "direction": "up",
        }

    def get_setting(self, key):
        return self.settings.get(key)

    def set_setting(self, key, value):
        if key in self.settings:
            self.settings[key] = value
        else:
            raise KeyError(f"Setting '{key}' does not exist.")
    