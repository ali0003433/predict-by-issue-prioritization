import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_bar(x, y, palette, title, xlabels): 
    plt.figure(figsize=(8, 7))
    bar_plot = sns.barplot(x=x, y=y,palette=palette)
    bar_plot.set_title(title)
    bar_plot.set_xticklabels(rotation=90, labels=xlabels)
    bar_plot.set_ylabel('Weighted frequency')
    return bar_plot


def plot_stacked(data, title):
    palette_short = ['cornflowerblue','tomato','lightgrey']
    stacked_plot = data.T.plot(kind='bar', stacked=True, color=palette_short)
    stacked_plot.set_title(title)
    pres_cat_list = ['Clinton', 'Trump', 'Other behavior']
    stacked_plot.legend(pres_cat_list)
    N = 5 
    ind = np.arange(N)
    stacked_plot.set_xlabel('')
    x_ticks = ('Very','Somewhat','Not very', 'Unimportant', 'No Response')
    y_label = 'Weighted frequency'
    plt.xticks(ind, x_ticks)
    stacked_plot.set_ylabel(y_label)
    stacked_plot.set(ylim=(0,2.1))
    return stacked_plot

def count_res(df):
    count_dict = {1: 0, 2: 0, 3: 0, 4: 0, 8: 0}
    for idx, row in df.iterrows():
        for col in df.columns:
            res = row[col]
            count_dict[res] +=1
    return count_dict