import streamlit as st
import requests

st.set_page_config(page_title="News Fetching App", page_icon="📰")

NEWS_API_KEY = "38758c61623c40e397d8a0671c25e91b"

def fetch_news(category, count):
    url = (
        "https://newsapi.org/v2/top-headlines?"
        f"country=us&category={category}&pageSize={count}&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    # SHOW RAW RESPONSE (DEBUG)
    st.write("🔍 API Response:", data)

    if data.get("status") != "ok":
        return []

    return data.get("articles", [])

st.title("📰 News Fetching Application")
st.write("Fetch live news articles by category using Streamlit.")

category = st.selectbox(
    "Select Category",
    ["business", "technology", "sports", "health", "science", "entertainment"]
)

count = st.slider("Number of articles", 1, 5, 3)

if st.button("Fetch News"):
    articles = fetch_news(category, count)

    if not articles:
        st.error("❌ No articles returned. Check API response above.")
    else:
        for i, article in enumerate(articles, 1):
            st.subheader(f"{i}. {article['title']}")
            st.write(article.get("description", "No description"))
            st.markdown("---")


