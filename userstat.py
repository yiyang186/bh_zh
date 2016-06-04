# encoding: utf-8

import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

userDf = pd.read_csv(open('user.csv', 'r'), sep='|')

for col in ['gender', 'school', 'major', 'location']:
    count = userDf[col].value_counts()
    count.to_csv(col + ".csv")


