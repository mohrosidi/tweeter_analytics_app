import openai

def generate_feedback(data, analysis_type, openai_api_key):
    """
    Menghasilkan feedback AI berdasarkan hasil analisis.

    Parameters:
        - data (dict): Data hasil analisis yang akan diberikan feedback
        - analysis_type (str): Jenis analisis (misalnya: "EDA", "Sentiment Analysis", "Topic Analysis")
        - openai_api_key (str): API Key OpenAI untuk pemrosesan

    Returns:
        - str: Feedback yang dihasilkan oleh AI
    """
    openai.api_key = openai_api_key

    prompt = f"Berikan feedback analitis tentang hasil {analysis_type} berikut:\n\n{data}"

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Anda adalah AI analis data yang membantu menganalisis hasil statistik."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error saat menghasilkan feedback: {str(e)}"
