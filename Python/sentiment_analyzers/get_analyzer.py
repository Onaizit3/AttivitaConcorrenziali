from sentiment_analyzers.vader_sentiment_analyzer import VaderSentimentAnalyzer
from sentiment_analyzers.transformer_sentiment_analyzer import TransformerSentimentAnalyzer



def get_analyzer(type_):
    if type_ == "vader":
        return VaderSentimentAnalyzer()
    elif type_ == "transformer":
        return TransformerSentimentAnalyzer()
    else:
        raise ValueError("Tipo non supportato")