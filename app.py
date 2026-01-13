def fetch_news(category, count):
    url = (
        "https://newsapi.org/v2/top-headlines?"
        f"country=us&category={category}&pageSize={count}&apiKey={38758c61623c40e397d8a0671c25e91b}"
    )

    response = requests.get(url)
    data = response.json()

    # DEBUG: show error if exists
    if data.get("status") != "ok":
        st.error(f"API Error: {data.get('message')}")
        return []

    return data.get("articles", [])

