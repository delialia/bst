import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from numpy import mean

df = pd.read_csv('merge.csv')

sns.set(style="whitegrid")
sns.set_palette("Paired")

g = sns.catplot(x="size ratio", y="time ratio",  hue='N', data = df, kind="point", legend_out = False,
                height = 8, aspect = 1, markers = ['o', 'x', 'v'], linestyles = ["-.","--","-"])

g.set( yscale="log")
g.set_titles('{col_name}')
ax = g.axes

for i in xrange(ax.shape[0]):
    for j in xrange(ax.shape[1]):
        ax[i,j].spines['right'].set_visible(False)
        ax[i,j].spines['top'].set_visible(False)
        ax[i,j].yaxis.set_ticks_position('left')
        ax[i,j].xaxis.set_ticks_position('bottom')



ax = plt.gca()
ax.set_title("Merge Function Efficiency")

plt.savefig('images/plot_exp03.png')
plt.show()
