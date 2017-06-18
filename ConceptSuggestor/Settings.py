import json

SETTINGS_PATH = "settings.json"

class Settings(object):
    """Singleton loading the settings and parameters from an external file."""

    class __Settings:
        def __init__(self):
            self._LoadSettings()

        def __str__(self):
            return repr(self) + self.val

        def _LoadSettings(self, file = SETTINGS_PATH):
            with open(file) as data_file:
                self.data = json.load(data_file)

        def Setting(self, name):
            return self.data(name)

    instance = None

    def __init__(self):
        if not Settings.instance:
            Settings.instance = Settings.__Settings()
        else:
            pass

    def LoadSettings(self, file = SETTINGS_PATH):
        Settings.instance._LoadSettings()

    def Setting(self, name):
        return Settings.instance.data[name]