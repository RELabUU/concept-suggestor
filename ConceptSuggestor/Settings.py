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
    @property
    def Reload(self):
        return self._Setting("reload")
    @property
    def WordNetSimilarityMethod(self):
        return self._Setting("wordnetSimilarityMethod")
    @property
    def UseSynonymity(self):
        return self._Setting("useSynonymity")
    @property
    def SpaCyWeight(self):
        return self._Setting("spacyWeight")
    @property
    def WordNetWeight(self):
        return self._Setting("wordnetWeight")
    @property
    def SimilarityThreshold(self):
        return self._Setting("similarityThreshold")
    @property
    def Alpha(self):
        return self._Setting("alpha")
    @property
    def Beta(self):
        return self._Setting("beta")
    @property
    def Gamma(self):
        return self._Setting("gamma")
    @property
    def Delta(self):
        return self._Setting("delta")
    @property
    def Epsilon(self):
        return self._Setting("epsilon")
    @property
    def MinLambda(self):
        return self._Setting("minLambda")
    @property
    def MaxLambda(self):
        return self._Setting("maxLambda")
    @property
    def LambdaInterval(self):
        return self._Setting("lambdaInterval")
    @property
    def LambdaPlusMu(self):
        return self._Setting("lambdaPlusMu")
    @property
    def MinGamma(self):
        return self._Setting("minGamma")
    @property
    def MaxGamma(self):
        return self._Setting("maxGamma")
    @property
    def GammaInterval(self):
        return self._Setting("gammaInterval")
    @property
    def GammaPlusDeltaPlusTwoEpsilon(self):
        return self._Setting("gammaPlusDeltaPlusTwoEpsilon")

    # Derived settings
    @property
    def UseSpacy(self):
        return self.SpaCyWeight != 0
    @property
    def UseWordNet(self):
        return self.WordNetWeight != 0
    @property
    def TotalSimilarityWeight(self):
        return self.SpaCyWeight + self.WordNetWeight