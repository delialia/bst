# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUTHOR: Delia Fano Yela
# DATE:  March 2020
# CONTACT: d.fanoyela@qmul.ac.uk
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import seaborn as sns
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
from numpy import mean



df = pd.read_csv('results/results_exp03.csv') # merge.txt to .csv

colors = [ "amber",  "windows blue","faded green" ,"greyish", "dusty purple"]

sns.set(style="white",font_scale=1.2, font = "Times New Roman") #font_scale=1.8

sns.set_palette(sns.xkcd_palette(colors))
# sns.set_context("paper",font_scale=0.5, rc = {'lines.linewidth':0.5})
sns.set_context( {'lines.linewidth':0.8})

g = sns.catplot(x="size ratio", y="time ratio",  hue='N', data = df, kind="point", legend_out = False,
                 markers = ['o', 'x', 'v'], linestyles = ["-.","--","-"]) #height = 8  height = 8, aspect = 1,

g.set( yscale="log")
g.set(xlabel=r'size ratio ($n_{series}/n_{batch}$)', ylabel=r'time ratio ($t_{off-line}/t_{on-line}$)')
g.set( ylim =[0.5, 1000])
g.set_xticklabels(['1', '10', '100', '1000'])
ax = g.axes[0,0]

# ax.set_title("Merge Function Efficiency",fontsize = 24)#, fontweight='bold' )
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
# ax.spines['left'].set_linewidth(0.5)

leg = g.axes.flat[0].get_legend()
new_title = r'\Large{$n_{batch}$}'
leg.set_title(new_title)


plt.savefig('plot_exp03.pdf')
# plt.show()
