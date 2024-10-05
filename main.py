import streamlit as st
import requests
import pandas as pd

# Custom CSS for a modern, visually pleasing look
st.markdown("""
    <style>
    /* General body styling */
    body {
        background-color: #f4f4f9;
        font-family: 'Arial', sans-serif;
    }
    .main-header {
        font-size: 2.5rem;
        color: #2c3e50;
        font-family: 'Helvetica Neue', sans-serif;
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .news-card {
        background-color: #ffffff;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.3s ease;
    }
    .news-card:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .news-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1E90FF;
        margin-bottom: 10px;
    }
    .news-link {
        font-size: 1rem;
        color: #34495e;
        font-family: 'Verdana', sans-serif;
        text-decoration: none;
        font-weight: 500;
    }
    .news-link:hover {
        color: #1E90FF;
        text-decoration: underline;
    }
    .footer {
        text-align: center;
        font-size: 0.85rem;
        margin-top: 50px;
        color: #7f8c8d;
    }
    </style>
""", unsafe_allow_html=True)

# Function to fetch finance and commerce news using NewsAPI
def fetch_finance_news(api_key):
    url = f"https://newsapi.org/v2/top-headlines?category=business&apiKey={api_key}&language=en"
    response = requests.get(url)
    news_data = response.json()

    articles = news_data.get("articles", [])
    news_list = []
    
    for article in articles:
        title = article['title']
        link = article['url']
        news_list.append({'Title': title, 'Link': link})
    
    return pd.DataFrame(news_list)

# Streamlit app layout
st.markdown("<div class='main-header'>Top Finance & Commerce News</div>", unsafe_allow_html=True)

# Use your provided NewsAPI key
api_key = 'acf17eb315f244b6a11882a3ec298437'

# Refresh button
if st.button('Refresh News'):
    st.write("Fetching latest finance and commerce news...")
    news_df = fetch_finance_news(api_key)
else:
    news_df = fetch_finance_news(api_key)

# Display the news in cards with enhanced design
if not news_df.empty:
    for index, row in news_df.iterrows():
        st.markdown(f"""
        <div class="news-card">
            <div class="news-title">{row['Title']}</div>
            <a href="{row['Link']}" target="_blank" class="news-link">Read full article</a>
        </div>
        """, unsafe_allow_html=True)
else:
    st.write("No news available at the moment.")

# Footer
st.markdown("<div class='footer'>Powered by NewsAPI</div>", unsafe_allow_html=True)
