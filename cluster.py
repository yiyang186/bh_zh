# encoding: utf-8

import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

saysDf = pd.read_csv(open('says.csv', 'r'), sep='|')
contentGroup = saysDf[['uid', 'content']].dropna().groupby('uid')
contents = contentGroup.apply(lambda contentsDf: ' '.join(contentsDf.values.ravel()))

# 构建TF-IDF向量
vectorizer = TfidfVectorizer(max_df=0.5, max_features=5000, min_df=2, use_idf=True)
X = vectorizer.fit_transform(contents.values)

# 潜语义分析与标准化
n_components = 30
svd = TruncatedSVD(n_components)
normalizer = Normalizer(copy=False)
lsa = make_pipeline(svd, normalizer)
X = lsa.fit_transform(X)

# DBSCAN聚类
db = DBSCAN(eps=.7, min_samples=4).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print u"DBSCAN估计的类簇数量: %d" % n_clusters_
print u"DBSCAN轮廓系数: %0.3f" % metrics.silhouette_score(X, db.labels_)
print db.labels_

# K-means聚类
# for n_clusters in range(20):
#     km = KMeans(n_clusters=2, init='k-means++', max_iter=100, n_init=1)
#     km.fit(X)
#     print n_clusters, metrics.silhouette_score(X, km.labels_)
# print(u"K-means轮廓系数: %0.3f" % metrics.silhouette_score(X, km.labels_))
# print km.labels_

df = pd.DataFrame({'user': contents.index, 'label': labels, 'content': contents.values},
                  index=contents.index)

df.to_csv("cluster.csv", sep='|')
