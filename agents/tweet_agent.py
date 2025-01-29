from utils.fetch_tweets import fetch_tweets

class TweetAgent:
    def __init__(self, api_key=None):
        """Inisialisasi agent dengan API Key (opsional)."""
        self.api_key = api_key  

    def fetch_tweets(self, query, count):
        """Mengambil tweet berdasarkan query."""
        return fetch_tweets(query, count)
