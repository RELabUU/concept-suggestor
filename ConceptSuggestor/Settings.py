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

        def _Setting(self, name):
            return self.data[name]

    instance = None

    def __init__(self):
        if not Settings.instance:
            Settings.instance = Settings.__Settings()
        else:
            pass

    def LoadSettings(self, file = SETTINGS_PATH):
        Settings.instance._LoadSettings()

    def _Setting(self, name):
        return Settings.instance._Setting(name)

    # Methods to directly get all the various settings instead of having to manually input the names.
    def Reload(self):
        return self._Setting("reload")
    def WordNetSimilarityMethod(self):
        return self._Setting("wordnetSimilarityMethod")
    def SpaCyWeight(self):
        return self._Setting("spacyWeight")
    def WordNetWeight(self):
        return self._Setting("wordnetWeight")
    def SimilarityThreshold(self):
        return self._Setting("similarityThreshold")
    def Alpha(self):
        return self._Setting("alpha")
    def Beta(self):
        return self._Setting("beta")
    def Gamma(self):
        return self._Setting("gamma")
    def Delta(self):
        return self._Setting("delta")
    def Epsilon(self):
        return self._Setting("epsilon")

    # Derived settings
    def UseSpacy(self):
        return self.SpaCyWeight() != 0
    def UseWordNet(self):
        return self.WordNetWeight() != 0
    def TotalSimilarityWeight(self):
        return self.SpaCyWeight() + self.WordNetWeight()