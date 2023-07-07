#!/usr/bin/env python
# coding: utf-8



#example for EVI in Obara

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# load and preprocess data
path = r'/Users/xyc_month_mean_evi_compare.csv'
df = pd.read_csv(path)
df= df.set_index("year")

#plot different conditions
plt.plot(df['normal'], label='normal', color='green', linestyle='dashed')
plt.plot(df['positive'], label='positive', color='steelblue')
plt.plot(df['negative'], label='negative', color='purple')
plt.legend()
plt.ylabel('Mean Monthly EVI', fontsize=10)
plt.xlabel('year', fontsize=10)
plt.gcf().set_size_inches(20, 10)
plt.xticks(df.index[::12], rotation=45)

plt.show()





