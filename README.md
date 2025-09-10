# AI-Research-Assistant  
  
## Overview
I created an AI Agent to act as a Research Assistant.  

In an effort to continuously learn about the data science space, I wanted to have the latest updates in the world of data science to automatically be opened on my computer to read about.  
Not only that, but some terms in articles you may not understand, this is where I came up with the idea to create a personal research AI assistant.  

The idea is that:  
- Each morning articles about the latest developments in the field would open in my browser
- These article would be input into an LLM so that it could only query the articles
- I would read the articles and if I had any questions about the articles, I could query the LLM

To complete this project, I used the LLamaIndex Query Engine. A Query Engine is an LLM that will only query data that is provided to the database it is connected to and will not query its own knowledge base.  
  
This means if you put an article about AI into its database, it would return information from within the article based on the question you ask it but if you asked it a generic questions such as "What is the capital of England?", it wouldn't be able to answer this question unless this information was provided to its database.

## The Pipeline
  
One of the great things about this project is the mixture of skills that I was able to use, as I leaned on Data Engineering skills by creating an ETL pipeline.  

The pipeline consisted of three steps:  
1) Webscrape the article data
2) Clean the data and save it to a text file
3) Load the data into a vector database to be queried by the AI Agent

#### Data Sources  

I currently have two datasources that I fetch the articles from: MIT News and KD Nuggets.  
I found that MIT News has the latest groundbreaking information being released and KD Nuggets releases articles that help reinforce my knowledge.  

## The Process  

Now that we understand how the data is collected, I can explain how the entire process works:  
1) Upon logging on to my computer, a batch file will begin to run
2) The AI Agent's database and the articles from the previous day, in the 'daily' folder will be cleared
3) The articles are webscraped from online
4) The text files containing each article are transferred to a daily and historical data folder  
5) The articles will be opened in a browser
6) The AI Agent will begin to run, loading the new articles into its database
7) The Agent will be ready for use and can be queried in command prompt

## The Process Explained  

**1) Upon logging on to my computer, a batch file will begin to run**  

As the LLM is run locally using Ollama, I found it best to run the model in command prompt. Due to this, to have the application opened on startup, I added it to task scheduler, where it would begin once I logged into my account.  

**2) The AI Agent's database and the articles from the previous day, in the 'daily' folder will be cleared**  

This is an important step, as I found if you don't clear out the AI Agent's database each day then when you ask it a question it may reference the incorrect article that was posted before the previous day, therefore, I created 'daily' and 'historical' data folders.  
- The 'daily' data folder is cleared each day so no duplicate data is fed into the AI Agent's database and so the AI Agent will only reference the data from the articles from the previous day.  
- The 'historical' data folder is provided with all the articles from each day to keep a record for any future uses I may have for the articles.

**3) The articles are webscraped from online**  

The ETL pipeline that webscrapes the article data from online is ran and returns the articles as text files.  

However, if there are no article urls returned from the webscraping, there will be a small window that pops up saying "No articles today", advising me that no articles were posted yesterday.  

**4) The text files containing each article are transferred to a daily and historical data folder**  

The text files containing the article data are transferred to the 'daily' and 'historical' data folders.  

**5) The articles will be opened in a browser**  

The articles are then opened into an online browser for me to read.  

**6) The AI Agent will begin to run, loading the new articles into its database**  

The AI Agent will begin to run, where the text files in the 'daily' folder will be fed into its vector database.  
A 'while' loop will run so I can continuously query the AI Agent until I have finished reading the articles.
  
**7) The Agent will be ready for use and can be queried in command prompt**  

Once the Agent is now running, I will be prompted 'Agent ready for use!' and be requested for a user input  

## Conclusion  

This was a fun, interesting and insightful project that I worked hard on and enjoyed creating, whilst it still provides real value. The project did initially begin as an attempt to create a Learning Assistant but eventually morphed into a Research Assistant due to using a query engine.  
  
Completing this project allowed me to think about practical business use cases for this kind of project as well, for example:  

If a business had hundreds of documents that it needed to fetch information from but didn't want to have to continuously filter through masses of documents. They could be fed into a query engine database and the query engine could be used to return specific information from these documents. Not only that but as this is all local, it is completely private and secure meaning a business could trust that none of its information would be sent elsewhere.
