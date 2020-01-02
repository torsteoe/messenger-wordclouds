import json
import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np

currdir = os.path.dirname(__file__)
def create_wordcloud(text):
    mask = np.array(Image.open(os.path.join(currdir, "cloud.png")))
    stopwords = set(STOPWORDS)
    wc = WordCloud(stopwords=stopwords, mask=mask, background_color="white", max_words=200)
    wc.generate(text)
    wc.to_file(os.path.join(currdir, "wordcloud.png"))
create_wordcloud(get_wiki("Python programming language"))

def get_json_data_from_file(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

