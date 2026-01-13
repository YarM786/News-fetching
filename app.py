import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="News Fetching App",
    page_icon="📰",
    layout="wide"
)

# ---------------- API KEY ----------------
# Get a free key from https://newsapi.org
NEWS_API_KEY = "YOUR_NEWSAPI_KEY"

# ---------------- FUNCTION ----------------
def fetch_news(category, count):
    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"category={category}&language=en&pageSize={count}&apiKey={38758c61623c40e397d8a0671c25e91b}"
    )
    response = requests.get(url)
    data = response.json()

    if data.get("status") == "ok":
        return data.get("articles", [])
    return []

# ---------------- UI ----------------
st.title("📰 News Fetching Application")
st.write("Fetch **live news articles** by category using Streamlit.")

# Sidebar controls
st.sidebar.header("⚙️ Settings")
category = st.sidebar.selectbox(
    "Select News Category",
    ["business", "technology", "sports", "health", "science", "entertainment"]
)

article_count = st.sidebar.slider(
    "Number of Articles",
    min_value=1,
    max_value=10,
    value=5
)

# Fetch button
if st.sidebar.button("🔍 Fetch News"):
    articles = fetch_news(category, article_count)

    if not articles:
        st.warning("No news articles found.")
    else:
        for i, article in enumerate(articles, 1):
            st.markdown(f"## {i}. {article['title']}")
            st.write(article.get("description", "No description available."))

            if article.get("url"):
                st.markdown(f"[Read full article]({article['url']})")

            st.markdown("---")
else:
    st.info("Choose a category and click **Fetch News**.")
