from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

def mit_webpage_information(url:str, site_domain:str):
    '''
    This function fetches the main webpage information and 
    returns the article overviews 
    '''
    
    # Fetch page data and turn it to a string
    page = requests.get(url).text
    
    # Turn page data into a python object to navigate
    soup = BeautifulSoup(page, 'html.parser')
    
    # Fetch the article information
    articles = soup.find_all(class_='page-term--views--list-item')

    return articles

def mit_filter_articles(site_domain:str, articles):
    '''
    This function returns the urls of the articles posted from 
    yesterday onwards
    '''
    
    # Initialise the previous day's date
    yesterdays_date = (datetime.today()- timedelta(days=1)).strftime('%Y-%m-%d')

    # List of valid articles
    article_links = []
    
    # Fetch the articles posted from yesterday onwards
    for i in articles:
        # Fetch article date
        article_date = i.find(class_='term-page--news-article--item--publication-date').time['datetime'][:10]

        # Filter articles that were posted from yesterday onwards
        if article_date == yesterdays_date:
            
            # Fetch article url path
            article_path = i.find(class_='term-page--news-article--item--title--link')['href']
        
            # Create working article link
            article_url = site_domain + article_path
            article_links.append(article_url)

    return article_links

def fetch_articles(article_urls:list):
    # Empty list to store articles
    articles = []

    # For each article url
    for article_url in article_urls:

        # Empty string object to store article
        text = ''
        
        # Fetch the article page data
        article_page = requests.get(article_url).text
    
        # Create a parsable object
        article_soup = BeautifulSoup(article_page, 'html.parser')
    
        # Fetch the article data
        article_data = article_soup.find(class_='paragraph paragraph--type--content-block-text paragraph--view-mode--default')
    
        for paragraph in article_data.find_all('p'):
            text += (paragraph.text)
    
        articles.append(text)
    
    return articles

def fetch_mit_articles():

    site_domain = 'https://news.mit.edu'
    urls = ['https://news.mit.edu/topic/artificial-intelligence2?page=0',
           'https://news.mit.edu/topic/machine-learning']

    all_article_urls = []
    
    for url in urls:
        # Fetch main page data
        articles = mit_webpage_information(url, site_domain)

        # Fetch in-date article urls
        article_urls = mit_filter_articles(site_domain, articles)

        # Filter for the unique articles
        all_article_urls.extend(article_urls)
    unique_article_urls = list(set(all_article_urls))
        
    # Fetch article data
    article_data = fetch_articles(unique_article_urls)

    return article_data

def fetch_mit_urls():

    site_domain = 'https://news.mit.edu'
    urls = ['https://news.mit.edu/topic/artificial-intelligence2?page=0',
           'https://news.mit.edu/topic/machine-learning']

    all_article_urls = []
    
    for url in urls:
        # Fetch main page data
        articles = mit_webpage_information(url, site_domain)

        # Fetch in-date article urls
        article_urls = mit_filter_articles(site_domain, articles)

        # Filter for the unique articles
        all_article_urls.extend(article_urls)
    unique_article_urls = list(set(all_article_urls))

    return unique_article_urls


