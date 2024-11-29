import glob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def get_files(url):
    list_name = []

    for name in sorted(glob.glob(url)):
        #name = name.split('diary\\')
        #name = str(name[1])
        list_name.append(name)
    return list_name

def get_date(url):
    date_list = []
    for date in sorted(glob.glob(url)):
        date = date.split('.txt')
        date = str(date[0])
        date = date.split('diary\\')
        date = str(date[1])
        date_list.append(date)
    return date_list

def get_sentiment_analysys(file):
    with open(file, 'r', encoding='utf-8') as txtfile:
        txt = txtfile.read()
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(txt)
    return scores
