import re
import unicodedata
import emoji

class TextProcessor:
    def __init__(self):
        self.PUNCT_TO_REMOVE= """!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~`"""

    ## Convert To Lower Case
    def lower_case(self, raw_text):
        return raw_text.lower()

    ## Remove Punctuation
    def remove_punctuations(self, raw_text):
        return raw_text.translate(str.maketrans('', '', self.PUNCT_TO_REMOVE))

    ## clean HTML element
    def clean_html(self, raw_html):
        clean_text = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        clean_text = re.sub(clean_text, '', raw_html)
        return clean_text

    ## clean unicode character
    def remove_unicode(self, raw_text):
        return unicodedata.normalize('NFKD', raw_text).encode('ascii', 'ignore').decode('utf-8', 'ignore')

    ## clean specific words or text
    def clean_text(self, to_be_clean,target_source):
        return re.sub(to_be_clean, "", target_source)


    ## remove  emoji from the text
    def clean_emoji(self, raw_text):
        return ''.join(c for c in raw_text if c not in emoji.UNICODE_EMOJI)

    ## remove of urls from the text
    def remove_urls(self, text):
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        return url_pattern.sub(r'', text)
