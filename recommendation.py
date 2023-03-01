
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def search(title):
    """
    A function that takes in a search term of the title that we are 
    looking for then cleans it and uses the vectorizer
    to turn it into a sparse matrix and then uses cosine similarity to find the
    most similar titles.
    """
    data = pd.read_csv('cleaned_data.csv')
    #data.drop('Unnamed: 0', axis = 1, inplace = True)
    data.dropna(subset = ['Title'], inplace = True)

    # finding groups of 2 words that are consecutive
    vectorizer = TfidfVectorizer(ngram_range=(1,2))

    tfidf = vectorizer.fit_transform(data["Title"])
  
    # cleaning the title entered
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()

    # find the 5 most similar titles to the searcch term
    indices = np.argpartition(similarity, -5)[-10:]

    # reverse results so that most similar result is at the top
    results = data.iloc[indices].iloc[::-1]
    
    return results['Title'].to_list()