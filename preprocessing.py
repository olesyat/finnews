import pandas as pd
from pattern.en import lemma
import pandas as pd
import numpy as np

import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim.models import CoherenceModel, TfidfModel, LdaMulticore, Phrases, LdaSeqModel
from gensim.corpora import Dictionary

class Preprocess:
    def __init__(self, df):
        self.df = df

    def remove_duplicates(self, column):
        self.df.drop_duplicates(subset=column, keep=False, inplace=True)

    def preprocess(self, text):
        result = [token for token in simple_preprocess(text) if token not in STOPWORDS and len(token) > 3]
        return result

    def make_bigrams(self, processed_docs):
        bigram = Phrases(processed_docs, min_count=5, threshold=100)
        bigram_mod = gensim.models.phrases.Phraser(bigram)
        processed_docs = [bigram_mod[doc] for doc in processed_docs]
        return processed_docs

    def custom_clean(self):
        pass