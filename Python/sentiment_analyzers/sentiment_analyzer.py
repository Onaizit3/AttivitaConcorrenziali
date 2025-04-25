from abc import ABC, abstractmethod


class SentimentAnalyzer(ABC):

    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def analyze(self, text):
        pass
        