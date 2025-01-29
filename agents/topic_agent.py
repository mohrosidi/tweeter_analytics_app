from utils.topic import detect_topics

class TopicAgent:
    def __init__(self, api_key):
        """Inisialisasi agent dengan API Key."""
        self.api_key = api_key  

    def detect_topics(self, text):
        """Menganalisis topik dalam kumpulan tweet."""
        return detect_topics(text, self.api_key)
