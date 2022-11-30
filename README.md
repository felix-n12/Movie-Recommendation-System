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
In the past, people used to shop in a physical store, in which the items available are limited. For instance, the number of movies that can be placed in a Blockbuster store depends on the size of that store. By contrast, nowadays, the Internet allows people to access abundant resources online. Netflix, for example, has an enormous collection of movies. Although the amount of available information increased, a new problem arose as people had a hard time selecting the items they actually want to see and the production companies had a difficult time locating their target audience.
Due to the prevalence of the Internet, we need recommender systems in modern society that will assist people in finding products that are in their tastes and preference from the vast options. Moreover, recommendation systems can be deployed on commercial websites to help producers market their products to the right consumers.
## Proposed Solution
The most appropriate solution to deal with our problem is to come up with a system that would recommend movies to our consumers based on their preferences and tastes in order to maximize consumer utility and increase profits for producer companies.
## Justification of the Study
The objective of recommender systems is to provide recommendations based on recorded information on the users' preferences. If recommendations are engineered and deployed effectively they can have a direct impact on the world. Users would be able to access movies in line with their interests thereby maximizing their utility whereas movie producers will be able to know their target market thereby maximizing profits.
## Specific Objectives
To build a model that will recommend and make predictions about a  user’s taste.
To build a model that will be able to show movie producers their target audience.

Research Questions

●  	What are the most popular anime genres?

●  	What are the top movie sources? 
## Success Criteria
Create a model that can recommend movies to users based on their preferences 
## DATA UNDERSTANDING
Overview

In this project, a dataset containing a list of anime movies was collected from kaggle.
Exploring Data

The dataset has the following features.

●      Data contains 17002 entries.

●      There are 15 columns.

The following is a brief description of the columns in the dataset.

Anime_id :anime Id (as per myanimelist.net)

Title : Name of anime

Genre :Main genres in the movie

Synopsis :Brief Description

Type

Producer: Production company of the anime

Studio: The studio that produced the anime

Rating: Rating of anime as per myanimelist. net/(on a scale of 1-10)

ScoredBy: Total no user scored given anime

Popularity: Rank of anime based on popularity

Members: No of members added given anime on their list

Episodes: No. of episodes

Source

Aired

Link: Link to the anime on myanimelist
## DATA PREPARATION 
This was done to ensure the Validity, Accuracy, Completeness, Consistency, and Uniformity of the Data. These are the steps followed in preparing the data: 

TASK1: The first task was to check if the column names were uniform and readable.

TASK2: The second task was to check for duplicated rows.

TASK3: The next task was to check if there were missing values.

TASK4:The next task was to decide how to deal with the missing values. (Either drop if they are unnecessary or replace the missing values with the best 
fit.)

TASK5: The last task was to check if the columns had the correct data types.

The data provided is correct and up to date.

link to notebook:
## DATA ANALYSIS 
To better comprehend the data patterns and even develop some hypotheses, let’s first begin by studying our dataset. In order to find any significant trends, we will first examine the distribution of the various variables.


Univariate analysis

This involves the plotting of data into histograms and bar charts in order to have a better understanding of the data.

From the univariate analysis, we came up with the following inferences:







Bivariate analysis

This involves the use of two columns on our dataset in order to plot charts that will show the relationship between various features in our dataset.

From the bivariate analysis, we came up with the following inferences:








Multi-variate analysis

This involves using more than two columns of data to create charts that will give us a superior understanding of how the various features affect and relate to each other.

From the multi-variate analysis, we came up with the following inferences:








### Visualization 

The charts we generated from the Exploratory Data Analysis are: 

## MODELLING
Pre-processing
We create a function that will be able to clean the anime titles using REGEX. Cleaning the title name is crucial because it can often lead to errors whereby the title name is not in a machine-readable format
Then we use the term frequency-inverse document frequency to create a search engine so that it is easy to find an anime title and its anime id. The tfdif Vectorizer will enable the computer to find the title that is most similar to the title we enter.
We then create a function that will use cosine similarity to compute the similarity between a term that we will enter in our search box and the anime titles in our dataset.
We then build an interactive search box that will enable one to type in the name of an anime and have the results.

## Modeling Techniques





