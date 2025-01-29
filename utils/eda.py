import pandas as pd

def perform_eda(df):
    """
    Melakukan Exploratory Data Analysis (EDA) pada dataset tweet.

    Args:
        df (pd.DataFrame): DataFrame berisi tweet.

    Returns:
        dict: Hasil EDA.
    """

    total_tweets = len(df)
    unique_users = df["screen_name"].nunique()
    total_likes = df["favorites"].sum()
    total_retweets = df["retweets"].sum()

    result = {
        "Total Tweets": total_tweets,
        "Total Unique Users": unique_users,
        "Total Likes": total_likes,
        "Total Retweets": total_retweets
    }

    return result
