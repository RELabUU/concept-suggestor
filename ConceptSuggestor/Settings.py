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

            # Set the variables to the values found in the JSON file.
            self.reload = self._Setting("reload")
            self.wordnetSimilarityMethod = self._Setting("wordnetSimilarityMethod")
            self.useSynonymity = self._Setting("useSynonymity")
            self.spacyWeight = self._Setting("spacyWeight")
            self.wordnetWeight = self._Setting("wordnetWeight")
            self.similarityThreshold = self._Setting("similarityThreshold")
            self.alpha = self._Setting("alpha")
            self.beta = self._Setting("beta")
            self.gamma = self._Setting("gamma")
            self.delta = self._Setting("delta")
            self.epsilon = self._Setting("epsilon")
            self.minLambda = self._Setting("minLambda")
            self.maxLambda = self._Setting("maxLambda")
            self.lambdaSteps = self._Setting("lambdaSteps")
            self.lambdaPlusMu = self._Setting("lambdaPlusMu")
            self.minGamma = self._Setting("minGamma")
            self.maxGamma = self._Setting("maxGamma")
            self.gammaSteps = self._Setting("gammaSteps")
            self.gammaPlusDeltaPlusTwoEpsilon = self._Setting("gammaPlusDeltaPlusTwoEpsilon")

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

    # Methods to directly get and set all the various settings.
    @property
    def Reload(self):
        return Settings.instance.reload
    @Reload.setter
    def Reload(self, value):
        Settings.instance.reload = value

    @property
    def WordNetSimilarityMethod(self):
        return Settings.instance.wordnetSimilarityMethod
    @WordNetSimilarityMethod.setter
    def WordNetSimilarityMethod(self, value):
        Settings.instance.wordnetSimilarityMethod = value

    @property
    def UseSynonymity(self):
        return Settings.instance.useSynonymity
    @UseSynonymity.setter
    def UseSynonymity(self, value):
        Settings.instance.useSynonymity = value

    @property
    def SpaCyWeight(self):
        return Settings.instance.spacyWeight
    @SpaCyWeight.setter
    def SpaCyWeight(self, value):
        Settings.instance.spacyWeight = value

    @property
    def WordNetWeight(self):
        return Settings.instance.wordnetWeight
    @WordNetWeight.setter
    def WordNetWeight(self, value):
        Settings.instance.wordnetWeight = value

    @property
    def SimilarityThreshold(self):
        return Settings.instance.similarityThreshold
    @SimilarityThreshold.setter
    def SimilarityThreshold(self, value):
        Settings.instance.similarityThreshold = value

    @property
    def Alpha(self):
        return Settings.instance.alpha
    @Alpha.setter
    def Alpha(self, value):
        Settings.instance.alpha = value

    @property
    def Beta(self):
        return Settings.instance.beta
    @Beta.setter
    def Beta(self, value):
        Settings.instance.beta = value

    @property
    def Gamma(self):
        return Settings.instance.gamma
    @Gamma.setter
    def Gamma(self, value):
        Settings.instance.gamma = value

    @property
    def Delta(self):
        return Settings.instance.delta
    @Delta.setter
    def Delta(self, value):
        Settings.instance.delta = value

    @property
    def Epsilon(self):
        return Settings.instance.epsilon
    @Epsilon.setter
    def Epsilon(self, value):
        Settings.instance.epsilon = value

    @property
    def MinLambda(self):
        return Settings.instance.minLambda
    @MinLambda.setter
    def MinLambda(self, value):
        Settings.instance.minLambda = value

    @property
    def MaxLambda(self):
        return Settings.instance.maxLambda
    @MaxLambda.setter
    def MaxLambda(self, value):
        Settings.instance.maxLambda = value

    @property
    def LambdaSteps(self):
        return Settings.instance.lambdaSteps
    @LambdaSteps.setter
    def LambdaSteps(self, value):
        Settings.instance.lambdaSteps = value

    @property
    def LambdaPlusMu(self):
        return Settings.instance.lambdaPlusMu
    @LambdaPlusMu.setter
    def LambdaPlusMu(self, value):
        Settings.instance.lambdaPlusMu = value

    @property
    def MinGamma(self):
        return Settings.instance.minGamma
    @MinGamma.setter
    def MinGamma(self, value):
        Settings.instance.minGamma = value

    @property
    def MaxGamma(self):
        return Settings.instance.maxGamma
    @MaxGamma.setter
    def MaxGamma(self, value):
        Settings.instance.maxGamma = value

    @property
    def GammaSteps(self):
        return Settings.instance.gammaSteps
    @GammaSteps.setter
    def GammaSteps(self, value):
        Settings.instance.gammaSteps = value

    @property
    def GammaPlusDeltaPlusTwoEpsilon(self):
        return Settings.instance.gammaPlusDeltaPlusTwoEpsilon
    @GammaPlusDeltaPlusTwoEpsilon.setter
    def GammaPlusDeltaPlusTwoEpsilon(self, value):
        Settings.instance.gammaPlusDeltaPlusTwoEpsilon = value

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