#!/usr/bin/env python
# coding: utf-8



import warnings
import itertools
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


#example for EVI in Shobara
#import SARIMA 
# “grid search” is used to find the optimal set of parameters by AIC value

p = d = q = range(0,3)

pdq = list(itertools.product(p,d,q))

seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

warnings.filterwarnings("ignore")

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(ts,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)

            results = mod.fit()

            print('ARIMA{}x{}11 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue



#Fitting the model
mod = sm.tsa.statespace.SARIMAX(ts,
                                order=(1, 0, 1),
                                seasonal_order=(1, 0, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()

print(results.summary().tables[1])




#model diagnostics
results.plot_diagnostics(figsize=(15, 12))
plt.show()


#load prepared data
df = pd.read_csv(r'/Users/zhongchenxi/zy_month_mean_evi.csv',usecols=['evi','year'])
df['year'] = pd.to_datetime(df['year'])


df = df.set_index('year')
ts = df['evi']
ts.index = pd.to_datetime(df.index)
print(ts)

#plot graph
pred = results.get_prediction(start=ts.index[185], dynamic=False)
pred_ci = pred.conf_int()

ax = ts.plot(label='observation')
pred.predicted_mean.plot(ax=ax, label='prediction', alpha=.7, linewidth = 3.5)

ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2, label='prediction interval')

ax.set_xlabel('year')
ax.set_ylabel('Mean Monthly EVI')

plt.gcf().set_size_inches(20, 10)
plt.show()


#evaluate the model performance
y_forecasted = pred.predicted_mean
y_truth = ts[185:]
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error is {}'.format(round(mse, 2)))
print('The Root Mean Squared Error is {}'.format(round(np.sqrt(mse), 2)))
print('r square: %.4f'% r2_score(ts, pred))

