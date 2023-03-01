# importing class Flask,render_template from flask module
from flask import Flask, render_template,request, url_for
# import libraries for my hybrid recommender
import pandas as pd
import numpy as np
from recommendation import search
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# instastiate a Flask object to give a unique name by using __name__
app=Flask(__name__)
# use a decorator an make a REQUEST to the endpoint inside the brackets
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])

def recommend():
    # getting the users input
    user_input = request.form['input']
    # recommend using the model
    # creating a hybrid function
    data = pd.read_csv('cleaned_data.csv')
    #data.drop('Unnamed: 0', axis = 1, inplace = True)
    data.dropna(subset = ['Title'], inplace = True)

    # finding groups of 2 words that are consecutive
    vectorizer = TfidfVectorizer(ngram_range=(1,2))

    tfidf = vectorizer.fit_transform(data["Title"])
  
    
    recommendation = search(user_input)
    return render_template('recommendations.html',recommendation = recommendation)

if __name__ == '__main__':
    app.run(port=5000,debug=True)