from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

def fetch_mainpage_date():
    '''
    Fetch the mainpage data for the website
    '''

    url = 'https://www.kdnuggets.com/news/index.html'

    page = requests.get(url).text
        
    # Turn page data into a python object to navigate
    soup = BeautifulSoup(page, 'html.parser')
    
    # Fetch main page article information
    main_page_data = soup.find('td').ul
    
    # Fetch the article information
    articles = main_page_data.find_all(class_='li-has-thumb')

    return articles

def fetch_article_urls(articles):
    '''
    Fetch the article urls
    '''

    # Initialise the previous day's date
    yesterdays_date = (datetime.today()- timedelta(days=1)).strftime('%Y-%m-%d')
    
    # List of valid articles
    article_links = []
    
    # Fetch the articles posted from yesterday onwards
    for i in articles:
        article = i.find(class_='li-has-thumb__content')
    
        # Fetch article date
        author = article.find(class_='author-link').text
        date_line = author.split(' on')[-1]
        date_str = date_line.split('in')[0].strip()
        article_date = datetime.strptime(date_str, "%B %d, %Y").strftime('%Y-%m-%d')
    
        # Filter articles that were posted from yesterday onwards
        if article_date == yesterdays_date:
            
            # Fetch article url path
            article_url = i.find(class_='li-has-thumb__content').a['href']
        
            article_links.append(article_url)

    return article_links

def fetch_kdnuggets_urls():
    '''
    Fetch KD Nuggets article URLs from the previous day
    '''

    articles = fetch_mainpage_date()

    urls = fetch_article_urls(articles)

    return urls


def fetch_kdnuggets_articles():

    article_urls = fetch_kdnuggets_urls()

    articles = []
    allowed_tags = ["p", "h2", "h3", "h4", "ol", "strong", "a"]

    for url in article_urls:
        text = ""
        article_page = requests.get(url).text
        article_soup = BeautifulSoup(article_page, 'html.parser')
        article_content = article_soup.find('div', class_='single', id='content')

        for tag in article_content.find_all(allowed_tags):
            if tag.name == "ol":
                for li in tag:
                    text += li.get_text(strip=True)
            else:
                text += tag.text

        articles.append(text)

    return articles