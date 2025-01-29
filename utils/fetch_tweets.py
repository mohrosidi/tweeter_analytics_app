import requests
import pandas as pd
import time

# API Endpoint dan Header
API_URL = "https://twitter-api45.p.rapidapi.com/search.php"
HEADERS = {
    "x-rapidapi-key": "YOUR_RAPIDAPI_API",  # API Key sudah ditetapkan di header
    "x-rapidapi-host": "twitter-api45.p.rapidapi.com"
}

def fetch_tweets(query, num_tweets=100):
    """
    Mengambil tweet berdasarkan query dengan paginasi menggunakan next_cursor.

    Args:
        query (str): Kata kunci pencarian.
        num_tweets (int): Jumlah tweet yang ingin diambil.

    Returns:
        pd.DataFrame: DataFrame yang berisi tweet.
    """

    all_tweets = []
    next_cursor = None
    total_fetched = 0  

    while total_fetched < num_tweets:
        params = {"query": query, "search_type": "Top"}
        if next_cursor:
            params["cursor"] = next_cursor  

        try:
            response = requests.get(API_URL, headers=HEADERS, params=params)
            data = response.json()

            if "timeline" not in data:
                print("Tidak ada data timeline dalam response.")
                break

            tweets = data["timeline"]

            for tweet in tweets:
                if "tweet_id" in tweet:
                    all_tweets.append({
                        "tweet_id": tweet.get("tweet_id"),
                        "screen_name": tweet["screen_name"],
                        "created_at": tweet["created_at"],
                        "text": tweet["text"],
                        "favorites": tweet["favorites"],
                        "retweets": tweet["retweets"],
                        "replies": tweet["replies"],
                        "quotes": tweet["quotes"],
                        "views": tweet.get("views", "N/A"),
                    })

            total_fetched = len(all_tweets)
            print(f"✅ Berhasil mengambil {total_fetched} tweet...")

            next_cursor = data.get("next_cursor")
            if not next_cursor:
                print("🚀 Tidak ada lagi next_cursor, berhenti mengambil data.")
                break

            time.sleep(1)

        except Exception as e:
            print(f"❌ Error saat mengambil tweet: {e}")
            break

    return pd.DataFrame(all_tweets)
