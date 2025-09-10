from main_components import open_articles, transfer_article_data, agent, no_article_window, clear_previous_data
from data_sources.fetch_urls import fetch_urls



clear_previous_data.clear_previous_daily_data()


# Fetch article urls
#urls = fetch_urls()
urls = []

# Run window advising no news today
if len(urls) == 0:
    print("No articles were released yesterday...")
    no_article_window.no_article_window()

else:

    # Open the articles in browser windows
    print("Opening Articles in browser...")
    open_articles.open_articles(urls)
    print("="*50)

    # Transfer articles to 'article_data' folder to be fed into the model
    print("Saving articles into data folder...")
    transfer_article_data.place_articles_in_data_folder()
    print("="*50)

    # Run the Agent to query the articles
    print("Beginning agent initialisation...")
    agent.run_agent()