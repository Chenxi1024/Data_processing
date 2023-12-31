# -*- coding: utf-8 -*-
"""statistical analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/187G9zI6evzatTVoSEOOnsAPLy7nMFrbT
"""

from google.colab import drive
drive.mount('/content/drive')

pip install pingouin

import pingouin as pg
import pandas as pd

"""one way"""

path=r'/content/drive/MyDrive/zy_change_2011-2019_terrainclass_all.csv'
df=pd.read_csv(path)
aov=pg.anova(data=df,dv='evi',between='maxcur',detailed=True)
aov.round(3)

"""assumption check: Shapiro-Wilk test

"""

import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path=r'/content/drive/MyDrive/zy_change_2011-2019_terrainclass_all.csv'
df=pd.read_csv(path)
x=df["slo"]
# x=x[(x > -0.5) & (x < 0.5)]
fig = plt.figure(figsize= (10, 10))
ax = fig.add_subplot(111)

normality_plot, stat = stats.probplot(x, plot= plt, rvalue= True)
ax.set_title("Probability plot of model residual's", fontsize= 20)
ax.set

plt.show()

"""two-way ANOVA"""

import pandas as pd
path=r'/content/drive/MyDrive/xyc_change_1985-2011_terrainclass_all.csv'
df=pd.read_csv(path)
# two-way ANOVA with balanced design
df.anova(dv="evi", between=["ele", "hil"]).round(3)
# two-way ANOVA with unbalanced design(requires statsmodels)
# df.anova(dv="bi", between=["hil", "slo"],effsize= "n2" ).round(3)

"""Three-way ANOVA"""

path=r'/content/drive/MyDrive/xyc_change_1985-2011_terrainclass_all.csv'
df=pd.read_csv(path)
df.anova(dv='evi', between=['asp', 'hor', 'ver'],
           ss_type=3).round(3)

"""POST-HOC TESTING"""

import numpy as np
import pandas as pd
import statsmodels.stats.multicomp as mc
import glob
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd

comp = mc.MultiComparison(df['ndvi'], df['ver'])
post_hoc_res = comp.tukeyhsd()
post_hoc_res.summary()

# post_hoc_res.plot_simultaneous(ylabel= "aspect", xlabel= "value Difference")

import numpy as np
import pandas as pd
import statsmodels.stats.multicomp as mc
import glob
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
path=r'/content/drive/MyDrive/zy_change_2011-2019_terrainclass_all.csv'
df=pd.read_csv(path)

comp = mc.MultiComparison(df['ndvi'], df['geo'])
post_hoc_res = comp.tukeyhsd()
post_hoc_res.summary()

# post_hoc_res.plot_simultaneous(ylabel= "geology", xlabel= "value Difference")

"""spearman coefficient"""

path = r'/content/drive/MyDrive/zy_change_2011-2019_terrainclass_all.csv'
df = pd.read_csv(path)
df = df[(df['slo']>30) & (df['slo']<80)]
# print(df)
pg.corr(df['slo'],df['evi'],method="pearson").round(3)
