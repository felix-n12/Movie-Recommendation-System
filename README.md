# Movie-Recommendation-System
## Authors
* [Collins Kiptoo](https://github.com/Collins-Kiptoo)
* [Amos Pride](https://github.com/amoskiito)
* [Faith Makokha](https://github.com/faithmaks)
* [Felix Nyagah](https://github.com/felix-n12)
* [Gorreti Muthoni](https://github.com/Gorreti)
* [Jamleck Mathenge]()

## Overview
Anime has become an increasingly popular genre of entertainment in recent years, brought about by nerd culture gaining popularity in the mainstream pop culture areas. Some people like it just for the subtitles 
The explosive growth in the amount of available digital information and the number of visitors to the Internet have created a big challenge where consumers have a wide variety of choices but yet very few choices at their disposal and producers have a difficult time figuring out their potential
market. Information retrieval systems, such as Google, DevilFinder, and Altavista have partially solved this problem but the personalization of this data to make relevant recommendations to consumers and producers were absent.
Recommender systems are information filtering systems that deal with the problem of information overload by filtering vital information fragments out of large amounts of dynamically generated information according to the user’s preferences, interests, or observed behavior about an item. The recommender system has the ability to predict whether a particular user would prefer an item or not based on the user’s profile.
Recommender systems are beneficial to both service providers and users. They reduce the transaction costs of finding and selecting items in an online shopping environment. Recommendation systems have also proved to improve the decision-making process and quality. In an e-commerce setting, recommender systems enhance revenues, for the fact that they are effective means of selling more products. In scientific libraries, recommender systems support users by allowing them to move beyond catalog searches. Therefore, the need to use efficient and accurate recommendation techniques within a system that will provide relevant and dependable recommendations for users cannot be over-emphasized.
## Problem Statement
In the past, people used to shop in a physical store, in which the items available were limited. For instance, the number of movies/music CDs/vinyl that can be placed in a local shop depends on the size of that shop. By contrast, nowadays, the Internet allows people to access abundant resources online. Netflix, for example, has an enormous collection of movies. Although the amount of available information increased, a new problem arose as people had a hard time selecting the items they actually wanted to see and the production companies had a difficult time locating their target audience.
Due to the prevalence of the Internet, we need recommender systems in modern society that will assist people in finding products that are in their tastes and preference from the vast options. Moreover, recommendation systems can be deployed on commercial websites to help producers market their products to the right consumers.

## Proposed Solution
The most appropriate solution to deal with our problem is to come up with a system that would recommend movies to our consumers based on their preferences and tastes in order to maximize consumer utility and increase profits for producer companies.
## Justification of the Study
The objective of recommender systems is to provide recommendations based on recorded information on the users' preferences. If recommendations are engineered and deployed effectively they can have a direct impact on the world. Users would be able to access movies in line with their interests thereby maximizing their utility whereas movie producers will be able to know their target market thereby maximizing profits.

## Specific Objectives

* To build a model that will recommend the most likely anime a user may watch.

* To find out the most watched anime genre

* To determine the highest rated genre

* To determine the anime source with the most members

## Research Questions

* Which is the model that provides recommendations?

* What is the most-watched anime genre? 

* What is the highest-rated anime genre?

* Which anime sources have the most members?

## Success Criteria
Create a model that can recommend movies to users with an RMSE of 2.0 and below. 

## DATA UNDERSTANDING
### Overview

In this project, a dataset containing a list of anime movies was collected from kaggle.
Exploring Data

The dataset has the following features.

●      Data contains 17002 entries.

●      There are 15 columns.

The following are the columns in the dataset.

* Anime_id :anime Id (as per myanimelist.net)
* Title : Name of anime
* Genre :Main genres in the movie
* Synopsis :Brief Description
* Type
* Producer: Production company of the anime
* Studio: The studio that produced the anime
* Rating: Rating of anime as per myanimelist. net/(on a scale of 1-10)
* ScoredBy: Total no user scored given anime
* Popularity: Rank of anime based on popularity
* Members: No of members added given anime on their list
* Episodes: No. of episodes
* Source
* Aired
* Link: Link to the anime on myanimelist

## DATA PREPARATION 

This was done to ensure the Validity, Accuracy, Completeness, Consistency, and Uniformity of the Data. These are the steps followed in preparing the data: 

>- TASK1: The first task was to check if the column names were uniform and readable.
>- TASK2: The second task was to check for duplicated rows.
>- TASK3: The next task was to check if there were missing values.
>- TASK4:The next task was to decide how to deal with the missing values. (Either drop if they are unnecessary or replace the missing values with the best 
fit.)
>- TASK5: The last task was to check if the columns had the correct data types.

## DATA ANALYSIS 

To better comprehend the data patterns and even develop some hypotheses, let’s first begin by studying our dataset. In order to find any significant trends, we will first examine the distribution of the various variables.


### Univariate analysis

This involves the plotting of data into histograms and bar charts in order to have a better understanding of the data.

From the univariate analysis, we came up with the following inferences:

Animes aired on TV are the most watched

Hental is the top genre.

The top-known movie sources are original sources and Manga


### Bivariate analysis

This involves the use of two columns on our dataset in order to plot charts that will show the relationship between various features in our dataset.

From the bivariate analysis, we came up with the following inferences:

Light novel, Manga, and 4-Koma manga are the top-rated anime sources
(‘Aniplex’, ‘Square Enix’, ‘Mainichi Broadcast with 9,25), ( ‘Kadokawa Shoten,’ ‘Toho’, ‘Sound Team Don Ju with 9.19) and (‘TV Tokyo’, ‘Aniplex’, ‘Dentsu’ with 9.15 ) are the most-rated producers

Death note, Shingeki no Kyojin and Sword art online are the anime movies that are rated the most.

All movie sources produce different types of anime movies. Moreover, original and manga sources are the most popular.

### Multi-variate analysis

This involves using more than two columns of data to create charts that will give us a superior understanding of how the various features affect and relate to each other.

This involves using more than two columns of data to create charts that will give us a superior understanding of how the various features affect and relate to each other.
From the multivariate analysis, we came up with the following inferences:

The average rating of the types in the anime sources is 6.5   But there is no clear observed difference between the different sources or types.

## MODELLING
### Pre-processing
We create a function that will be able to clean the anime titles using REGEX. Cleaning the title name is crucial because it can often lead to errors whereby the title name is not in a machine-readable format
Then we use the term frequency-inverse document frequency to create a search engine so that it is easy to find an anime title and its anime id. The tfdif Vectorizer will enable the computer to find the title that is most similar to the title we enter.
We then create a function that will use cosine similarity to compute the similarity between a term that we will enter in our search box and the anime titles in our dataset.
We then build an interactive search box that will enable one to type in the name of an anime and have the results.

Modeling Techniques
We used various modeling techniques to create a recommendation system
Including

Content-Based model (Model 1)
We build a content-based model by using the ‘synopsis’  and ‘Title’ column.
We make use of linear kernel to make a matrix based on the cosine similarity.
We then make a function that takes in the anime title and cosine similarity and returns the 15 most similar movies

Content-Based model (Model 2)
We build a content-based model by using the ‘studio’,  ‘genre’, and ‘Producer’ column.
We make use of linear kernel to make a matrix based on the cosine similarity.
We then make a function that takes in the anime title and cosine similarity and returns the 15 most similar movies

Collaborative filtering  Recommendation system
Under collaborative filtering, we made use of the KNN machine learning algorithm.
KNN is a machine learning algorithm to find clusters of similar users based on common book ratings and makes predictions using the average rating of top-k nearest neighbors.
Once the model was correctly engineered we made a function that takes in a movie and gives recommendations of other movies based on the movie the user watched.
We make a pivot table for an easier modeling process.

Item-based
We generate a compressed sparse row from the pivot values in the pivot table.
We employed KNN with cosine as the metric.
We then make a function that takes in the name and a number and returns the number of most similar movies

User-based 
A user-based recommendation system predicts the user preferences or ratings that users would give to items. We made use of pair_wise distances that computes the distances between corresponding elements of two arrays.
The next step is to make predictions based on these similarities which are done by a function we created that takes in the movie ratings, the user similarity scores, and the type of user and gives recommendations.

Hybrid Recommendation System
We create a function that takes in a user, ratings based on collaborative filtering, and predictions based on user-based recommendations to make recommendations on what movie a user should view based on their tastes and preferences. 
we use the Term Frequency-inverse document frequency to create a search engine so that it is easy to find an anime title and its anime id. The tddif will enable the computer to find the title that is most similar to the one we enter.
We will then create a function that will use cosine similarity to compute the similarity between a term that we will enter in our search and all the anime titles in our dataset.
We implement the model to find similar users by finding the score between the similar users and all users. The higher the score the better the recommendation. We then get the top 10 recommendations and their titles
We create a function to perform the previous function more efficiently.
We then create an interactive recommendation widget where one enters the anime title and gets recommendations based on the title.

Model-Based modeling
We make use of the KNNwithmeans and SVD algorithms to build our recommendation system
We make use of surprise to find the best collaborative filtering model.
Model validation
KNNwithmean: RMSE is 1.6958 for test data and 1.706 for validation data.
SVD: RMSE is 1.6959 for test data and 1.707 for validation data.
 
Model Evaluation
We have built two types of models:
Metric based
Model based
 
For the metric-based model, we have the content-based and the hybrid model. The hybrid model gave better recommendations than the content-based model.
For the Model-based, we have used the SVD and  KNNwithmeans algorithms. Both models perform almost the same hence we opted to go with either of the models since they both satisfy our objective of attaining an RMSE of 2.0 and below.

Deployment
We made use of Streamlit which is an open source python-based framework for developing and deploying interactive data science dashboards and machine learning models.
The app prompts the user to select a title then it gives the top 10 recommendations.
Link:Recommendation System 
RECOMMENDATIONS
This app is beneficial for anime lovers and anime producers
The recommendation system can be improved by using GridSearch cv. Grid 
Search requires a lot of computation power therefore it is recommended that you have rough computation power.

### Hybrid Recommendation System

We create a function that takes in a user, ratings based on collaborative filtering and predictions based on user-based recommendations to make recommendations on what movie a user should view based on their tastes and preferences.

## Model Validation.

We employ Root mean squared error to validate our hybrid model.
The model has an RMSE which is 1.707

## Deployment

We made use of Streamlit which is an open source python-based framework for developing and deploying interactive data science dashboards and machine learning models.
[Link](https://anime-deployment.streamlit.app/) 





