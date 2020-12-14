# py-text-processor
py-text-processor is collection of python function which is helpful in data pre processing and cleaning


# Core Features
- Text Processing & Data Cleaning
- NLP Utilities
- Data Frame processing

# Installation
    git clone https://github.com/Kohimax/py-text-processor.git
    cd py-text-processor
    pip install --editable .

# Example
    from py_text_processor.txt import TextProcessor
    txt_utils = new  TextProcessor()
    
    txt = 'Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data.'
    result = txt_utils.lower_case(txt)
