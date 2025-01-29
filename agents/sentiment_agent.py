from utils.sentiment import analyze_sentiment

class SentimentAgent:
    def __init__(self, api_key):
        """Inisialisasi agent dengan API Key."""
        self.api_key = api_key  

    def analyze_sentiment(self, text):
        """Menganalisis sentimen dari teks menggunakan OpenAI."""
        return analyze_sentiment(text, self.api_key)
