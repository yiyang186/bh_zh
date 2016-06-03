# encoding: utf-8

#from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import sys
import csv

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    saysDf = pd.read_csv(open('says.csv', 'r'), sep='|')
    saysCorpus = saysDf['content'].dropna().values
    says = ' '.join(list(saysCorpus)).decode('utf-8')
    wordcloud = WordCloud(font_path='msyh.ttf', background_color="black",
                          margin=5, width=2000, height=1500)
    wc = wordcloud.generate(says)
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig('wordcloud.png', dpi=200)
    plt.show()
    # vectorizer = CountVectorizer()
    # X = vectorizer.fit_transform(corpus)
    # wordsCount = X.sum(axis=0)
    # words = vectorizer.get_feature_names()
