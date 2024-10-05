import streamlit as st
import requests
import pandas as pd

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
st.title("Top Finance & Commerce News")

# Use your provided NewsAPI key
api_key = 'acf17eb315f244b6a11882a3ec298437'

# Refresh button
if st.button('Refresh News'):
    st.write("Fetching latest finance and commerce news...")
    news_df = fetch_finance_news(api_key)
else:
    st.write("Displaying cached finance and commerce news... Click 'Refresh News' for latest updates.")
    news_df = fetch_finance_news(api_key)

# Display the news in Streamlit
if not news_df.empty:
    for index, row in news_df.iterrows():
        st.write(f"**{row['Title']}**")
        st.write(f"[Read more]({row['Link']})")
        st.write("---")
else:
    st.write("No news available at the moment.")
