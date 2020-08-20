# Daniel-Mod5-Final-Project
# Recommendation Systems

## Introduction:

Used the dataset from worldometers.com for most up to data on COVID19 cases in the US
https://www.worldometers.info/coronavirus/country/us

Used Yelp Dataset (200,000 businesses, millions of reviews & users)

https://www.yelp.com/dataset

## Objective:
 
1. To predict the ratings of Yelp Businesses and create a recommendation system for localized travel and things to do incorporating COVID-19 elements
2. To create a recommendation system for localized travel and restaurants incorporating COVID-19 elements

## The Dataset:

* WorldOMeters
* Yelp

## Skills Required to Complete:

The skills used to complete this project consisted of:

* Working with Python to make visualizations using Matplotlib & Seaborn
* Using Pandas to collect and clean the dataset
* Using BeatuifulSoup to webscrape COVID19 Data
* Building & interpreting various regression models based on RMSE scores & hyperparameter tuning
* Building a recommendation system through surprise package
* Creating a frontend on streamlit user dahsboard to provide recommendations

## What Was Posted on GitHub:

Currently two notebooks posted on GitHub. The Webscrapping & Predicting notebook which consisted of the Data Cleaning, Collection & Modeling components of the supervised machine learning. The second notebook contains a recommendation system based off of the same cleaned data set using the COVID-19 features.

Additionally, covapp.py contains the code used to create the front end dashboard for this project on streamlit

## Questions That Were Posed:

* What kind of categories are the most common in the YELP data set
* Which states would be the safest to visit based on the COVID19 data
* What are some ways that businesses are adapting to COVID19
* What restaurants/cities/states are safe to dine at during COVID19

## How the Data Was Put Together:

The data was gathered from over 200,000 different businesses from the Yelp data set. Following that, the data was cleaned and supplemented with feature engineering. After EDA was performed to see which features had any statistical relationships with one another. Next the data set was put through various regression models to predict star ratings. In addition, webscrapping was pulled from world0meters.com to incorporate relevant COVID19 data. 

For the recommendation system the same cleaned data set was utilized by running the dat through various algorithms. Ultimately SVD was chosen to run the final recommendation system using both content and collaborative filtering. Finally the scraped COVID-19 data and recommendations were coded onto streamlit to serve as a front end application for a user

## Limitations:

* Dataset is limited to specific regions and cities acorss the country
* COVID-19 situation is constantly evolving so data today might not be as relevant tomorrow

## Future Steps:

* Cloud based computing: a personal computer does not have the processing power to incorporate millions of reviews and users
* Explore deep learning recommendation systems
* Further advance to user front end dashboard to be more interactive

## Recommendation Based on Analysis:

Recommendations are at the discretion of the user and their preferences. Additional features such as Takeout/Delivery, Outdoor Seating, BYOB, Reservations, Good for Groups, etc. were all added to aid the user in finding safe options to dine during COVID-19

## Presentation Link:

1st Presentation: Predicting Ratings
https://docs.google.com/presentation/d/1xy46YoCnQQYcBNtZE4EHbuo3UE1-ncaM6w38L4IDzDc/edit#slide=id.p

Final Presentation: Recommendation Systems
https://docs.google.com/presentation/d/1veie-Js1GEn-K0ziimZSFQWdhmVIGD7qdbUlAGYliTQ/edit?usp=sharing

## Visual:

![](https://github.com/dhcho0622/Mod-5-Final-Project/blob/master/PNG_Visuals/Count_of_Ratings.png)








