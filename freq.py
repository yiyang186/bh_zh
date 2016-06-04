# encoding: utf-8

from sklearn.feature_extraction.text import CountVectorizer
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    num = int(sys.argv[1])

    saysDf = pd.read_csv(open('says.csv', 'r'), sep='|')
    saysCorpus = saysDf['content'].dropna().values

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(saysCorpus)
    wordsCount = np.array(X.sum(axis=0))[0]
    countSum = X.sum()
    wordsFreq = list(wordsCount.astype(float) / float(countSum))
    words = vectorizer.get_feature_names()

    wc = pd.DataFrame({'word': words, 'count': wordsFreq})
    soredwc = wc.sort_values(by='count', ascending=False)
    topwc = soredwc.head(num)


    myfont = matplotlib.font_manager.FontProperties(fname='msyh.ttf')
    pos = np.arange(num)
    width = 0.9
    plt.barh(pos*1.1, topwc['count'].values, width, align='center', alpha=0.4)
    plt.yticks(pos*1.1, topwc['word'].values, fontproperties=myfont)
    plt.ylabel(u'关键词', fontproperties=myfont)
    plt.xlabel(u'词频', fontproperties=myfont)
    plt.title(u'事件主要关键词', fontproperties=myfont)
    plt.savefig('freq.png', dpi=300)
    plt.show()