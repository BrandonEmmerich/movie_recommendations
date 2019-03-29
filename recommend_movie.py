import nltk
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys

def load_and_clean_data():
    df_raw = pd.read_csv('data/raw_data.zip', compression='zip', header=0, sep=',', quotechar='"')
    df = df_raw[df_raw['Origin/Ethnicity'] == 'American']
    df = df.fillna('.') # fill NA with punctuation so the TfidfVectorizer removes them

    return df

def calculate_cosine_similarity(search_parameter):
    '''
    Given a search parameter, ie a column in the movies dataframe, return cosine
    similarity scores for a given movie with all other movies in the dataset.
    '''
    documents = df[search_parameter].tolist()
    comparison_document = df[search_parameter][df['Title'] == user_input_movie_title].iloc[0]
    documents.append(comparison_document)

    tfidf = vectorizer.fit_transform(documents)
    cosine_similarity_values = cosine_similarity(tfidf[-1], tfidf)

    return cosine_similarity_values


if __name__ == '__main__':
    user_input_movie_title = str(sys.argv[1])
    df = load_and_clean_data()
    vectorizer = TfidfVectorizer()
    all_movie_titles = df['Title'].tolist()

    while True:
        if user_input_movie_title not in all_movie_titles:
            print("That movie isn't in the database, please check your spelling.")
            break

        search_parameters_and_weights = [('Plot', 3), ('Cast', 1), ('Director', 1)]
        cosine_similarity_values = []
        all_weights = []

        for parameter, weight in search_parameters_and_weights:
            values = weight * calculate_cosine_similarity(parameter)
            cosine_similarity_values.append(values)
            all_weights.append(weight)

        average_cosine_similarty = np.array(cosine_similarity_values).mean(axis = 0) / sum(all_weights)
        sorted_similarity_scores = average_cosine_similarty.argsort()[0]

        top_movie_positions = [-3, -4, -5, -6, -7] # Start counting at third to last because the list of plots includes the searched movie twice

        movie_recommendations = []
        for counter, position in enumerate(top_movie_positions):
            movie_index = sorted_similarity_scores[position]
            movie_details = df.iloc[sorted_similarity_scores[position]].to_dict()
            movie_similarity_score = round(100 * average_cosine_similarty[0][movie_index], 1)

            recommendation = {
                '1. Rank': counter + 1,
                '2. Title': movie_details['Title'],
                '3. Movie Similarity Score': movie_similarity_score,
                '4. Cast': movie_details['Cast'].replace("\r\n", ", "),
                '5. Director': movie_details['Director'],
                '6. Year': movie_details['Release Year'],
            }
            movie_recommendations.append(recommendation)

        pprint.pprint(movie_recommendations)

        break
