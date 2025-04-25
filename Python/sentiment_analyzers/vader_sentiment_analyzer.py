from .sentiment_analyzer import SentimentAnalyzer

class VaderSentimentAnalyzer(SentimentAnalyzer):

    def __init__(self):
        super().__init__()

    def load_model(self):
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        self.model = SentimentIntensityAnalyzer()

    def analyze(self, text):
        result = self.model.polarity_scores(text)['compound']
        return result