import re
import pandas as pd
from collections import Counter

from txt import TextProcessor
from nlp import NLPUtils

## https://www.kaggle.com/sudalairajkumar/getting-started-with-text-preprocessing
## https://github.com/rishabhverma17/sms_slang_translator/blob/master/slang.txt
## https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset


class DataFrameProcessor:
  def __init__(self, language):
    self.nlp_utils = NLPUtils(language)
    self.text_processor = TextProcessor()

# remove all records which are having null values for a specific column
  def df_remove_null_column(self, columnName,df):
    return df[~df[columnName].isnull()]

  # remove all records which are having null values for a specific column
  def df_remove_null(self, columnName,df):
    return df.dropna(how='any',axis=0)

  ## Remove Punctuation
  def df_remove_punctuation(self, columnName,df):
      return df.loc[:,columnName].apply(lambda x: self.text_processor.remove_punctuations(x))

  ## Remove Punctuation
  def df_lower_case(self, columnName,df):
      return df.loc[:,columnName].apply(lambda x: self.text_processor.lower_case(x))

  ## clean HTML element
  def df_clean_html(self, columnName,df):
    return df.loc[:,columnName].apply(lambda x: self.text_processor.clean_html(x))

  ## clean unicode character
  def df_remove_unicode(self, columnName,df):
    return df.loc[:,columnName].apply(lambda x: self.text_processor.remove_unicode(x))

  ## clean specific words or text
  def df_clean_text(self, to_be_clean, columnName, df):
    return df.loc[:,columnName].apply(lambda x: self.text_processor.clean_text(to_be_clean,x))


  ## remove  emoji from the text
  def df_clean_emoji(self, to_be_clean, columnName, df):
    return df.loc[:,columnName].apply(lambda x: self.text_processor.clean_emoji(x))

  ## remove url from the dataframe column
  def df_remove_urls(self, to_be_clean, columnName, df):
    return df.loc[:,columnName].apply(lambda x: self.text_processor.remove_urls(x))

  ## remove stop words
  def df_remove_stopwords(self, columnName, df):
    return df.loc[:,columnName].apply(lambda x: self.nlp_utils.remove_stopwords(x))

  ## get word frequency
  def df_get_word_frequency(self, columnName, df,top_words):
    cnt = Counter()
    for text in df[columnName].values:
        for word in text.split():
            cnt[word] += 1
    return cnt.most_common(top_words)


  ## dataframe Stem words
  def df_stem_words(self, columnName, df):
    return df.loc[:,columnName].apply(lambda x: self.nlp_utils.stem_words(x))

  ## dataframe Stem words
  def df_lemmatize_words(self, columnName, df):
    return df.loc[:,columnName].apply(lambda x: self.nlp_utils.lemmatize_words(x))
