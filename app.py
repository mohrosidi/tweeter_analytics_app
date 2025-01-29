import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from agents.tweet_agent import TweetAgent
from agents.eda_agent import EDAAgent
from agents.sentiment_agent import SentimentAgent
from agents.topic_agent import TopicAgent
from utils.openai_feedback import generate_feedback  # Feedback AI tetap dari utils

# 📌 **Deskripsi Aplikasi**
st.set_page_config(page_title="Twitter Analytics App", layout="wide")
st.title("📊 Twitter Analytics App")

st.markdown(
    """
    **Twitter Analytics App** adalah aplikasi berbasis Streamlit yang memungkinkan pengguna untuk 
    **menganalisis tweet berdasarkan keyword atau hashtag**. Aplikasi ini menyediakan fitur:
    - 🚀 **Scraping Data Twitter** menggunakan API
    - 📊 **Exploratory Data Analysis (EDA)** termasuk visualisasi data
    - 😊 **Analisis Sentimen** (Positive, Negative, Neutral)
    - 🗣 **Deteksi Topik** berdasarkan pembicaraan dalam tweet
    - 🔍 **Feedback AI yang menganalisis data visualisasi**
    """
)

# Sidebar: Input API Key
st.sidebar.subheader("🔑 API Key")
openai_api_key = st.sidebar.text_input("Masukkan OpenAI API Key:", type="password")

# Sidebar: Input Pencarian Twitter
st.sidebar.subheader("🔍 Pencarian Twitter")
query = st.sidebar.text_input("Masukkan kata kunci atau hashtag:", "elon musk")
num_tweets = st.sidebar.slider("Jumlah Tweet", 50, 500, 100)

# Validasi API Key sebelum inisialisasi agent
if openai_api_key:
    tweet_agent = TweetAgent(api_key=openai_api_key)
    eda_agent = EDAAgent()
    sentiment_agent = SentimentAgent(api_key=openai_api_key)
    topic_agent = TopicAgent(api_key=openai_api_key)
else:
    st.sidebar.warning("⚠️ Masukkan OpenAI API Key untuk menggunakan fitur analisis!")

# Tombol untuk mengambil data
if st.sidebar.button("🚀 Ambil Data Twitter"):
    if not openai_api_key:
        st.error("⚠️ API Key diperlukan untuk mengambil data dan melakukan analisis!")
    else:
        with st.spinner("Mengambil tweet..."):
            tweets_df = tweet_agent.fetch_tweets(query, num_tweets)

            if not tweets_df.empty:
                st.success(f"✅ Berhasil mengambil {len(tweets_df)} tweet!")
                st.dataframe(tweets_df)

                ### 📊 **EDA Analysis & Data Visualization** ###
                st.subheader("📊 Exploratory Data Analysis (EDA) & Data Visualization")
                eda_result = eda_agent.perform_eda(tweets_df)
                for key, value in eda_result.items():
                    st.write(f"**{key}:** {value}")

                # 🔥 **Visualisasi Data**
                st.markdown("### 📈 Visualisasi Data")
                
                # 🎯 Bar Chart - Top KOL berdasarkan engagement
                tweets_df["total_engagement"] = (
                    tweets_df["favorites"] + tweets_df["retweets"] + 
                    tweets_df["replies"] + tweets_df["quotes"]
                )
                top_kol = tweets_df.groupby("screen_name")["total_engagement"].sum().sort_values(ascending=False).head(10)

                fig, ax = plt.subplots()
                top_kol.plot(kind="barh", ax=ax)
                ax.set_title("Top 10 KOL berdasarkan Engagement")
                ax.set_xlabel("Total Engagement")
                ax.set_ylabel("Username")
                st.pyplot(fig)

                # 📢 Bar Chart - Top Tweet berdasarkan Engagement
                top_tweets = tweets_df.sort_values(by="total_engagement", ascending=False).head(10)

                fig, ax = plt.subplots(figsize=(8, 5))
                ax.barh(top_tweets["text"].apply(lambda x: x[:50] + "..."), top_tweets["total_engagement"])
                ax.set_xlabel("Total Engagement")
                ax.set_ylabel("Tweet (Dipotong)")
                ax.set_title("Top 10 Tweet berdasarkan Engagement")
                st.pyplot(fig)

                # 📈 Line Chart - Tweet Over Time
                st.subheader("📈 Tweet Over Time")
                tweets_df["created_at"] = pd.to_datetime(tweets_df["created_at"])
                tweets_df["date"] = tweets_df["created_at"].dt.date
                tweet_over_time = tweets_df.groupby("date")["tweet_id"].count()

                fig, ax = plt.subplots(figsize=(8, 5))
                ax.plot(tweet_over_time.index, tweet_over_time.values, marker="o", linestyle="-")
                ax.set_xlabel("Tanggal")
                ax.set_ylabel("Jumlah Tweet")
                ax.set_title("Tren Jumlah Tweet Seiring Waktu")
                st.pyplot(fig)

                # **🔍 Feedback AI dengan Konteks dari Visualisasi**
                visualization_summary = {
                    "Top KOL": top_kol.to_dict(),
                    "Top Tweets": top_tweets[["text", "total_engagement"]].to_dict(orient="records"),
                    "Tweet Over Time": tweet_over_time.to_dict()
                }

                eda_feedback = generate_feedback(visualization_summary, "EDA & Data Visualization", openai_api_key)
                st.markdown("**🔍 AI Insight dari Visualisasi Data:**")
                st.info(eda_feedback)

                ### 😊 **Sentiment Analysis** ###
                st.subheader("😊 Sentiment Analysis")
                tweets_df["Sentiment"] = tweets_df["text"].apply(lambda x: sentiment_agent.analyze_sentiment(x))
                st.dataframe(tweets_df[["text", "Sentiment"]])

                # Generate AI feedback untuk Sentiment Analysis
                sentiment_feedback = generate_feedback(
                    tweets_df["Sentiment"].value_counts().to_dict(),
                    "Sentiment Analysis",
                    openai_api_key
                )
                st.markdown("**🔍 Feedback AI:**")
                st.info(sentiment_feedback)

                ### 🗣️ **Topic Analysis** ###
                st.subheader("🗣️ Topic Analysis")
                try:
                    topic_result = topic_agent.detect_topics(" ".join(tweets_df["text"]))

                    if "Topik yang ditemukan" in topic_result:
                        st.markdown("### 📌 Topik yang ditemukan")
                        st.write(topic_result["Topik yang ditemukan"])
                    else:
                        st.warning("⚠️ Tidak ada topik yang terdeteksi.")
                    
                    # Generate AI feedback untuk Topic Analysis
                    topic_feedback = generate_feedback(topic_result, "Topic Analysis", openai_api_key)
                    st.markdown("**🔍 Feedback AI:**")
                    st.info(topic_feedback)
                except Exception as e:
                    st.error(f"❌ Error saat mendeteksi topik: {e}")

            else:
                st.error("❌ Tidak ada tweet yang ditemukan!")
