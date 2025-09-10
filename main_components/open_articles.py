import webbrowser

def open_articles(urls):
    '''
    Open all the articles that have been fetch 
    or confirm that no articles were returned
    '''
    count = 0

    for url in urls:
        try:
            webbrowser.open_new(url)
            print("Window successfully opened!")
            count += 1
            
        except:
            print("Failed to open window...")
    
    print(f"{count} of {len(urls)} articles opened!")