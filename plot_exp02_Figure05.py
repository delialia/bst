import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import SeabornFig2Grid as sfg
import matplotlib.gridspec as gridspec
from collections import OrderedDict

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

sns.set(style="white",font_scale = 2.5, font = "Times New Roman")

#Series samples:
df_series = pd.read_csv('sample_data/samples_spfn.csv')

ds = {"color" : "k"}
s = sns.FacetGrid(df_series, col="type", sharey = False, sharex = False, hue_kws=ds)

kws = dict(linewidth=.5)
s = s.map(plt.plot, "y", **kws)

# titles = ['Speech Series','Finance Series']
titles = ['\t (a)', '\t (b)']

ax = s.axes
for i in xrange(ax.shape[0]):
    for j in xrange(ax.shape[1]):
        ax[i,j].set_title(' ')
        ax[i,j].set_title(titles[j], loc = 'left')#, fontweight='bold')
        ax[i,j].spines['right'].set_visible(False)
        ax[i,j].spines['top'].set_visible(False)
        ax[i,j].yaxis.set_ticks_position('left')
        ax[i,j].xaxis.set_ticks_position('bottom')
        ax[i,j].set_xlabel('time')
        ax[i,j].xaxis.set_ticklabels(' ')
        ax[i,j].yaxis.set_ticklabels(' ')
        if j < 1:
            ax[i,j].set_ylabel('y')

#  Computation times
df = pd.read_csv('results/results_exp02.csv') # unify finance.txt and speech.txt
df["Method"] = df["Method"].map({'basic': 'Basic', 'dc': 'DC', 'bt': 'BST'})


g = sns.FacetGrid(df, col = 'Type', hue = "Method",
                     sharey = False, margin_titles = True, legend_out = False,
                     hue_kws=dict(marker=[".","^", "v"]),palette = 'Set2') #sharey = "row",sharex = "row"


g = g.map(sns.stripplot, "visibility","computation time (s)", s=6)
# g.add_legend(title='')
g.set_titles( col_template = ' ')
ax = g.axes
for i in xrange(ax.shape[0]):
    for j in xrange(ax.shape[1]):
        ax[i,j].spines['right'].set_visible(False)
        ax[i,j].spines['top'].set_visible(False)
        ax[i,j].yaxis.set_ticks_position('left')
        ax[i,j].xaxis.set_ticks_position('bottom')

ax[0,0].set_ylabel('comp. time (s)')
ax[0,0].set_ylim([-0.1, 3])
ax[0,0].set_yticks([0,1,2,3])

ax[0,1].set_ylim([-0.3, 10])
ax[0,1].set_yticks([0,2,4,6,8,10])

g.set( xticklabels =['NVg', 'HVg'])
# g.set( ylabel = 'comp. time (s)')


handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), scatterpoints = 1, markerscale = 3 )


fig = plt.figure(figsize=(12,10) )
gs = gridspec.GridSpec(2, 1)

mg0 = sfg.SeabornFig2Grid(s, fig, gs[0])
mg1 = sfg.SeabornFig2Grid(g, fig, gs[1])


fig.savefig('plot_exp02.jpg')
# plt.show()
