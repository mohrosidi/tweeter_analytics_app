import openai

class SummaryAgent:
    def __init__(self, api_key):
        """Inisialisasi agent dengan API Key."""
        self.api_key = api_key
        self.client = openai.Client(api_key=self.api_key)  # Gunakan OpenAI Client

    def generate_summary(self, tweets_df, eda_summary, topic_summary, eda_feedback, sentiment_feedback, topic_feedback):
        """Membuat ringkasan AI berdasarkan hasil analisis tweet."""
        prompt = f"""
        Summarize the following Twitter data analysis:

        1. Exploratory Data Analysis (EDA):
        {eda_summary}
        Feedback: {eda_feedback}

        2. Sentiment Analysis:
        {sentiment_feedback}

        3. Topic Analysis:
        {topic_summary}
        Feedback: {topic_feedback}

        Provide an executive summary with actionable insights.
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",  # Gunakan model yang sudah ditentukan di config.py
            messages=[
                {"role": "system", "content": "Provide a detailed summary of Twitter data analysis."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content.strip(), "AI summary successfully generated."
