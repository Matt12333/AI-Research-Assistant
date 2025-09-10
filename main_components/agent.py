import time

from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex
from llama_index.llms.ollama import Ollama

def run_agent():

    '''
    Loads the data into the agent database and initialises the agent to be queried
    '''

    start = time.time()

    
    # Load the data
    reader = SimpleDirectoryReader(input_dir='C:\\Users\\Matth\\OneDrive\\Desktop\\Coding\\Projects\\startup_articles_learning\\main_app\\app\\article_data\\daily')

    # Converts the data in a document object
    documents = reader.load_data()

    # Create a folder containing the sql database 
    # Everything embedded is permenently stored here
    db = chromadb.PersistentClient('C:\\Users\\Matth\OneDrive\\Desktop\\Coding\Projects\\startup_articles_learning\\main_app\\app\\database')

    # Create/Load a collection to store the vector embeddings from the chunks/nodes
    chroma_collection = db.get_or_create_collection('test_db')

    # Make the collection compatible with 'llamaindex'
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    # Defines how documents will be processed and outputs are sent
    # Outputs are delivered to the vector store
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=512, chunk_overlap=50), # Breaks the document down into chunks, based on sentence boundaries
            HuggingFaceEmbedding(model_name='BAAI/bge-small-en-v1.5'), # Creates vector embeddings of each chunk
        ],
        vector_store=vector_store
    )

    # Run the data through the pipeline to embed the data and store it in the vector store  
    pipeline.run(documents=documents)

    # Initialise embedding model to embed string data, same model in the pipeline
    embed_model = HuggingFaceEmbedding(model_name='BAAI/bge-small-en-v1.5')

    # The Chroma vector store is wrapped in a 'VectorStoreIndex'
    # This allows it to be queried using natural language
    index = VectorStoreIndex.from_vector_store(vector_store, embed_model=embed_model)

    llm=Ollama(
        model="llama3.2:3b",
        request_timeout=180.0,
        context_window=2000)

    query_engine = index.as_query_engine(
        llm=llm,
        response_mode='tree_summarize',
        system_prompt='''You are a personal research and learning assistant, providing accurate information based on the questions you are asked.
                        If there are articles that have been posted on the websites: MIT News or KD Nuggets, you will be provided them within a text file.
                        These text files are individual articles that you will query to help the user, this could range from: defining definitions about terms within the 
                        queries; summarising each article/text file you are give or more. When you are instructed to summarise a article/text file, you must summarise all the
                        text data within that file, not just the first portion.
                        ''')

    print('Time taken: ', time.time() - start)
    print("\nAgent ready for use!")
    
    while True:
        print('\n' + ('='*50))
        print('\nUser Input:')

        question = input("\nAsk me something (or type 'exit'): ")
        if question.lower() == "exit":
            break
        resp = query_engine.query(question)

        print('\n' + ('='*50))
        print('\nAgent Response:\n')
        print(resp)