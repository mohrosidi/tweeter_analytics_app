import openai

def detect_topics(text, api_key):
    """
    Mendeteksi topik dari teks menggunakan OpenAI GPT.

    Parameters:
        text (str): Teks yang akan dianalisis.
        api_key (str): OpenAI API Key.

    Returns:
        dict: Ringkasan topik yang ditemukan.
    """
    client = openai.OpenAI(api_key=api_key)  # ✅ Gunakan client baru OpenAI API

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Anda adalah AI yang melakukan analisis topik dari kumpulan teks."},
            {"role": "user", "content": f"Deteksi topik utama dalam teks ini:\n\n{text}"}
        ],
        temperature=0.5
    )

    topics = response.choices[0].message.content.strip()
    return {"Topik yang ditemukan": topics}
