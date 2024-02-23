# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:38:59 2023

@author: pb910

this script reads in the csv of mcyintyre tensile results
it produces a grouped by sample violin plot

based on https://stackoverflow.com/questions/43345599/process-pandas-dataframe-into-violinplot


"""

import chardet # used to detect csv encoding
import pandas as pd
import matplotlib.pyplot as plt

encodi = 'ISO-8859-1'  # assumed encoding of the csv file

### only have to use this once to confirm that PAS csv outpuits as a ISO-8859-1 format.
### kept for future resilience, but one regular runs just slows things down.
#with open('whorls_20240223112608.csv', 'rb') as f:
#    enc= chardet.detect(f.read())
#    print('encoding found')
#   encodi = enc['encoding']

data = pd.read_csv('whorls_20240223112608.csv', encoding = encodi)
data3d = pd.read_csv('3dwhorls_20240223112559.csv', encoding = encodi)

filt_data = data[data['weight'].notnull()] # strip out nulls
filt_data = filt_data[filt_data['weight'] > 1.0] # strip out weights less than 1g (typos?)


# pubvlishable image settings
cm = 1/2.54  # centimeters in inches
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(8*cm*2, 5*cm*2))

SMALL_SIZE = 9
MEDIUM_SIZE = 11.5
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
# /pubvlishable image settings

fig.suptitle("Violin plots and medians of PAS spindle whorl data")
ax1.violinplot(dataset = filt_data["weight"].values, showmeans=False, showextrema=True, showmedians=True, bw_method=0.1)
ax2.violinplot(dataset = filt_data["weight"].values, showmeans=False, showextrema=False, showmedians=True, bw_method=0.1)
ax2.violinplot(dataset = data3d["weight"].values, showmeans=True, showextrema=True, showmedians=True, bw_method=0.1)



ax1.set_ylabel('Weight (g)')
ax1.set_xlabel('Extrema and median')

ax2.set_ylim(0,100)
ax2.set_ylabel('Weight (g)')
ax2.set_xlabel('Showing 18 whorls with 3d data on PAS')

ax1.label_outer()
#ax2.label_outer()
plt.show()