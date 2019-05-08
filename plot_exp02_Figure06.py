import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import SeabornFig2Grid as sfg
import matplotlib.gridspec as gridspec

sns.set(style="whitegrid")

#Series samples:
df_series = pd.read_csv('samples_spfn.csv')
df_series["type"] = df_series["type"].map({'finance': 'Finance Series', 'speech': 'Speech Series'})

ds = {"color" : "k"}
s = sns.FacetGrid(df_series, col="type", sharey = False, sharex = False, hue_kws=ds)

kws = dict(linewidth=.5)
s = s.map(plt.plot, "y", **kws)
s.set_titles('{col_name}')
ax = s.axes
for i in xrange(ax.shape[0]):
    for j in xrange(ax.shape[1]):
        ax[i,j].spines['right'].set_visible(False)
        ax[i,j].spines['top'].set_visible(False)
        ax[i,j].yaxis.set_ticks_position('left')
        ax[i,j].xaxis.set_ticks_position('bottom')
        ax[i,j].set_xlabel('t')
        if j < 1:
            ax[i,j].set_ylabel('y')

#  Computation times
df = pd.read_csv('finance_speech.csv')
df["Method"] = df["Method"].map({'basic': 'Basic', 'dc': 'DC', 'bt': 'BST'})


g = sns.FacetGrid(df, col = 'Type', hue = "Method",
                     sharey = False, margin_titles = True, legend_out = False,
                     hue_kws=dict(marker=[".","^", "v"]),palette = 'Set2') #sharey = "row",sharex = "row"


g = g.map(sns.stripplot, "Visibility","Computation Time (s)")
g.add_legend()
g.set_titles( col_template = ' ')
ax = g.axes
for i in xrange(ax.shape[0]):
    for j in xrange(ax.shape[1]):
        ax[i,j].spines['right'].set_visible(False)
        ax[i,j].spines['top'].set_visible(False)
        ax[i,j].yaxis.set_ticks_position('left')
        ax[i,j].xaxis.set_ticks_position('bottom')


fig = plt.figure(figsize=(16,12) )
gs = gridspec.GridSpec(2, 1)

mg0 = sfg.SeabornFig2Grid(s, fig, gs[0])
mg1 = sfg.SeabornFig2Grid(g, fig, gs[1])


fig.savefig('images/plot_exp02.png')
plt.show()
