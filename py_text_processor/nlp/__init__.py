from collections import Counter
from nltk.corpus import stopwords
from spellchecker import SpellChecker
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from spellchecker import SpellChecker


class NLPUtils:

    def __init__(self, language):
        ## declaration and initialization
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

        self.spell = SpellChecker()
        ## English stopper words
        ", ".join(stopwords.words('english'))
        self.STOPWORDS = set(stopwords.words('english'))

    ## remove stop words
    def remove_stopwords(self,text):
        """custom function to remove the stopwords"""
        return " ".join([word for word in str(text).split() if word not in self.STOPWORDS])

    ## Word stemmer
    def stem_words(self, text):
        return " ".join([self.stemmer.stem(word) for word in text.split()])

    ## word Lemmatization
    def lemmatize_words(self, text):
        return " ".join([self.lemmatizer.lemmatize(word) for word in text.split()])

    ## Correction of spelling
    def correct_spellings(self, text):
        corrected_text = []
        misspelled_words = self.spell.unknown(text.split())
        for word in text.split():
            if word in misspelled_words:
                corrected_text.append(self.spell.correction(word))
            else:
                corrected_text.append(word)
        return " ".join(corrected_text)