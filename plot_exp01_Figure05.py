 import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import SeabornFig2Grid as sfg
import matplotlib.gridspec as gridspec

sns.set(style="whitegrid")


df_series = pd.read_csv('series.csv')
df_series["type"] = df_series["type"].map({'random': 'Random Series', 'random_walk': 'Random Walk Series', 'conway':'Conway Series'})
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

#----------------------------------------------------------------------------------------------------
df = pd.read_csv('results_exp01.csv') # manually go from .txt to .csv

df["Method"] = df["Method"].map({'basic': 'Basic', 'dc': 'DC', 'bt':'BST'})

# Uncomment to calculate the mean:
# df_plot = df.groupby(['Method', "series size n", "visibility", "series_type"]).mean()
# df_plot.to_csv('df_mean.csv',index=True)

df_p2 = pd.read_csv('df_mean.csv')
d = {"ls":["--","-.","-"]}
#----------------------------------------------------------------------------------------------------
g = sns.FacetGrid(df_p2, col="series_type", row="visibility", hue="Method",
                     sharey = 'col', sharex = "row", margin_titles = True, legend_out = False,
                     col_order=['random', 'walk', 'conway'], row_order=['nvg', 'hvg'],
                     hue_kws=d,palette = 'Set2')

kws = dict(linewidth=2)
g = (g.map(plt.plot, "series size n", "computation time (s)", marker= ".", **kws).add_legend(label_order=["Basic", "DC", "BST"]))


g.set(xscale="log", yscale="log")
g.set_titles( col_template = ' ')
g.set( xlim =[50, 5e3])
g.set( ylim =[1e-4, 1e2])
ax = g.axes
for i in xrange(ax.shape[0]):
    for j in xrange(ax.shape[1]):
        ax[i,j].spines['right'].set_visible(False)
        ax[i,j].spines['top'].set_visible(False)
        ax[i,j].yaxis.set_ticks_position('left')
        ax[i,j].xaxis.set_ticks_position('bottom')

#----------------------------------------------------------------------------------------------------
fig = plt.figure(figsize=(22,14) )
gs = gridspec.GridSpec(3, 1)

mg0 = sfg.SeabornFig2Grid(s, fig, gs[0])
mg1 = sfg.SeabornFig2Grid(g, fig, gs[1:3])


fig.savefig('images/plot_exp01.png')
plt.show()
