
from .sentiment_analyzer import SentimentAnalyzer

# TODO: Testare che keras e Pythorch pesano un casino 
class TransformerSentimentAnalyzer(SentimentAnalyzer):
    def __init__(self, model_name="MilaNLProc/feel-it-italian-sentiment"):
        self.model_name = model_name
        
    def load_model(self, model_name=None):
        from transformers import pipeline
        if model_name:
            self.model_name = model_name
        self.model = pipeline("sentiment-analysis", model=self.model_name)

    def analyze(self, text):
        results = self.model(text)
        positive_score = None
        for result in results:
            if result['label'] == 'POSITIVE':
                positive_score = result['score']
                break
        return positive_score