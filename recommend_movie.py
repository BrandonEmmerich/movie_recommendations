import nltk
from nltk.corpus import stopwords
import pandas as pd
import pprint
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import sys

def load_data():
    df_raw = pd.read_csv('data/raw_data.zip', compression='zip', header=0, sep=',', quotechar='"')
    df = df_raw[df_raw['Origin/Ethnicity'] == 'American'].tail(1000)

    return df

def remove_unicode_and_nulls(input):
    if type(input) == str:
        clean_text = re.sub(r'[^\x00-\x7f]',r'', input)
        return clean_text
    elif input is None:
        return '-'
    else:
        return input

if __name__ == '__main__':
    user_input = str(sys.argv[1])
    vectorizer = TfidfVectorizer()
    df = load_data()
    df = df.fillna('.')
    df.applymap(remove_unicode_and_nulls)

    user_movie_index = df[df['Title'] == user_input].index.tolist()[0]

    movie_plots = df['Plot'].tolist()
    plot_to_search = df['Plot'][df['Title'] == user_input].iloc[0]
    movie_plots.append(plot_to_search)
    tfidf_plots = vectorizer.fit_transform(movie_plots)
    cosine_similarity_values_plots = cosine_similarity(tfidf_plots[-1], tfidf_plots)

    movie_casts = df['Cast'].tolist()
    cast_to_search = df['Cast'][df['Title'] == user_input].iloc[0]
    movie_casts.append(cast_to_search)
    tfidf_casts = vectorizer.fit_transform(movie_casts)
    cosine_similarity_values_casts = cosine_similarity(tfidf_casts[-1], tfidf_casts)

    movie_directors = df['Director'].tolist()
    director_to_search = df['Director'][df['Title'] == user_input].iloc[0]
    movie_directors.append(director_to_search)
    tfidf_directors = vectorizer.fit_transform(movie_directors)
    cosine_similarity_values_directors = cosine_similarity(tfidf_directors[-1], tfidf_directors)

    average_cosine_similarty = (cosine_similarity_values_casts + cosine_similarity_values_plots + cosine_similarity_values_directors)/3.0
    sorted_similarity_scores = average_cosine_similarty.argsort()[0]

    top_three = [-3, -4, -5] # Start counting at third to last because the list of plots includes the searched movie twice

    movie_recommendations = []
    for counter, position in enumerate(top_three):
        movie_index = sorted_similarity_scores[position]
        movie_details = df[df['Plot'] == movie_plots[movie_index]].to_dict()
        percent_match = round(100*average_cosine_similarty[0][movie_index],1)

        recommendation = {
            '1. Rank': counter + 1,
            '2. Title': movie_details['Title'].values()[0],
            '3. Percent Match': percent_match,
            '4. Cast': movie_details['Cast'].values()[0].replace("\r\n", ", "),
            '5. Director': movie_details['Director'].values()[0],
            '6. Year': movie_details['Release Year'].values()[0],

        }
        movie_recommendations.append(recommendation)

    pprint.pprint(movie_recommendations)

import ipdb; ipdb.set_trace()
