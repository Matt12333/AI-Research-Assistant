import os
import chromadb

def clear_database():

    '''
    This function clears the agent database, so it can query only the articles posted on the previous day
    '''

    # Clear old data
    try:
        db = chromadb.PersistentClient('C:\\Users\\Matth\OneDrive\\Desktop\\Coding\Projects\\startup_articles_learning\\main_app\\app\\database')
        db.delete_collection("test_db")
        print("Database successfully cleared!")

    except Exception as e:
        print(f"Unsuccessful in clearing database as {e}")


def clear_daily_data():

    '''
    Clears the 'daily' data in the 'article_data' folder so duplicate data isn't added to the agent database
    '''

    dir_path = r'C:\Users\Matth\OneDrive\Desktop\Coding\Projects\startup_articles_learning\main_app\app\article_data\daily'

    try:
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            os.remove(file_path)

        print("Daily data successfully cleared")

    except Exception as e:
        print(f"Unsuccessful in previous daily data as {e}")   


def clear_previous_daily_data():

    '''
    This function is called in 'main.py' to clear the previous daily data
    '''

    clear_database()

    clear_daily_data()
    print("="*50)
    