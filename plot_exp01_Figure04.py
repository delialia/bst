import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import SeabornFig2Grid as sfg
import matplotlib.gridspec as gridspec

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

sns.set(style="white", font_scale=2, font = "Times New Roman")
df_series = pd.read_csv('sample_data/series.csv')

ds = {"color" : "k"}
s = sns.FacetGrid(df_series, col="type", sharey = False, sharex = False, hue_kws=ds)
kws = dict(linewidth=.5)
s.map(plt.plot, "y", **kws)

titles = ['\t (a)', '\t (b)', ' \t (c)']

axes = s.axes.flatten()

for ax in axes :
    ax.set_title(' ')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_ticklabels(' ')
    ax.yaxis.set_ticklabels(' ')
    ax.set_xlabel('time')

axes[0].set_title(titles[0], loc='left')
axes[1].set_title(titles[1], loc='left')
axes[2].set_title(titles[2], loc='left')
axes[0].set_ylabel('y')


#----------------------------------------------------------------------------------------------------
df = pd.read_csv('results/results_exp01.csv')

df["Method"] = df["Method"].map({'basic': 'Basic', 'dc': 'DC', 'bt':'BST'})

# Uncomment to calculate the mean:
# df_plot = df.groupby(['Method', "series size n", "visibility", "series_type"]).mean()
# df_plot.to_csv('df_mean.csv',index=True)

df_p2 = pd.read_csv('sample_data/df_mean.csv')
d = {"ls":["--","-.","-"]}
#----------------------------------------------------------------------------------------------------
g = sns.FacetGrid(df_p2, col="series_type", row="visibility", hue="Method",
                     sharey = 'col', sharex = "row", margin_titles = True, legend_out = False,
                     col_order=['random', 'walk', 'conway'], row_order=['nvg', 'hvg'],
                     hue_kws=d,palette = 'Set2')

kws = dict(linewidth=2)
g.map(plt.plot, "series size n", "computation time (s)", marker= ".", **kws).add_legend(label_order=["Basic", "DC", "BST"],title='')


axes = g.axes.flatten()
for ax in axes :
    ax.set_title(' ')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_ylabel('')



axes[0].set_ylabel('NVg comp. time (s)')
axes[3].set_ylabel('HVg comp. time (s)')



g.set(xscale="log", yscale="log")
g.set_titles( col_template = ' ')
g.set( xlim =[50, 5200])
g.set( ylim =[0.0005, 500])


#----------------------------------------------------------------------------------------------------
fig = plt.figure(figsize=(20,12))
gs = gridspec.GridSpec(3, 1)

mg0 = sfg.SeabornFig2Grid(s, fig, gs[0])
mg1 = sfg.SeabornFig2Grid(g, fig, gs[1:3])


#----------------------------------------------------------------------------------------------------
fig.savefig('plot_exp01.jpg')
# plt.show()
