import os
from datetime import datetime, timedelta

from data_sources.mit_news_data import fetch_mit_articles
from data_sources.kdnuggests_data import fetch_kdnuggets_articles

def transfer_mit_articles(mit_articles, yesterdays_date, daily_folder_path, historical_folder_path):
    
    '''Transfer the mit articles into the 'article_data' file and return number of articles'''

    if len(mit_articles) > 0:
        for idx, article in enumerate(mit_articles, start=1):
            file_name = f"MIT_News_Article{idx}_{yesterdays_date}.txt"

            daily_file_path = os.path.join(daily_folder_path, file_name)
            historical_file_path = os.path.join(historical_folder_path, file_name)
        
            with open(daily_file_path, "w", encoding="utf-8") as f:
                f.write(article)

            with open(historical_file_path, "w", encoding="utf-8") as f:
                f.write(article)

        return len(mit_articles)
        
    else:
        return len(mit_articles)

def transfer_kdnuggets_articles(kdnuggets_articles, yesterdays_date, daily_folder_path, historical_folder_path):

    '''Transfer the  KD Nugget articles into the 'article_data' file and return number of articles'''

    if len(kdnuggets_articles) > 0:
        for idx, article in enumerate(kdnuggets_articles, start=1):
            file_name = f"KDNuggets_News_Article{idx}_{yesterdays_date}.txt"

            daily_file_path = os.path.join(daily_folder_path, file_name)
            historical_file_path = os.path.join(historical_folder_path, file_name)
        
            with open(daily_file_path, "w", encoding="utf-8") as f:
                f.write(article)

            with open(historical_file_path, "w", encoding="utf-8") as f:
                f.write(article)

        return len(kdnuggets_articles)
    
    else:
        return len(kdnuggets_articles)

def place_articles_in_data_folder():

    '''Call the functions to place the data into the article folder to be fed into the agent.'''

    yesterdays_date = (datetime.today()- timedelta(days=1)).strftime('%Y-%m-%d')

    daily_folder_path  = r'C:\Users\Matth\OneDrive\Desktop\Coding\Projects\startup_articles_learning\main_app\app\article_data\daily'
    historical_folder_path  = r'C:\Users\Matth\OneDrive\Desktop\Coding\Projects\startup_articles_learning\main_app\app\article_data\historical'

    # Fetch article data
    mit_articles = fetch_mit_articles()
    kdnuggets_articles = fetch_kdnuggets_articles()

    # Transfer article data to folder    
    mit_article_count = transfer_mit_articles(mit_articles, yesterdays_date, daily_folder_path, historical_folder_path)
    kdnuggets_article_count = transfer_kdnuggets_articles(kdnuggets_articles, yesterdays_date, daily_folder_path, historical_folder_path)

    # Return total number of articles count
    article_count = (mit_article_count + kdnuggets_article_count)
    
    print(f"Saved {article_count} articles!")




        


