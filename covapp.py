import streamlit as st
import pandas as pd
import numpy as np
import re
from sklearn.externals import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

from scipy import stats

from surprise import Dataset
from surprise import Reader
from surprise.model_selection import GridSearchCV
from surprise.model_selection import cross_validate
from surprise import SVD

st.write("""
# COVID-19 Restaurant Recommendation App

COVID-19 has dramatically changed the landscape of traveling for the future. Many of us haved stayed home for we
eks or months without leaving our homes or with any human interactions. This app will hopefully guide you through
these unprecendented times! Whether you want up to date COVID19 cases counts or recommendations on safe place for your next meals

one of the recommenders below can help. The first recommender will incorporate what common features you look for in a restaurant such as location, price point, or for COVID19 purpose delivery/takeout

the second recommender uses your preferences as well as ratings from other similar users to help guide you

you can type in a unique user id and the system will check for restaurants that this userlikes and recommend similar!
""")

def covid_data():
    dfcov = pd.read_csv('daily_corona.csv', index_col = 0)
    return dfcov

def covid_data_edit():
    dfcov = pd.read_csv('daily_corona_edited.csv', index_col = 0)
    return dfcov

def covid_new_cases():
    dfcov = pd.read_csv('daily_corona_new_cases.csv', index_col = 0)
    return dfcov

def covid_total_cases():
    dfcov = pd.read_csv('daily_corona_total_cases.csv', index_col = 0)
    return dfcov

dfd = covid_data()
dfcov = covid_data_edit()
dfnc = covid_new_cases()
dftc = covid_total_cases()
df = pd.read_csv('model_data.csv', index_col = 0)
df_rec = pd.read_csv('model1_data.csv', index_col = 0)
df_con = pd.read_csv('model2_data.csv', index_col = 0)
svd = SVD(n_factors=100, reg_all=0.1, n_epochs=30, verbose = True)

st.subheader('COVID-19 Data')
st.write(dfd)

st.write("### New COVID-19 Cases by States")

st.line_chart(dfnc)

st.write("### Total COVID-19 Cases by States")

st.line_chart(dftc)

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df, reader)
dataset = data.build_full_trainset()
svd.fit(dataset)

def recommendations_basic(user_id, model, num, state):
    business_rating = []
    for business_id in df['business_id'].unique():
        business_rating.append((business_id,model.predict(user_id,business_id)[3]))
    business_preds = pd.DataFrame(business_rating)
    business_preds.columns = ['business_id','stars']
    business_preds = business_preds.sort_values(by='stars',ascending=False)
    business_rec = business_preds.merge(df_rec, on = 'business_id', how ='inner')
    business_rec = business_rec.drop_duplicates(subset='business_id',keep='first')
    state_rec = business_rec[business_rec['state'] == state]
    return state_rec[0:num]

st.write("### Collaborative Filtering: SVD for Restaurants in Pennsylvania")
st.write(recommendations_basic('V34qejxNsCbcgD8C0HVk-Q', svd, 5, 'PA'))

def recommendations_cont(num, state, city, price, choice, rcount):
    state_rec = df_con[df_con['state'] == state]
    city_rec = state_rec[state_rec['city'] == city]
    price_rec = city_rec[city_rec['RestaurantsPriceRange2'] == price]
    choice_rec = price_rec[price_rec['delivery or takeout'] == choice]
    review_rec = choice_rec[choice_rec['review_count'] >= rcount]
    return review_rec.sort_values(by='stars',ascending = False)[0:num]

st.write("### Content Filtering: SVD for Restaurants in Phoenix & Price$$ & Delivery/Takeout Option)")
st.write(recommendations_cont(5, 'AZ', 'Phoenix', 2, 1, 50))

