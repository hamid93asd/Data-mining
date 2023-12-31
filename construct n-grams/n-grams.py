import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def n_grams_sklearn () :
      # Let ’s read some data
      url = "https://raw.githubusercontent.com/koaning/icepickle/main/datasets/imdb_subset.csv "
      df = pd.read_csv( url ) # This is how you read a csv file to a pandas frame
      corpus = list ( df ['text'])
      corpus_small = corpus [:4] # This is a list of 4 movie reviews

      
     # Read documentation for https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

      def vectorizer(analyzer, ngram): # define a function for vectorizing data
            vectorizer = CountVectorizer(analyzer=analyzer, ngram_range=ngram) # calling CountVectorizer to analyze input with defined parameters
            X = vectorizer.fit(corpus) # this will prepare the data for CountVectorizer
            vocab = X.vocabulary_ # characters with their indexes
            output = (vectorizer.get_feature_names_out()).tolist() # return characters without indexes as list
            matrix = vectorizer.transform(corpus) # transform corpus to matrix
            shape = matrix.shape # show row and column in matrix

            return vocab

      print(vectorizer("char", (2,2))) # for vectorize 2 chars
      print(vectorizer("char", (3,3))) # for vectorize 3 chars
      print(vectorizer("word", (2,2))) # for vectorize 2 words
