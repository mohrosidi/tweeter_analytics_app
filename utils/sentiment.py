import openai

def analyze_sentiment(text, api_key):
    """
    Menganalisis sentimen dari teks menggunakan OpenAI GPT.

    Parameters:
        text (str): Teks yang akan dianalisis.
        api_key (str): OpenAI API Key.

    Returns:
        str: Label sentimen (Positive, Negative, Neutral).
    """
    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Anda adalah AI yang melakukan analisis sentimen."},
            {"role": "user", "content": f"Tentukan sentimen dari teks ini:\n\n{text}"}
        ],
        temperature=0.5
    )

    sentiment = response.choices[0].message.content.strip().lower()
    
    if "positive" in sentiment:
        return "Positive"
    elif "negative" in sentiment:
        return "Negative"
    else:
        return "Neutral"
