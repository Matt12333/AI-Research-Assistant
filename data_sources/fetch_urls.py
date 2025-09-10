from . import mit_news_data, kdnuggests_data

def fetch_urls():
    '''
    Fetches the article URLs to be opened on startup
    '''
    
    urls = []
    
    # Fetch MIT article urls
    mit_urls = mit_news_data.fetch_mit_urls()

    # Advise if there were any urls fetched
    if len(mit_urls) == 0:
        print("No MIT articles today")
    else:
        print('MIT article URLs have been collected...')


    # Fetch KD Nuggets article urls
    kdnuggests_urls = kdnuggests_data.fetch_kdnuggets_urls()

    # Advise if there were any urls fetched
    if len(kdnuggests_urls) == 0:
        print("No KD Nuggets articles today")
    else:
        print('KD Nuggets article URLs have been collected...')


    # Combine urls
    urls = mit_urls + kdnuggests_urls
    

    # Check if any urls were collected
    if len(urls) == 0:
        print('No articles released yesterday')

    else:
        print('URL collection successful!')
        print('='*50)

    return urls
